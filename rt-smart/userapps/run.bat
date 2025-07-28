@echo off
setlocal

:: 获取脚本所在目录（当前目录）
set "SCRIPT_DIR=%~dp0"


set "QEMU_SCRIPT=%SCRIPT_DIR%..\kernel\bsp\qemu-vexpress-a9\qemu-nographic.bat"
:: 检查目标脚本是否存在
if not exist "%QEMU_SCRIPT%" (
    echo Error: qemu-dbg.bat not found at:
    echo %QEMU_SCRIPT%
    pause
    exit /b 1
)

:: 运行 QEMU 调试脚本
echo Starting QEMU debug session...
call "%QEMU_SCRIPT%"

:: 检查执行结果
if errorlevel 1 (
    echo Error: QEMU debug session failed with error %errorlevel%
) else (
    echo QEMU debug session completed successfully
)