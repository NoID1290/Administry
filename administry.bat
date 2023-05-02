::[Bat To Exe Converter]
::
::YAwzoRdxOk+EWAjk
::fBw5plQjdCqDJBeq+2sUeUkNHESxM22uEbQO7dS17u6Kq0MUR/YtYbPZz72CJNxDpBezSZcp23NUkd8eFSRRfR2UPFpisSBLtWvl
::YAwzuBVtJxjWCl3EqQJgSA==
::ZR4luwNxJguZRRnk
::Yhs/ulQjdF+5
::cxAkpRVqdFKZSDk=
::cBs/ulQjdF+5
::ZR41oxFsdFKZSDk=
::eBoioBt6dFKZSDk=
::cRo6pxp7LAbNWATEpCI=
::egkzugNsPRvcWATEpCI=
::dAsiuh18IRvcCxnZtBJQ
::cRYluBh/LU+EWAnk
::YxY4rhs+aU+IeA==
::cxY6rQJ7JhzQF1fEqQJgZksaHkrVXA==
::ZQ05rAF9IBncCkqN+0xwdVsEAlTMbiXtZg==
::ZQ05rAF9IAHYFVzEqQIRLBZdQg2RKHmjZg==
::eg0/rx1wNQPfEVWB+kM9LVsJDCWGMWK0D6YI+vGb
::fBEirQZwNQPfEVWB+kM9LVsJDCWGMWK0D6YI+vGb
::cRolqwZ3JBvQF1fEqQIHIRVQQxORfEq+C7wSqNz04Obn
::dhA7uBVwLU+EWHeL3WZhekIELA==
::YQ03rBFzNR3SWATE2k0ZDEoGFVTi
::dhAmsQZ3MwfNWATE2k0ZDEoGFVTi
::ZQ0/vhVqMQ3MEVWAtB9weFUEAlbMaws=
::Zg8zqx1/OA3MEVWAtB9weFUEAlbMaws=
::dhA7pRFwIByZRRmz/Uw0JwxHDCWGMWK0RoET5+Sb
::Zh4grVQjdCqDJBeq+2sUeUkNHESxM22uEbQO7dS17u6Kq0MUR/YtYbPZz72CJNxDpBezSbcp23NUkdgYHgIWewquDg==
::YB416Ek+ZG8=
::
::
::978f952a14a936cc963da21a135fa983
:ADMINISTRY BY NOID1290 - 2021©
:FIRSTBOOTKEYDEBUG=G423FGF45GC2RG4F4DFGS546D4G23DGB56FGIFGJH687H8G7
:INSTALLEDBOOTKEYDEBUG=UDFM45FGS546FD4CJSRG4F4DG423FGRG4F4DX78DGTTH74SJXF64TSGH56GF


@echo off
mode con: cols=105 lines=40
setlocal enabledelayedexpansion enableextensions
:begin
title Administry
cls
			


:BOOTKEY
if exist "scripts\firstbootKey.noid" (
GOTO READKEY
) else (
GOTO ERROR_X01D
)
:READKEY
set /p KEY=<scripts\firstbootKey.noid
if %KEY%==G423FGF45GC2RG4F4DFGS546D4G23DGB56FGIFGJH687H8G7 GOTO REGISTER
if %KEY%==UDFM45FGS546FD4CJSRG4F4DG423FGRG4F4DX78DGTTH74SJXF64TSGH56GF GOTO  SPLASHBOOT

:REGISTER
echo Hi! Welcome to Administry.
echo.
echo What is the PC Owner name?
set /p userName=
cls
echo.
echo.
echo Hi %userName%, Thanks you!
set /p ="UDFM45FGS546FD4CJSRG4F4DG423FGRG4F4DX78DGTTH74SJXF64TSGH56GF"<nul >scripts\firstbootKey.noid
echo.
echo Do you want to configure your Power Schemes shortcut now?
echo 1 = Yes
echo 2 = No

choice /n /c:12 /m "Choose a option"%1
if errorlevel ==2 GOTO SPLASHBOOT
if errorlevel ==1 GOTO POW_CONFIG_SELECT
timeout /t 2 >nul
GOTO SPLASHBOOT
pause

