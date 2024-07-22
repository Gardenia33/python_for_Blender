@echo off
setlocal enabledelayedexpansion

REM 定义源文件夹和目标文件夹
set source_folder=D:\Laboratory\catiadataset\liyumo
set target_folder=D:\Laboratory\catiadataset

REM 检查目标文件夹是否存在，如果不存在则创建
if not exist "%target_folder%" (
    mkdir "%target_folder%"
)

REM 初始化计数器
set count=32

REM 遍历源文件夹中的所有.obj文件
for %%f in ("%source_folder%\*.obj") do (
    REM 生成新的文件名
    set new_name=objfile_!count!.obj
    
    REM 复制文件并重命名
    copy "%%f" "%target_folder%\!new_name!"
    
    REM 递增计数器
    set /a count+=1
)

echo 所有文件已复制并重命名。
pause
