import zipfile
import os
import random
import shutil

classes = ['missing_hole', 'mouse_bite', 'open_circuit',
           'short', 'spur', 'spurious copper']

train_percent = 0.8
validation_percent = 0.15
test_percent = 0.05

# Archive unpack
unzip_dir = 'VOC_PCB'

if not os.path.exists(unzip_dir):
    path_to = 'VOC_PCB.zip'
    with zipfile.ZipFile(path_to, 'r') as zip_ref:
        zip_ref.extractall()

# Data group
new_dir = 'Good_dataset'

if not os.path.exists(new_dir):
    os.mkdir(new_dir)
    os.mkdir(new_dir + '/train')
    os.mkdir(new_dir + '/validation')
    os.mkdir(new_dir + '/test')

photo_dir = unzip_dir + '/JPEGImages'
for filename in os.listdir(photo_dir):
    class_dir = None
    for class_name in classes:
        if class_name in filename:
            class_dir = class_name
            break

    if class_dir is None:
        class_dir = 'other'

    rand_num = random.random()

    if rand_num < train_percent:
        target_dir = os.path.join(new_dir, 'train', class_dir)
    elif rand_num < train_percent + validation_percent:
        target_dir = os.path.join(new_dir, 'validation', class_dir)
    else:
        target_dir = os.path.join(new_dir, 'test', class_dir)

    os.makedirs(target_dir, exist_ok=True)
    source_path = os.path.join(photo_dir, filename)

    if os.path.exists(source_path):
        target_path = os.path.join(target_dir, filename)
        shutil.move(source_path, target_path)
    else:
        print(f"File is not real: {source_path}")