:SPLASHBOOT
if not exist cache\ (
GOTO showSB 
) else (
GOTO sb_pass2
)
:sb_pass2
if not exist "cache/ssbcInit.noid" (
GOTO showSB 
) else (
GOTO sb_pass3
pause
)
:sb_pass3
set /p sb_ValueFile=<cache\ssbcInit.noid
if %sb_ValueFile%==F87AHN GOTO showSB
if %sb_ValueFile%==PXC28S GOTO bypass_SB


:showSB
color 6
type scripts\asciiSplash-100.noid
timeout /t 2 >nul
cls
:bypass_SB

:CHECK_FOLDERCACHE
if exist cache\ (
  GOTO CHECK_IFSTREAMEXIST 
) else (
  mkdir cache
  echo Folder cache created
  
timeout /t 3 >nul
GOTO CHECK_TEMPFILE
)

:CHECK_TEMPFILE
if exist "hpviTemp.noid" (
copy hpviTemp.noid cache\hpValueGUID.noid
copy sviTemp.noid cache\svValueGUID.noid
echo Cleaning Temporary Files...
timeout /t 1 >nul
del hpviTemp.noid
del sviTemp.noid
echo Done
GOTO CHECK_IFSTREAMEXIST
) else (
GOTO CHECK_IFSTREAMEXIST
)

:CHECK_IFSTREAMEXIST
if exist "stream/cnfm.wav" (
GOTO CHECK_IFCACHE_EXIST
) else (
GOTO SET_STREAMCACHE
)

:SET_STREAMCACHE
set "file=stream/cnfm.wav"
( echo Set Sound = CreateObject("WMPlayer.OCX.7"^)
  echo Sound.URL = "%file%"
  echo Sound.Controls.play
  echo do while Sound.currentmedia.duration = 0
  echo wscript.sleep 100
  echo loop
  echo wscript.sleep (int(Sound.currentmedia.duration^)+1^)*1000) >scripts/audioScript_cnfm.vbs
  
  
set "file=stream/err.wav"
( echo Set Sound = CreateObject("WMPlayer.OCX.7"^)
  echo Sound.URL = "%file%"
  echo Sound.Controls.play
  echo do while Sound.currentmedia.duration = 0
  echo wscript.sleep 100
  echo loop
  echo wscript.sleep (int(Sound.currentmedia.duration^)+1^)*1000) >scripts/audioScript_err.vbs     
:END_SET_STREAMCACHE 





:CHECK_IFCACHE_EXIST
if exist "cache/HUD.noid" (
GOTO LOADCOLORCACHE
) else (
color 3f
GOTO PASS_COLORCHECK
)

:LOADCOLORCACHE
set /p colorHUD_cache=<cache/HUD.noid
if %colorHUD_cache%==BLUE color 1
if %colorHUD_cache%==AQUA color 3
if %colorHUD_cache%==DEFAULT color A
if %colorHUD_cache%==RED color 4
if %colorHUD_cache%==BL color 3f
:PASS_COLORCHECK


:CHECKPATH_1
if exist cache\ (
GOTO CHECKPATH_2
) else (
ECHO SOME FILE IS MISSING! PLEASE REINSTALL!
pause
GOTO KILL
)
:CHECKPATH_2
if exist stream\ (
GOTO LOAD_PROGRAM
) else (
mkdir stream
set /p ="F0X3"<nul >cache/userAdmin.noid
copy C:\Windows\Media\ding.wav stream\cnfm.wav
copy C:\Windows\Media\chord.wav stream\err.wav
GOTO LOAD_PROGRAM
)


  
:LOAD_PROGRAM
cls
set VER=				v0.27
set X01=		*****************************************
set X02=		     ADMINISTRY by NoID1290 - 2021(C)
set X03= 			%DATE% %TIME%
set X04=powercfg /getactivescheme
set XOS=%OS%
set CPU_ID=%PROCESSOR_IDENTIFIER%
set CPU_LOGICAL_CORES=%NUMBER_OF_PROCESSORS%
set USER=%COMPUTERNAME%
set VOID=			



echo %X01%
echo %X02%
echo %X03%
echo %VER%
echo %X01%



