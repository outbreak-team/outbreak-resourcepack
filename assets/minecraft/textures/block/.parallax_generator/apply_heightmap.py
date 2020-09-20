import sys
import os
from PIL import Image
import traceback

# В скрипт через первый аргумент (drag&drop файла на скрипт в Windows)
# передаётся путь к файлу с _n в названии. Скрипт ищет файл с похожим
# названием, но оканчивающийся на _h. Файл, оканчивающийся на _h должен
# быть чёрно-белой картой высот.
# Скрипт делает картинке с _n в названии прозрачность в соответствии
# с картой высот.


def apply_heightmap(nm_path: str, hm_path: str):
    new_data = []

    nm_img = Image.open(nm_path)
    hm_img = Image.open(hm_path)

    nm_img = nm_img.convert("RGBA")
    # hm_img = hm_img.convert("RGBA")

    nm_data = nm_img.getdata()
    hm_data = list(hm_img.getdata())

    # print(hm_data)

    for num, px in enumerate(list(nm_data)):
        px = list(px)
        hm_px = hm_data[num]
        # print(hm_avg)
        # print(hm_px)
        avg = int((hm_px[0]+hm_px[1]+hm_px[2])/3)

        px = [px[0], px[1], px[2], avg]
        new_data.append(tuple(px))

    nm_img.putdata(new_data)

    nm_img.save(nm_path)


try:
    apply_heightmap(
        input("Normal map > "),
        input("Height map > ")
    )
except Exception as e:
    traceback.print_exc()
    input()