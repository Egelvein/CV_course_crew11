import zipfile
import os
import random
import shutil

train_percent = 0.8

# Archive unpack
unzip_dir = 'VOC_PCB'

if not os.path.exists(unzip_dir):
    path_to = '../VOC_PCB.zip'
    with zipfile.ZipFile(path_to, 'r') as zip_ref:
        zip_ref.extractall()

# Data group
new_dir = 'Dataset_for_YOLO'

if not os.path.exists(new_dir):
    os.mkdir(new_dir)
    os.mkdir(os.path.join(new_dir, 'train'))
    os.mkdir(os.path.join(new_dir, 'val'))
    os.mkdir(os.path.join(new_dir, 'train', 'images'))
    os.mkdir(os.path.join(new_dir, 'train', 'labels'))
    os.mkdir(os.path.join(new_dir, 'val', 'images'))
    os.mkdir(os.path.join(new_dir, 'val', 'labels'))

photo_dir = unzip_dir + '/JPEGImages'
annotation_dir = '../Labels'

for filename in os.listdir(photo_dir):
    rand_num = random.random()

    if rand_num < train_percent:
        target_dir = os.path.join(new_dir, 'train', 'images')
        annotation_target_dir = os.path.join(new_dir, 'train', 'labels')
    else:
        target_dir = os.path.join(new_dir, 'val', 'images')
        annotation_target_dir = os.path.join(new_dir, 'val', 'labels')

    os.makedirs(target_dir, exist_ok=True)
    source_path = os.path.join(photo_dir, filename)

    if os.path.exists(source_path):
        target_path = os.path.join(target_dir, filename)
        shutil.move(source_path, target_path)

        annotation_file = os.path.splitext(filename)[0] + '.txt'
        annotation_source_path = os.path.join(annotation_dir, annotation_file)
        annotation_target_path = os.path.join(annotation_target_dir, annotation_file)

        if os.path.exists(annotation_source_path):
            shutil.move(annotation_source_path, annotation_target_path)
        else:
            print(f"Annotation file not found: {annotation_source_path}")
    else:
        print(f"File is not real: {source_path}")