:CHECKCACHE_USERSETPOWER
if exist "cache/userSet.noid" (
GOTO LOAD_POWERCACHE
) else (
set /p ="DEFAULT"<nul >cache/userSet.noid
set /p ="%userName%"<nul >cache/userProfil.noid
echo System cache file created!
timeout /t 3 >nul
GOTO begin
)

:LOAD_POWERCACHE
set /p config=<cache/userSet.noid

:LOAD_USERPROFIL
if exist "cache/userProfil.noid" (
set /p userValue=<cache/userProfil.noid
GOTO SHOW_USERPROFIL
) else (
GOTO SHOWCACHE
)

:SHOW_USERPROFIL
echo Welcome Back %userValue%


:SHOWCACHE
if %config%==f71556f20b4a ( 
set OX01= Power Saving *
) else ( set OX01= Power Saving
)

if %config%==b7cd3ecb2790 (
set OX02= High Performance *
) else ( set OX02= High Performance
)

echo.
echo.

:MAIN MENU
echo 1: Monitor Off
echo 2:%OX01%
echo 3:%OX02%
echo.
echo 7: More Tools...
echo 8: Settings
echo 9: Exit

choice /n /c:123456789 /m "Choose a option"%1


if errorlevel ==9 GOTO KILL
if errorlevel ==8 GOTO SETTINGS
if errorlevel ==7 GOTO MOPTS
if errorlevel ==6 GOTO UKNW_COMMAND
if errorlevel ==5 GOTO UKNW_COMMAND
if errorlevel ==4 GOTO UKNW_COMMAND
if errorlevel ==3 GOTO HPERFORMANCE_SET
if errorlevel ==2 GOTO SILENT_SET
if errorlevel ==1 GOTO MONITOR_OFF

GOTO END

:MOPTS
cls
echo %X01%
echo %X02%
echo %X03%
echo %VER%
echo %X01%
echo.
echo.

echo 1: System Information
echo 2: IP/Ethernet 
echo 3: Restart explorer
echo 4: Admin Tools
echo 5: Control Panel
echo 6: Programs Start-up Folder
echo 7: Ping Website
echo 8: Basic Text/Password Encryption
echo.
echo 9: Return

choice /n /c:123456789 /m "Choose a option (1 ,2 or 3)"%1

if errorlevel ==9 GOTO LOAD_PROGRAM
if errorlevel ==8 GOTO ENCRYPT_MENU
if errorlevel ==7 GOTO PING_WEBSITE
if errorlevel ==6 GOTO STARTUP_FOLDER
if errorlevel ==5 GOTO CTRLPANEL
if errorlevel ==4 GOTO ADMIN_TOOLS
if errorlevel ==3 GOTO EXP_SHUTDOWN
if errorlevel ==2 GOTO IPCONFIG
if errorlevel ==1 GOTO SYINFO

GOTO END


pause
GOTO END


:ADMIN_TOOLS
cls
echo %X01%
echo %X02%
echo %X03%
echo %VER%
echo %X01%
echo.
echo.
echo 1: DISKPART
echo 2: REGISTRY EDITOR
echo 3: LOCAL USER AND GROUP MANAGEMENT
echo 4: DirectX Diagnostic Tool
echo 5: Windows Features
echo 6: GOD MODE [WINDOWS MASTER CONTROL PANEL]
echo 7: Refresh Monitor and Graphic Card
echo 9: Return

choice /n /c:123456789 /m "Choose a option (1 ,2 or 3)"%1

if errorlevel ==9 GOTO MOPTS
if errorlevel ==8 GOTO UKNW_COMMAND_ADMINTOOLS
if errorlevel ==7 GOTO REFRESH_MENU
if errorlevel ==6 GOTO MASTER_CTRL
if errorlevel ==5 GOTO WINF
if errorlevel ==4 GOTO DXDIAG
if errorlevel ==3 GOTO LUSRMGR
if errorlevel ==2 GOTO REGEDIT
if errorlevel ==1 GOTO DISKPART

GOTO END

pause

:SETTINGS
cls
echo %X01%
echo %X02%
echo %X03%
echo %VER%
echo %X01%
echo.
echo.
echo 1: Change Color HUD
echo 2: Turn On/Off Bootscreen Logo
echo 3: Turn On/Off auto close
echo 4: Set default TimeWait
echo.
echo 8: Reset All Settings
echo 9: Return

