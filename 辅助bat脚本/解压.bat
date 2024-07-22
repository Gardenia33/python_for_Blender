@echo off
setlocal

set "target_dir=D:\Laboratory\dataset\linux_blender_\catia_obj_31"

:: Ensure 7-Zip path is in system PATH or set it explicitly
set "zip_exe=C:\Users\Gardenia\AppData\Local\Microsoft\WindowsApps\7z.exe"

:: Loop through all files in the target directory
for %%F in ("%target_dir%\*.*") do (
    echo Processing: %%F
    if /i "%%~xF"==".zip" (
        "%zip_exe%" x "%%F" -o"%%~dpF"
    ) else if /i "%%~xF"==".rar" (
        "%zip_exe%" x "%%F" -o"%%~dpF"
    ) else if /i "%%~xF"==".7z" (
        "%zip_exe%" x "%%F" -o"%%~dpF"
    ) else (
        echo Unsupported format: %%F
    )
)

echo Done.
pause
