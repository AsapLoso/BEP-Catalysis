import numpy as np
from scipy.integrate import solve_ivp

# =============================================================================
# 1. PARAMETERS (Open gelaten voor literatuurwaarden)
# =============================================================================

class ModelParams:
    # --- Reactor & Hardware Parameters ---
    L = 0.5           # [m] Reactor lengte
    R_p = 0.002       # [m] Catalyst deeltjes radius
    epsilon_b = 0.4   # [-] Bed porositeit (void fraction)
    epsilon_p = 0.5   # [-] Deeltjes porositeit
    rho_s = 1200.0    # [kg/m3] Dichtheid van het katalysatordeeltje
    C_t = 1.0         # [mol/kg] Totale actieve site capaciteit
    u_s = 0.1         # [m/s] Superficial gas velocity
    s = 2             # [-] Geometrie factor (2 = sfeer)

    # --- Operationele Parameters ---
    T = 400.0         # [K] Isothermische temperatuur
    R_G = 8.314       # [J/mol.K] Gasconstante
    
    # Inlet concentraties [mol/m3]
    C_inlet = {
        'H2': 10.0,
        'C2H2': 1.0,
        'C2H4': 0.0,
        'C2H6': 0.0
    }

    # --- Kinetische Parameters (Arrhenius Reference & Activation) ---
    # Structuur: 'Reactie': (k_ref, E_a)
    # Let op: Dit zijn placeholders. Zowel adsorptie/desorptie als oppervlaktereacties.
    kinetics = {
        'ads_H2':   (0.0, 0.0), # H2 + 2* <-> 2H*
        'des_H2':   (0.0, 0.0),
        'ads_C2H2': (0.0, 0.0), # C2H2 + * <-> C2H2*
        'des_C2H2': (0.0, 0.0),
        'ads_C2H4': (0.0, 0.0), # C2H4 + * <-> C2H4*
        'des_C2H4': (0.0, 0.0),
        'surf_R1':  (0.0, 0.0), # C2H2* + 2H* -> C2H4* + 2* (Reactie 1)
        'surf_R2':  (0.0, 0.0)  # C2H4* + 2H* -> C2H6 + 3*  (Reactie 2)
    }
    
    # --- Transport Parameters ---
    # Effectieve diffusiviteit in de poriën [m2/s]
    D_e = {
        'H2': 1e-6,
        'C2H2': 1e-6,
        'C2H4': 1e-6,
        'C2H6': 1e-6
    }

# =============================================================================
# 2. DISCRETISATIE & INDEXERING
# =============================================================================

N_z = 20  # Aantal nodes over de reactorlengte
N_r = 10  # Aantal nodes over de deeltjesradius

# Species definities en indexering voor arrays
gas_species = ['H2', 'C2H2', 'C2H4', 'C2H6']
surf_species = ['H_star', 'C2H2_star', 'C2H4_star']

N_gas = len(gas_species)
N_surf = len(surf_species)

# =============================================================================
# 3. KINETISCHE WETTEN (De "Twee Reacties" C2H2 -> C2H4 -> C2H6)
# =============================================================================

