from django.conf import settings
import cv2
import os


def handle_uploaded_file(file):
    folder = f'{settings.MEDIA_ROOT}/uploads'
    if not os.path.exists(folder):
        os.makedirs(folder)
    with open(f'{folder}/{file.name}', 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)

    return f'{folder}/{file.name}'


def draw_counters(image_path, preds):
    img = cv2.imread(image_path)
    for pred in preds:
        contour = pred["contour"]
        img = cv2.rectangle(img, (int(contour[0]), int(contour[1])),
                            (int(contour[2]), int(contour[3])), (0, 255, 255), )

    cv2.imshow("Bounding Rectangle", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