choice /n /c:123456789 /m "Choose a option (1 ,2 or 3)"%1

if errorlevel ==9 GOTO LOAD_PROGRAM
if errorlevel ==8 GOTO RESET_CFG
if errorlevel ==7 GOTO UKNW_COMMAND_SETTINGS
if errorlevel ==6 GOTO UKNW_COMMAND_SETTINGS
if errorlevel ==5 GOTO UKNW_COMMAND_SETTINGS
if errorlevel ==4 GOTO UKNW_COMMAND_SETTINGS
if errorlevel ==3 GOTO UKNW_COMMAND_SETTINGS
if errorlevel ==2 GOTO SET_SPLASHBOOT_CONFIG
if errorlevel ==1 GOTO COLORHUD

:DISKPART
diskpart
GOTO ADMIN_TOOLS

:REGEDIT
regedit
GOTO ADMIN_TOOLS

:LUSRMGR
lusrmgr
GOTO ADMIN_TOOLS

:CTRLPANEL
control
GOTO MOPTS

:DXDIAG
dxdiag
GOTO ADMIN_TOOLS

:WINF
optionalfeatures
GOTO ADMIN_TOOLS

:MASTER_CTRL
explorer.exe shell:::{ED7BA470-8E54-465E-825C-99712043E01C}
GOTO ADMIN_TOOLS

:STARTUP_FOLDER
explorer.exe shell:startup
GOTO MOPTS

:PING_WEBSITE
cls
echo %X01%
echo %X02%
echo %X03%
echo %VER%
echo %X01%
echo.
echo.
echo Enter the website you would like to ping
set input=
set /p input= Enter your Website here:

	cls
	echo %X01%
	echo %X02%
	echo %X03%
	echo %VER%
	echo %X01%
	echo.
	echo.

echo Processing Your Request For ''%input%''
ping localhost>nul
ping localhost>nul
echo Result=
ping %input%
echo Please Wait...
ping localhost -n 10 >nul
echo Done!
pause
:B
GOTO BEGIN

:ENCRYPT_MENU
cls
echo %X01%
echo %X02%
echo %X03%
echo %VER%
echo %X01%
echo.
echo.
echo Basic Encryption 1.0 - based on Batch Text Encrypter by Batchcc
echo.
echo.
echo 1: Encrypt Text/Password
echo 2: Decrypt Text/Password
echo.
echo 3: Return


choice /n /c:123 /m "Choose a option"%1
if errorlevel ==3 GOTO MOPTS
if errorlevel ==2 GOTO decrypt
if errorlevel ==1 GOTO encrypt



:encrypt
cls
echo %X01%
echo %X02%
echo %X03%
echo %VER%
echo %X01%
echo.
echo.
echo Enter or paste your text/password:
set /p encryptPending=
set /p =%encryptPending%<nul >scripts/userInputPending.noid
echo Waiting for encryption return...
start /wait scripts\encrypt.exe
set /p encryptResult=<scripts/encryptResult.noid
cls
echo %X01%
echo %X02%
echo %X03%
echo %VER%
echo %X01%
echo.
echo.
echo Encryption done.
echo Result = %encryptResult%
echo.
echo.
echo Do you want a Text File on your Desktop of this result?
echo.
echo.
echo 1: Yes
echo 2: No


choice /n /c:123 /m "Choose a option"%1
if errorlevel ==2 GOTO LOAD_PROGRAM
if errorlevel ==1 GOTO saveENC

:saveENC
cls
echo %X01%
echo %X02%
echo %X03%
echo %VER%
echo %X01%
echo.
echo.
set /p =%encryptResult%<nul >%USERPROFILE%\Desktop\yourEncryption.txt
echo Done!
timeout /t 2 >nul
GOTO LOAD_PROGRAM


:decrypt
cls
echo %X01%
echo %X02%
echo %X03%
echo %VER%
echo %X01%
echo.
echo.
echo Enter or paste your text/password:
set /p decryptPending=
set /p =%decryptPending%<nul >scripts/userInputPending.noid
echo Waiting for decryption return...
start /wait scripts\decrypt.exe
set /p decryptResult=<scripts/decryptResult.noid
cls
echo %X01%
echo %X02%
echo %X03%
echo %VER%
echo %X01%
echo.
echo.
echo Encryption done.
echo Result = %decryptResult%
echo.
echo.
echo Do you want a Text File on your Desktop of this result?
echo.
echo.
echo 1: Yes
echo 2: No


