from django.conf import settings
import cv2
import os


def handle_uploaded_file(file, chip):
    folder = f'{settings.MEDIA_ROOT}/uploads'
    if not os.path.exists(folder):
        os.makedirs(folder)
    with open(f'{folder}/{chip.id}.jpg', 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)

    return f'{folder}/{chip.id}.jpg'


def draw_counters(image_path, result_path, preds):
    img = cv2.imread(image_path)
    for pred in preds:
        contour = pred["contour"]
        img = cv2.rectangle(img, (int(contour[0]), int(contour[1])),
                            (int(contour[2]), int(contour[3])), (0, 255, 255), )

    cv2.imwrite(result_path, img)

    return result_path
