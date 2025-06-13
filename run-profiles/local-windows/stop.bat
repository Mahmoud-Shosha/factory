@echo off
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0..\banner.ps1"
docker compose -f .\compose.yaml down

:checkloop
echo Stopping Experts Vision Odoo ...
curl --silent --fail http://localhost:8069 >nul
if %errorlevel%==0 (
    timeout /t 2 >nul
    goto checkloop
)