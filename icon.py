from PIL import Image

def resize_and_paste_watermark(main_image_path, watermark_image_path, output_image_path):
    # 打开主图像并调整大小到128x128
    main_img = Image.open(main_image_path)
    main_img = main_img.resize((64, 64), Image.LANCZOS)  # ANTIALIAS模式会报错

    # 打开水印图像
    watermark_img = Image.open(watermark_image_path)

    # 计算水印的位置（右下角）
    position = (main_img.width - watermark_img.width, main_img.height - watermark_img.height)

    # 确保主图像和水印图像具有相同的模式（例如RGBA）
    if main_img.mode != 'RGBA':
        main_img = main_img.convert('RGBA')
    if watermark_img.mode != 'RGBA':
        watermark_img = watermark_img.convert('RGBA')

    # 创建一个透明的图层作为新的背景
    new_img = Image.new('RGBA', main_img.size, (0, 0, 0, 0))
    new_img.paste(main_img, (0, 0))

    # 将水印贴到新图层上
    new_img.paste(watermark_img, position, mask=watermark_img)

    # 保存结果图像
    new_img.save(output_image_path, format='PNG')

# 调用函数，传入你的文件路径
resize_and_paste_watermark('icon.png', 'forbidden.png', 'output.png')