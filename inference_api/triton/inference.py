import contextlib
import subprocess
import time
from config import triton_repo_path, triton_model_path
from tritonclient.http import InferenceServerClient
from ultralytics import YOLO


tag = 'nvcr.io/nvidia/tritonserver:23.09-py3'  # 6.4 GB

# subprocess.call(f'docker pull {tag}', shell=True)

container_id = subprocess.check_output(
    f'docker run -d --rm -v {triton_repo_path}:/models -p 8000:8000 {tag} tritonserver --model-repository=/models',
    shell=True).decode('utf-8').strip()

triton_client = InferenceServerClient(url='localhost:8000', verbose=False, ssl=False)

for _ in range(10):
    with contextlib.suppress(Exception):
        assert triton_client.is_model_ready("yolov8n")
        break
    time.sleep(1)


model = YOLO(f'http://localhost:8000/yolo', task='detect')

