import os
from PIL import Image

source_folder = 'test_frames'
output_folder = 'gif'

# 检查 output 文件夹是否存在，如果不存在则创建
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 遍历 source 文件夹下的子文件夹
for folder_name in os.listdir(source_folder):
    folder_path = os.path.join(source_folder, folder_name)

    # 检查是否为文件夹
    if os.path.isdir(folder_path):
        output_folder_path = os.path.join(output_folder, folder_name)

        # 检查 output 文件夹下对应的同名文件夹是否存在，如果不存在则创建
        if not os.path.exists(output_folder_path):
            os.makedirs(output_folder_path)

        # 获取文件夹中的图片文件列表
        image_files = [f for f in os.listdir(folder_path) if f.endswith('.jpg') or f.endswith('.png')]

        # 将图片按文件名排序
        image_files.sort()

        # 创建一个图像列表，用于存储每个图片
        images = []

        # 遍历文件夹中的图片文件
        for image_file in image_files:
            image_path = os.path.join(folder_path, image_file)

            # 打开图片文件并添加到图像列表中
            image = Image.open(image_path)
            images.append(image)

        # 指定输出文件路径和文件名
        output_file_path = os.path.join(output_folder_path, f'{folder_name}.gif')

        # 将图像列表保存为 GIF 文件
        images[0].save(output_file_path, save_all=True, append_images=images[1:], loop=0, duration=200)

        print(f'已生成 GIF 文件：{output_file_path}')