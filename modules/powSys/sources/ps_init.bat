@echo off
title Administry - Power Scheme Installation rev 0.1
:INS_STR
:: BatchGotAdmin
:-------------------------------------
REM  --> Check for permissions
    IF "%PROCESSOR_ARCHITECTURE%" EQU "amd64" (
>nul 2>&1 "%SYSTEMROOT%\SysWOW64\cacls.exe" "%SYSTEMROOT%\SysWOW64\config\system"
) ELSE (
>nul 2>&1 "%SYSTEMROOT%\system32\cacls.exe" "%SYSTEMROOT%\system32\config\system"
)

REM --> If error flag set, we do not have admin.
if '%errorlevel%' NEQ '0' (
    echo Requesting administrative privileges...
    goto UACPrompt
) else ( goto gotAdmin )

:UACPrompt
    echo Set UAC = CreateObject^("Shell.Application"^) > "%temp%\getadmin.vbs"
    set params= %*
    echo UAC.ShellExecute "cmd.exe", "/c ""%~s0"" %params:"=""%", "", "runas", 1 >> "%temp%\getadmin.vbs"

    "%temp%\getadmin.vbs"
    del "%temp%\getadmin.vbs"
    exit /B

:gotAdmin
    pushd "%CD%"
    CD /D "%~dp0"
:--------------------------------------  
echo Please Wait...
powercfg import "%UserProfile%\AppData\Roaming\Administry\powSys\gamingScheme.pow" a8ff579c-aed1-49c0-a69c-fc5b5f2d968a
powercfg import "%UserProfile%\AppData\Roaming\Administry\powSys\silentScheme.pow" 3c857587-cf01-4c11-8da8-0f43f3c2ad98
timeout /t 1 >nul
cls
echo Done!
timeout /t 2 >nul
exit


pause