def calculate_rates(cp_gas, theta, p: ModelParams):
    """
    Berekent de netto productiesnelheden (R_i en R_j) voor een specifiek (z, r) punt.
    cp_gas: array van [H2, C2H2, C2H4, C2H6] in de porie
    theta: array van [H*, C2H2*, C2H4*]
    """
    # Unpack concentraties
    cp_H2, cp_C2H2, cp_C2H4, cp_C2H6 = cp_gas
    theta_H, theta_C2H2, theta_C2H4 = theta
    
    # Vrije sites (site balance)
    theta_v = 1.0 - (theta_H + theta_C2H2 + theta_C2H4)
    
    # Helper functie voor Arrhenius (Hier gesimplificeerd naar k_ref voor demonstratie)
    # In een volledig model: k = k_ref * exp(-Ea/R * (1/T - 1/Tref))
    k = lambda name: p.kinetics[name][0] 

    # --- Elementaire stappen ---
    # 1. H2 Adsorptie/Desorptie (Dissociatief)
    r_ads_H2 = k('ads_H2') * cp_H2 * (theta_v ** 2) - k('des_H2') * (theta_H ** 2)
    
    # 2. C2H2 Adsorptie/Desorptie
    r_ads_C2H2 = k('ads_C2H2') * cp_C2H2 * theta_v - k('des_C2H2') * theta_C2H2
    
    # 3. Oppervlaktereactie 1: C2H2* + 2H* -> C2H4* + 2*
    r_R1 = k('surf_R1') * theta_C2H2 * (theta_H ** 2)
    
    # 4. C2H4 Desorptie/Adsorptie
    r_des_C2H4 = k('des_C2H4') * theta_C2H4 - k('ads_C2H4') * cp_C2H4 * theta_v
    
    # 5. Oppervlaktereactie 2: C2H4* + 2H* -> C2H6(g) + 3* (Ethaan desorbeert direct)
    r_R2 = k('surf_R2') * theta_C2H4 * (theta_H ** 2)

    # --- Stoichiometrie: Netto Gas Productie (R_i) [mol / kg_cat s] ---
    R_gas = np.zeros(N_gas)
    R_gas[0] = -r_ads_H2                # H2
    R_gas[1] = -r_ads_C2H2              # C2H2
    R_gas[2] = r_des_C2H4               # C2H4
    R_gas[3] = r_R2                     # C2H6
    
    # --- Stoichiometrie: Netto Oppervlakte Accumulatie (R_j) [1/s] ---
    R_surf = np.zeros(N_surf)
    R_surf[0] = 2 * r_ads_H2 - 2 * r_R1 - 2 * r_R2  # H*
    R_surf[1] = r_ads_C2H2 - r_R1                   # C2H2*
    R_surf[2] = r_R1 - r_des_C2H4 - r_R2            # C2H4*
    
    return R_gas, R_surf

# =============================================================================
# 4. DE DIFFERENTIAALVERGELIJKINGEN (MOL Framework)
# =============================================================================

