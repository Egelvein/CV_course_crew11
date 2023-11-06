from celery import shared_task
from .utils import draw_counters
import requests
import json


@shared_task
def detect_problem(upload_path, result_path):
    files = {'file': open(upload_path, 'rb')}

    r = requests.post("http://127.0.0.1:8000/file/", files=files)
    data = r.json()["results"]
    draw_counters(upload_path, data)
    return result_path
