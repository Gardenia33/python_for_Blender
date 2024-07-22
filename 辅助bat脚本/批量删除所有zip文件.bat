@echo off
setlocal
set "target_dir=D:\Laboratory\dataset\linux_blender_"
set "file_extension=*.zip"

:: Call the recursive function
call :delete_files "%target_dir%"

endlocal
echo Done.
goto :eof

:delete_files
set "current_dir=%~1"
pushd "%current_dir%" || exit /b

:: Delete files with the specified extension
del /q "%file_extension%"

:: Recursively process each subdirectory
for /d %%D in (*) do (
    call :delete_files "%%D"
)

popd
exit /b
