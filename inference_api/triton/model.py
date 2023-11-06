from ultralytics import YOLO

# Load a model

# Export the model
# onnx_file = model.export(format='onnx', dynamic=True)


def init_model():
    model = YOLO('best.pt')
    return model
