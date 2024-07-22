import os
import subprocess

# 配置 GitHub 仓库 URL 和本地目录
github_repo_url = 'https://github.com/Gardenia33/test_for_blender_objaverse.git'
local_directory = 'D:\\Laboratory\\dataset\\r1.0.1'

# 切换到指定的本地目录
os.chdir(local_directory)

# 初始化 git 仓库
subprocess.run(['git', 'init'])

# 添加所有 .obj 文件
subprocess.run(['git', 'add', '*.obj'])

# 提交更改
commit_message = 'Add .obj model files'
subprocess.run(['git', 'commit', '-m', commit_message])

# 连接到远程 GitHub 仓库
subprocess.run(['git', 'remote', 'add', 'origin', github_repo_url])

# 推送到 GitHub
subprocess.run(['git', 'push', '-u', 'origin', 'main'])
