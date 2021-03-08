from PIL import Image

file_path = "input/0001-01.jpeg"

# Orientation タグ値にしたがった処理
# PIL における Rotate の角度は反時計回りが正
convert_image = {
    1: lambda img: img,
    2: lambda img: img.transpose(Image.FLIP_LEFT_RIGHT),                              # 左右反転
    3: lambda img: img.transpose(Image.ROTATE_180),                                   # 180度回転
    4: lambda img: img.transpose(Image.FLIP_TOP_BOTTOM),                              # 上下反転
    5: lambda img: img.transpose(Image.FLIP_LEFT_RIGHT).transpose(Pillow.ROTATE_90),  # 左右反転＆反時計回りに90度回転
    6: lambda img: img.transpose(Image.ROTATE_270),                                   # 反時計回りに270度回転
    7: lambda img: img.transpose(Image.FLIP_LEFT_RIGHT).transpose(Pillow.ROTATE_270), # 左右反転＆反時計回りに270度回転
    8: lambda img: img.transpose(Image.ROTATE_90),                                    # 反時計回りに90度回転
}

img = Image.open(file_path)
exif = img._getexif()
orientation = exif.get(0x112, 1)

new_img = convert_image[orientation](img)

new_img.save(file_path.replace("input/", "output/"))