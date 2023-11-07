import base64
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.conf import settings
from .forms import ImageForm
from .utils import handle_uploaded_file
from .tasks import detect_problem, test
from .models import Chip


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

        chip = Chip()
        chip.save()

        upload_path = handle_uploaded_file(uploaded_file, chip)

        task = detect_problem.delay(chip.id)

        # return JsonResponse({'Json': str(task)})
        return redirect("result", chip.id)


def result(request, chip_id):
    chip = Chip.objects.get(pk=chip_id)
    status = chip.status

    result_path = chip.result_path

    return render(request, 'results.html', context={
        "status": status,
        "result_path": result_path,
        "preds": [
            {'contour': [301.8711242675781, 377.7820129394531, 318.38507080078125, 402.55255126953125],
             'probability': 0.8628689050674438, 'class': 'mouse_bite'},
            {'contour': [301.8711242675781, 377.7820129394531, 318.38507080078125, 402.55255126953125],
             'probability': 0.8628689050674438, 'class': 'mouse_bite'},
        ],
    })