def reactor_model(t, y, p: ModelParams):
    """
    De core ODE functie die aan solve_ivp wordt gevoerd.
    Evalueert de ruimtelijke afgeleiden van Buiten (Bulk) naar Binnen (Porie -> Chemie).
    """
    # 1. State vector y uitpakken in leesbare 3D/2D arrays
    # y opbouw: [C_b (N_z*N_gas), c_p (N_z*N_r*N_gas), theta (N_z*N_r*N_surf)]
    idx1 = N_z * N_gas
    idx2 = idx1 + (N_z * N_r * N_gas)
    
    C_b = y[0:idx1].reshape((N_z, N_gas))
    c_p = y[idx1:idx2].reshape((N_z, N_r, N_gas))
    theta = y[idx2:].reshape((N_z, N_r, N_surf))
    
    # Arrays initialiseren voor de afgeleiden (d/dt)
    dCb_dt = np.zeros_like(C_b)
    dcp_dt = np.zeros_like(c_p)
    dTheta_dt = np.zeros_like(theta)
    
    dz = p.L / N_z
    dr = p.R_p / (N_r - 1)  # N_r punten betekent N_r-1 intervallen
    
    D_e_array = np.array([p.D_e[s] for s in gas_species])
    
    # Inlet randvoorwaarde array
    Cb_in = np.array([p.C_inlet[s] for s in gas_species])

    # 2. Ruimtelijke Loop over de Reactor (z-as)
    for z in range(N_z):
        
        # Pseudo-homogene aanname: Oppervlakteconcentratie = Bulkconcentratie
        C_s = C_b[z, :]
        
        # Deeltjes randvoorwaarde: Buitenste schil van deeltje (r = R_p) gelijk aan C_s
        c_p[z, -1, :] = C_s 
        dcp_dt[z, -1, :] = 0.0 # Wordt algebraïsch gedicteerd door de bulk, geen ODE
        
        R_gas_integraal = np.zeros(N_gas)
        
        # 3. Ruimtelijke Loop over het Deeltje (r-as)
        for r in range(N_r - 1): # Buitenste schil is al gedefinieerd
            r_radius = r * dr
            
            # Kinetiek en Stoichiometrie
            R_gas, R_surf = calculate_rates(c_p[z, r, :], theta[z, r, :], p)
            
            # Oppervlakte ODE (Accumulatie van actieve sites)
            dTheta_dt[z, r, :] = R_surf
            
            # Porie diffusie PDE (Discretisatie via eindige differenties)
            reactie_term = (p.rho_s * p.C_t / p.epsilon_p) * R_gas
            
            if r == 0:
                # Centrum (r=0): L'Hôpital / Symmetrie randvoorwaarde
                # d2c/dr2 approx = 2 * (c[1] - c[0]) / dr^2 (voor sfeer is het 6 ipv 2 in de limiet)
                diff_term = (D_e_array / p.epsilon_p) * ( (1 + p.s) * (c_p[z, 1, :] - c_p[z, 0, :]) / (dr**2) )
                dcp_dt[z, r, :] = diff_term + reactie_term
            else:
                # Interne nodes (CENTRAL DIFFERENCE SCHEME voor diffusie)
                dc_dr_plus = (c_p[z, r+1, :] - c_p[z, r, :]) / dr
                dc_dr_min  = (c_p[z, r, :] - c_p[z, r-1, :]) / dr
                
                # (1/r^s) d/dr (r^s * dc/dr)
                r_plus_s = (r_radius + dr/2)**p.s
                r_min_s  = (r_radius - dr/2)**p.s
                
                diff_term = (D_e_array / (p.epsilon_p * (r_radius**p.s) * dr)) * (r_plus_s * dc_dr_plus - r_min_s * dc_dr_min)
                dcp_dt[z, r, :] = diff_term + reactie_term
                
            # Integreer de gasproductie over het deeltjesvolume voor de bulkvergelijking
            # dV = afhankelijk van geometrie. Voor een sfeer: 4 * pi * r^2 * dr
            volume_gewicht = (r_radius**p.s) * dr
            R_gas_integraal += R_gas * volume_gewicht

        # Normaliseer integraal (gemiddelde reactiesnelheid in het deeltje)
        R_gas_avg = R_gas_integraal / ( (p.R_p**(p.s + 1)) / (p.s + 1) )

        # 4. Bulk gas PDE (Plug-flow met BACKWARD DIFFERENCE / UPWIND advectie)
        # Dit garandeert stabiliteit voor stromingsprofielen (kijkt alleen upstream).
        transfer_term = (p.rho_s * (1 - p.epsilon_b) * p.C_t / p.epsilon_b) * R_gas_avg
        
        if z == 0:
            advectie_term = - (p.u_s / p.epsilon_b) * (C_b[z, :] - Cb_in) / dz
        else:
            advectie_term = - (p.u_s / p.epsilon_b) * (C_b[z, :] - C_b[z-1, :]) / dz
            
        dCb_dt[z, :] = advectie_term + transfer_term

    # 5. Afgeleiden plat slaan tot één 1D array voor de solver
    return np.concatenate((dCb_dt.flatten(), dcp_dt.flatten(), dTheta_dt.flatten()))

# =============================================================================
# 5. EXECUTIE & IMPLICIETE TIJDSINTEGRATIE
# =============================================================================
if __name__ == "__main__":
    import time
    
    params = ModelParams()
    
    # Bereken totale dimensie van het systeem
    totaal_dimensie = (N_z * N_gas) + (N_z * N_r * N_gas) + (N_z * N_r * N_surf)
    y0 = np.zeros(totaal_dimensie) # Begin met een lege reactor (alles 0)
    
    print(f"Initialisatie compleet. Start simulatie met systeemgrootte: {totaal_dimensie} ODEs.")
    
    # Tijdspanne voor de simulatie
    t_span = (0, 10) # Simuleer de eerste 10 seconden
    
    # Gebruik van de impliciete BDF (Backward Differentiation Formula) methode.
    # Waarom impliciet? Omdat chemische reacties zeer stijf (stiff) zijn vergeleken met diffusie.
    # Een expliciete methode (zoals standaard RK45) zal vastlopen op minuscule benodigde tijdstappen.
    print("Start integratie via impliciete BDF solver (dit kan even duren afhankelijk van kinetiek)...")
    start_time = time.time()
    
    solution = solve_ivp(
        reactor_model, 
        t_span, 
        y0, 
        method='BDF', # IMPLICIETE METHODE
        args=(params,)
    )
    
    end_time = time.time()
    if solution.success:
        print(f"Simulatie succesvol afgerond in {end_time - start_time:.2f} seconden!")
        print(f"Aantal genomen tijdstappen door BDF: {len(solution.t)}")
    else:
        print("Simulatie gefaald:", solution.message)