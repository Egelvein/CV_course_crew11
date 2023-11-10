from celery import shared_task
from .utils import draw_counters
from .models import Chip
import requests
import os
import json


@shared_task
def detect_problem(chip_id):
    chip = Chip.objects.get(pk=chip_id)
    chip.status = "PROCESS"
    chip.save()

    upload_path = chip.original_path
    result_path = chip.result_path
    files = {'file': open(upload_path, 'rb')}

    api = os.getenv("API_URL")

    r = requests.post(f"http://{api}/file/", files=files)
    data = r.json()["results"]
    draw_counters(upload_path, result_path, data, chip_id)
    chip.status = "DONE"
    chip.save()

    return chip_id


@shared_task
def test():
    print("asdasdadsasdsa")