choice /n /c:123 /m "Choose a option"%1
if errorlevel ==2 GOTO LOAD_PROGRAM
if errorlevel ==1 GOTO saveDCC

:saveDCC
cls
echo %X01%
echo %X02%
echo %X03%
echo %VER%
echo %X01%
echo.
echo.
set /p =%decryptResult%<nul >%USERPROFILE%\Desktop\yourDecryption.txt
echo Done!
timeout /t 2 >nul
GOTO LOAD_PROGRAM



pause

:HPERFORMANCE_SET
cls
echo %X01%
echo %X02%
echo %X03%
echo %VER%
echo %X01%
echo.
echo.



start /min scripts/audioScript_cnfm.vbs

%KILLOBS%

cls
echo %X01%
echo %X02%
echo %X03%
echo %VER%
echo %X01%
echo.
echo.

set /p hpValueGUIDresult=<cache/hpValueGUID.noid

C:\Windows\System32\powercfg.exe /setactive %hpValueGUIDresult%
set /p ="b7cd3ecb2790"<nul >cache/userSet.noid



echo Your CPU is now set on HIGH PERFORMANCE!
timeout 3
GOTO END

:SILENT_SET
cls
echo %X01%
echo %X02%
echo %X03%
echo %VER%
echo %X01%
echo.
echo.


start /min scripts/audioScript_cnfm.vbs



cls
echo %X01%
echo %X02%
echo %X03%
echo %VER%
echo %X01%
echo.
echo.


set /p svValueGUIDresult=<cache/svValueGUID.noid

C:\Windows\System32\powercfg.exe /setactive %svValueGUIDresult%
set /p ="f71556f20b4a"<nul >cache/userSet.noid


echo Your CPU is now set on POWER SAVING!
timeout 3
GOTO END



:MONITOR_OFF
cls
echo %X01%
echo %X02%
echo %X03%
echo %VER%
echo %X01%
echo.
echo.

:CHECKIF_processExist

tasklist | findstr /i "sss.exe" > nul && echo SuperSleep is running! || GOTO BOOT_SSS


start /min scripts/audioScript_cnfm.vbs



cls
echo %X01%
echo %X02%
echo %X03%
echo %VER%
echo %X01%
echo.
echo.


set /p svValueGUIDresult=<cache/svValueGUID.noid

C:\Windows\System32\powercfg.exe /setactive %svValueGUIDresult%
set /p ="f71556f20b4a"<nul >cache/userSet.noid


echo Your CPU is now set on SILENT!
echo Monitor will close...
timeout 3
start /min scripts/sendKey.vbs
GOTO END

:BOOT_SSS
start ins/sss.exe
echo Starting SuperSleep...
timeout 3
GOTO MONITOR_OFF



:SYINFO
cls
echo %X01%
echo %X02%
echo %X03%
echo %VER%
echo %X01%
echo.
echo.
systeminfo > %USERPROFILE%\Desktop\administry-SystemInfo.txt
echo. Done! A text file was created on your desktop.
echo. Press any key to return...
pause >nul
GOTO begin

:EXP_SHUTDOWN
cls
echo %X01%
echo %X02%
echo %X03%
echo %VER%
echo %X01%
echo.
echo.
taskkill /f /im explorer.exe
echo Done! Restarting...please wait!
timeout /t 3 >nul
start explorer.exe
echo.
echo.
echo Restarting explorer completed! Press a key to return at the main menu!
PAUSE >nul
GOTO begin

:IPCONFIG
cls
echo %X01%
echo %X02%
echo %X03%
echo %VER%
echo %X01%
echo.
echo.
ipconfig
pause
GOTO begin

:REFRESH_MENU
cls
echo %X01%
echo %X02%
echo %X03%
echo %VER%
echo %X01%
echo.
echo.
echo This tool can Refresh your Monitor or your Graphic Card Driver. USE AT YOUR OWN RISK!
echo.
echo.
echo 1: Refresh Monitor
echo 2: Refresh Graphic Card
echo.
echo 3: Return
choice /n /c:123 /m "Choose a option"%1
if errorlevel ==3 GOTO ADMIN_TOOLS
if errorlevel ==2 GOTO 
if errorlevel ==1 GOTO SCREEN_REFRESH

