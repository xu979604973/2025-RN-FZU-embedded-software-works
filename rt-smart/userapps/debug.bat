@echo off
setlocal

set "SCRIPT_DIR=%~dp0"

set "SCRIPT_PATH=%SCRIPT_DIR%..\kernel\bsp\qemu-vexpress-a9\qemu-dbg.bat"

if not exist "%SCRIPT_PATH%" (
    echo Error: qemu-dbg.bat not found at:
    echo %SCRIPT_PATH%
    pause
    exit /b 1
)

echo Starting QEMU debug session...
call "%SCRIPT_PATH%"

if errorlevel 1 (
    echo Error: QEMU debug session failed with error %errorlevel%
) else (
    echo QEMU debug session completed successfully
)