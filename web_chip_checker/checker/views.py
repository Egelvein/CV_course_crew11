import base64
from django.http import JsonResponse
from django.shortcuts import render
from django.conf import settings
from .forms import ImageForm
from .utils import handle_uploaded_file


def main_camera(request):
    form = ImageForm()

    context = {
        'form': form,
        'data': None,
    }

    if request.method == 'GET':
        return render(request, "index.html", context)

    elif request.method == 'POST' and request.FILES['file']:
        uploaded_file = request.FILES['file']

        extension = uploaded_file.name.split(".")[-1]
        if extension not in ['jpag', 'jpg', 'png']:
            context['success'] = False
            context['error'] = "File should be an image"
            return render(request, 'index.html', context)

        upload_path = handle_uploaded_file(uploaded_file)

        # model inference here

        return JsonResponse({'Json': uploaded_file.name})
