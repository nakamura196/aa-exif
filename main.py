from PIL import Image
import argparse    # 1. argparseをインポート
import glob
import os

parser = argparse.ArgumentParser()    # 2. パーサを作る

# 3. parser.add_argumentで受け取る引数を追加していく
parser.add_argument('path', help='入力フォルダへのパス')    # 必須の引数を追加

args = parser.parse_args()    # 4. 引数を解析

files = []

suffixes = ["JPG", "png"]

for suffix in suffixes:
    files.extend(glob.glob(args.path+"/**/*.{}".format(suffix), recursive=True))

    

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

for file in files:

    img = Image.open(file)
    exif = img._getexif()

    if exif:

        orientation = exif.get(0x112, 1)

        new_img = convert_image[orientation](img)

    else:
        new_img = img

    output_path = file.replace("input/", "output/")
    dir_path = os.path.dirname(output_path)
    os.makedirs(dir_path, exist_ok=True)

    new_img.save(output_path)