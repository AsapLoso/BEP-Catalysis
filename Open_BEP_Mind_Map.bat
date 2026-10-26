@echo off
setlocal EnableExtensions
cd /d "%~dp0"
set "BEP_ROOT=%~dp0"

if defined BEP_MINDMAP_PYTHON (
  set "BEP_PYTHON=%BEP_MINDMAP_PYTHON%"
) else (
  if not exist "%BEP_ROOT%.venv\Scripts\python.exe" (
    where py >nul 2>&1
    if not errorlevel 1 (
      py -3 -m venv "%BEP_ROOT%.venv"
    ) else (
      python -m venv "%BEP_ROOT%.venv"
    )
    if errorlevel 1 goto :python_error
  )
  set "BEP_PYTHON=%BEP_ROOT%.venv\Scripts\python.exe"
)

"%BEP_PYTHON%" --version >nul 2>&1
if errorlevel 1 goto :python_error
"%BEP_PYTHON%" -c "import pydantic, yaml" >nul 2>&1
if errorlevel 1 (
  echo Installing the mind-map runtime packages into the selected Python environment...
  "%BEP_PYTHON%" -m pip install --disable-pip-version-check -r "%BEP_ROOT%requirements.txt"
  if errorlevel 1 goto :dependency_error
)

if not defined BEP_MINDMAP_PORT (
  for /f %%P in ('powershell -NoLogo -NoProfile -File "%BEP_ROOT%mindmap\launcher_helpers.ps1" -Action select-port') do set "BEP_MINDMAP_PORT=%%P"
)
if not defined BEP_MINDMAP_PORT goto :port_error
set "BEP_MINDMAP_URL=http://127.0.0.1:%BEP_MINDMAP_PORT%/?mode=owner"

start "BEP Mind Map Server" "%BEP_PYTHON%" -m mindmap.preview --host 127.0.0.1 --port %BEP_MINDMAP_PORT% --owner-map "research\manual_map_sessions_2026_10_22\owner_working_map\current_map.yaml" --reference-map "research\manual_map_sessions_2026_10_22\owner_working_map\reference_map.yaml" --git-root "%CD%" --no-browser
powershell -NoLogo -NoProfile -File "%BEP_ROOT%mindmap\launcher_helpers.ps1" -Action wait-ready -Port %BEP_MINDMAP_PORT% -TimeoutSeconds 45
if errorlevel 1 goto :failed

echo The personal map snapshot is ready at %BEP_MINDMAP_URL%
if not "%BEP_MINDMAP_NO_BROWSER%"=="1" start "" "%BEP_MINDMAP_URL%"
exit /b 0

:python_error
echo Python 3 could not be started. Install Python 3 or set BEP_MINDMAP_PYTHON to its executable path.
goto :failed

:dependency_error
echo The Python packages could not be installed. Check the console output and requirements.txt.
goto :failed

:port_error
echo Could not select a local TCP port. Set BEP_MINDMAP_PORT to an unused port and retry.
goto :failed

:failed
if not "%BEP_MINDMAP_NO_BROWSER%"=="1" pause
exit /b 1