:SCREEN_REFRESH
cls
echo %X01%
echo %X02%
echo %X03%
echo %VER%
echo %X01%
echo.
echo.
echo Refresh screen started...
tasklist | findstr /i "sss.exe" > nul && echo SuperSleep is running... || GOTO BOOT_SSS_forSCRN
:EXECUTE_REFRESH
echo TEST DONE
wait
GOTO REFRESH_MENU



:BOOT_SSS_forSCRN
start ins/sss.exe
echo Starting SuperSleep...
timeout 3
GOTO SCREEN_REFRESH


:UKNW_COMMAND
echo.
echo.
echo Unknown command...
timeout 3
GOTO begin

:UKNW_COMMAND_MOREOPTION
echo.
echo.
echo Unknown command...
timeout 3 
GOTO MOPTS

:UKNW_COMMAND_ADMINTOOLS
echo.
echo.
echo Unknown command...
timeout 3 
GOTO ADMIN_TOOLS

:UKNW_COMMAND_SETTINGS
echo.
echo.
echo Unknown command...
timeout 3 
GOTO SETTINGS



:COLORHUD
cls
echo %X01%
echo %X02%
echo %X03%
echo %VER%
echo %X01%
echo.
echo.

if not exist "cache/HUD.noid" (
set /p ="DEFAULT"<nul >cache/HUD.noid
echo. HUD Cache created!
) 
echo.
echo.

echo 1: BLUE
echo 2: AQUA
echo 3: DEFAULT (LIGHT GREEN)
echo 4: RED
echo 5: BLUELIGHT


choice /n /c:12345 /m "Choose a new color!"%1

if errorlevel ==5 GOTO BL_SET
if errorlevel ==4 GOTO RED_SET
if errorlevel ==3 GOTO DEFAULT_SET
if errorlevel ==2 GOTO AQUA_SET
if errorlevel ==1 GOTO BLUE_SET

pause

:COLOR_CACHESET
:BLUE_SET
cls
echo %X01%
echo %X02%
echo %X03%
echo %VER%
echo %X01%
echo.
echo.
color 1
set /p ="BLUE"<nul >cache/HUD.noid
echo. Done!
pause
GOTO LOAD_PROGRAM

:AQUA_SET
cls
echo %X01%
echo %X02%
echo %X03%
echo %VER%
echo %X01%
echo.
echo.
color 3
set /p ="AQUA"<nul >cache/HUD.noid
echo. Done!
pause
GOTO LOAD_PROGRAM
:DEFAULT_SET
cls
echo %X01%
echo %X02%
echo %X03%
echo %VER%
echo %X01%
echo.
echo.
color A
set /p ="DEFAULT"<nul >cache/HUD.noid
echo. Done!
pause
GOTO LOAD_PROGRAM
:RED_SET
cls
echo %X01%
echo %X02%
echo %X03%
echo %VER%
echo %X01%
echo.
echo.
color 4
set /p ="RED"<nul >cache/HUD.noid
echo. Done!
pause
GOTO LOAD_PROGRAM
:BL_SET
cls
echo %X01%
echo %X02%
echo %X03%
echo %VER%
echo %X01%
echo.
echo.
color 3f
set /p ="BL"<nul >cache/HUD.noid
echo. Done!
pause
GOTO LOAD_PROGRAM




: */*/*/*/*/CONFIG*/*/*/*/*/

:POW_CONFIG_SELECT
cls
echo.
echo.
echo Do you want to let Administry config your Power Scheme 
echo or do you want to do it yourself?
echo.
echo.
echo 1 = Automatically
echo 2 = Manually

choice /n /c:12 /m "Choose a option"%1
if errorlevel ==2 GOTO POWERGUID_CONFIG
if errorlevel ==1 GOTO POW_AUTOCFG

