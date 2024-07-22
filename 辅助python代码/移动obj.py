import os
import random
import shutil

# 源文件夹和目标文件夹路径
# source_folder = 'D:\\Laboratory\\dataset\\r1.0.1\\r1.0.1\\reconstruction'
source_folder = 'D:\\Laboratory\\dataset\\r1.0.1\\reconstruction'  # 新添加的路径
target_folder = 'D:\\Laboratory\\dataset\\r1.0.1\\reconstruction\\random_50'

# 如果目标文件夹不存在，创建它
if not os.path.exists(target_folder):
    os.makedirs(target_folder)

# 获取源文件夹中所有的OBJ模型文件列表，并按名称排序
obj_files = [f for f in os.listdir(source_folder) if f.endswith('.obj')]
# obj_files.sort()

# 将文件列表随机排序
random.shuffle(obj_files)

# 确保不超过n个文件
num_to_move = min(50, len(obj_files))

# 移动选定的文件到目标文件夹
for i in range(num_to_move):
    file_name = obj_files[i]
    source_file = os.path.join(source_folder, file_name)
    target_file = os.path.join(target_folder, file_name)
    shutil.move(source_file, target_file)
    print(f'Moved {file_name} to {target_folder}')

print(f'\nSuccessfully moved {num_to_move} OBJ files.')