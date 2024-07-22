# python_for_Blender
Blender渲染3D模型多视角图像python脚本，在渲染图片数量不变时，固定渲染角度。
参考源代码：Objaverse-XL Rendering Script

渲染代码需要在Linux系统中运行

Set up for this scripts：
1 克隆代码

```
git clone https://github.com/Gardenia33/python_for_Blender.git 
cd rendering
```

2 下载对应版本的Blender：

```
wget https://download.blender.org/release/Blender3.2/blender-3.2.2-linux-x64.tar.xz && \
  tar -xf blender-3.2.2-linux-x64.tar.xz && \
  rm blender-3.2.2-linux-x64.tar.xz
```

3 安装Python依赖，Python版本需要大于3.8

```
cd ../.. && \
  pip install -r requirements.txt && \
  pip install -e . && \
  cd rendering
```

4  使用示例

```
python3 main.py --num_renders 8
```

num_renders 可以根据所需渲染图片数量自行更改