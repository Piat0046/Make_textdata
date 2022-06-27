# -*- coding: utf-8 -*-
import os
from tqdm import tqdm

img_dir = r"F:\News_ocr\dataset\train\1"
aug_dir = r""
txt_file_path = r"F:\News_ocr\dataset\train\1\labels.txt"
new_txt_file_path = r"F:\News_ocr\dataset\train\1\train.txt"

write_file = open(new_txt_file_path, 'w', encoding='utf-8')
read_file = open(txt_file_path, 'r', encoding='utf-8')

for line in tqdm(read_file.readlines()):
    info = line.split(' ')
    if 'aug' in info[0]:
        data = os.path.join(aug_dir, os.path.basename(info[0])) + '\t' + ' '.join(info[1:])
    else:
        data = os.path.join(img_dir, os.path.basename(info[0])) + '\t' + ' '.join(info[1:])
    write_file.write(data)

write_file.close()