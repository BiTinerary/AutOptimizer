@ECHO OFF
SET choc=chocolatey install -y
@powershell -NoProfile -ExecutionPolicy unrestricted -Command "iex ((new-object net.webclient).DownloadString('https://chocolatey.org/install.ps1'))" && SET PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin
chocolatey update
%choc% sublime
%choc% classic-shell
%choc% firefox
%choc% adblockplusfirefox
%choc% googlechrome
%choc% adblockpluschrome
%choc% 7zip.install
%choc% githubforwindows
%choc% python -version 2.7.6 
%choc% imgburn
%choc% ccleaner
%choc% httrack
%choc% python
%choc% pip
%choc% virtualbox
%choc% virtualbox.extensionpack
%choc% rmprepusb
%choc% synergy
%choc% teamviewer
%choc% cameyo
%choc% revo.uninstaller
%choc% wim2vhd
%choc% gimp
%choc% vlc
%choc% putty
chocolatey update all

:: Set Path variable equal to existing path variables plus standard python directories
setx PATH "%PATH%;C:\Windows\System32;C:\Windows\System32\WindowsPowerShell\v1.0;C:\Python27;C:\Python27\Lib;C:\Python27\DLLs;C:\Python27\Scripts;C:\Python27\Lib\site-packages;C:\Python27\Lib\lib-tk" /m

:: Add Python Path variables to existing envars
setx PYTHON_PATH "C:\Python27;C:\Python27\Lib;C:\Python27\DLLs;C:\Python27\Scripts;C:\Python27\Lib\site-packages;C:\Python27\Lib\lib-tk" /m

cd %CD%
PythonLibs.bat