:POW_AUTOCFG
cls
echo.
echo.
echo Please Wait...
start /wait %UserProfile%\AppData\Roaming\Administry\powSys\ps_init.exe
echo Done!
timeout /t 1 >nul
echo Writing GUID...
set /p ="a8ff579c-aed1-49c0-a69c-fc5b5f2d968a"<nul >hpviTemp.noid
set /p ="3c857587-cf01-4c11-8da8-0f43f3c2ad98"<nul >sviTemp.noid
echo Configuration complete!
timeout /t 3 >nul
GOTO SPLASHBOOT

:POWERGUID_CONFIG
cls
echo.
echo.
echo This is the list of your current Power Scheme:
echo.
echo.
powercfg /l
echo.
echo.
echo Copy the 48 caracters of your Power Schemes choice for the following:
echo.
echo High performance/Gaming mode?
set /p highPerformanceValueInput=
set /p ="%highPerformanceValueInput%"<nul >hpviTemp.noid
echo Ok
echo.
echo Silent mode?
set /p silentValueInput=
set /p ="%silentValueInput%"<nul >sviTemp.noid
echo Ok
timeout /t 1 >nul
cls
echo Configuration complete!
timeout /t 3 >nul
GOTO SPLASHBOOT

pause


:SET_SPLASHBOOT_CONFIG
cls
echo %X01%
echo %X02%
echo %X03%
echo %VER%
echo %X01%
echo.
echo.
echo Show the Administry Logo at each boot?
echo.
echo.
echo 1 = Yes
echo 2 = No
choice /n /c:1234 /m "Waiting user input..."%1

if errorlevel ==2 GOTO SSBC_2
if errorlevel ==1 GOTO SSBC_1

:SSBC_1

set /p ="F87AHN"<nul >cache\ssbcInit.noid
echo Done!
timeout /t 2 >nul
GOTO LOAD_PROGRAM
:SSBC_2

set /p ="PXC28S"<nul >cache\ssbcInit.noid
echo Done!
timeout /t 2 >nul
GOTO LOAD_PROGRAM


:RESET_CFG
cls
echo %X01%
echo %X02%
echo %X03%
echo %VER%
echo %X01%
echo.
echo.
echo Do you want to reset Administry?
echo.
echo. *WARNING! THIS WILL INCLUDE ALL CONFIG FILES...* 
echo.
echo.
echo 1 = Yes
echo 2 = No
choice /n /c:12 /m "Waiting user input..."%1

if errorlevel ==2 GOTO SETTINGS
if errorlevel ==1 GOTO RESET_PROCEED

:RESET_PROCEED
cls
echo %X01%
echo %X02%
echo %X03%
echo %VER%
echo %X01%
echo.
echo.
echo Deleting powers schemes...
start /wait %UserProfile%\AppData\Roaming\Administry\powSys\ps_rem.exe
timeout /t 1 >nul
echo Deleting caches files...
del /Q cache
timeout /t 1 >nul
@RD /Q cache
echo Deleting stream files...
del /Q stream
timeout /t 1 >nul
@RD /Q stream
echo Removing registry key...
set /p ="G423FGF45GC2RG4F4DFGS546D4G23DGB56FGIFGJH687H8G7"<nul >scripts\firstbootKey.noid
timeout /t 1 >nul
echo DONE!
start /min scripts/err_F12C.vbs
exit

:TIMEWAIT_DEFAULT
cls
echo %X01%
echo %X02%
echo %X03%
echo %VER%
echo %X01%
echo.
echo.
:SET_AUTOCLOSE
cls
echo %X01%
echo %X02%
echo %X03%
echo %VER%
echo %X01%
echo.
echo.
echo Close automatically Administry after power profile selection?
echo.
echo.
echo 1 = Yes
echo 2 = No
choice /n /c:1234 /m "Waiting user input..."%1

if errorlevel ==2 GOTO AUTOC_UNSET
if errorlevel ==1 GOTO AUTOC_SET

:AUTOC_SET
set /p ="01"<nul >cache\autoc_s.noid
echo Done!
timeout /t 2 >nul
GOTO LOAD_PROGRAM


:AUTOC_UNSET
set /p ="00"<nul >cache\autoc_s.noid
echo Done!
timeout /t 2 >nul
GOTO LOAD_PROGRAM


:KILL
GOTO END

:ERROR_X01D
start /min scripts/err_X01D.vbs
exit
:ERROR_KILL
echo ERROR
pause

pause



