from pathlib import Path

triton_repo_path = Path('tmp') / 'triton_repo'
triton_model_path = triton_repo_path / 'yolo'

(triton_model_path / '1').mkdir(parents=True, exist_ok=True)

# Path("yolov8n.onnx").rename(triton_model_path / '1' / 'model.onnx')


(triton_model_path / 'config.pdtxt').touch()