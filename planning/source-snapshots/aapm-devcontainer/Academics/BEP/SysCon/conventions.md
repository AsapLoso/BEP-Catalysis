# BEP System & Control (SysCon) Project Conventions

This file documents the conventions and guidelines unique to the BEP System & Control (Adaptive Optics) project.

## 🎛️ Project Guidelines

### 1. Dual Degree Integration
- Ensure all modeling options satisfy both Applied Physics and Applied Mathematics BEP requirements.
- Focus on control theory, state-space modeling, recursive least squares, and Kalman filtering, with clear application to Adaptive Optics.

### 2. File & Tracking Conventions
- **State History:** Preserve state transitions by appending the old state to `history.log` before making modifications to `state.md`.
- **Reference Materials:** Keep academic literature, external links, and reading materials in `resources.md`, linking to them from `state.md`.
- **Target Contacts:** Maintain clear tracking of supervisor contacts (Dylan Kalisvaart, Carlas Smith) in `state.md`.
