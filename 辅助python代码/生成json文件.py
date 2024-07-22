import os
import hashlib
import json


# 函数：计算文件的 SHA-256 哈希值
def calculate_sha256(file_path):
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()


# 主目录路径，这里假设所有的模型文件都在同一个目录下
# main_directory = "D:\\Laboratory\\dataset\\r1.0.1\\reconstruction"
main_directory = 'D:\\Laboratory\\catiadataset'

# 获取主目录下的所有文件
# 获取主目录下的所有 .obj 文件
file_list = [os.path.join(main_directory, f) for f in os.listdir(main_directory) if f.endswith('.obj') and os.path.isfile(os.path.join(main_directory, f))]


# 初始化一个空列表，用来存储每个文件的信息
models_info = []

# 遍历文件列表，为每个文件计算哈希值，并生成信息字典
for file_path in file_list:
    # 计算文件的 SHA-256 哈希值
    sha256_hash = calculate_sha256(file_path)

    # 生成文件的下载链接（假设上传到 GitHub 后的地址）
    # 这里假设 GitHub 仓库的地址是 https://github.com/your-username/your-repo
    file_name = os.path.basename(file_path)
    file_identifier = f"https://github.com/Gardenia33/obj_for_blender/blob/main/{file_name}"
    # file_identifier = f"https://github.com/Gardenia33/dataset/blob/master/{file_name}"

    # 将文件信息字典添加到列表中
    models_info.append({
        "sha256": sha256_hash,
        "fileIdentifier": file_identifier,
        "source": "github"
    })


# 将模型信息列表保存为 JSON 文件
json_file_path = "D:\\PycharmProject\\python_for_blender\\objaverse_blender\\models_info_42_catia_obj.json"
with open(json_file_path, "w") as json_file:
    json.dump(models_info, json_file, indent=4)

print(f"已生成 JSON 文件：{json_file_path}")
