from django.conf import settings
import os


def handle_uploaded_file(file):
    folder = f'{settings.MEDIA_ROOT}'
    if not os.path.exists(folder):
        os.makedirs(folder)
    with open(f'{folder}/{file.name}', 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)

    return f'{folder}/{file.name}'