from abc import ABC, abstractmethod
from PIL import Image
from torchvision.transforms import functional as F
from typing import List
from dataclasses import dataclass, asdict
import logging
import numpy as np
from .contour import Contour
from ultralytics import YOLO


@dataclass
class DetectorPrediction:
    predicted_contour: Contour
    contour_probability: float
    contour_class: int

    dict = asdict
    names = {
        0: 'missing_hole',
        1: 'mouse_bite',
        2: 'open_circuit',
        3: 'short',
        4: 'spurious_copper',
        5: 'spur'
    }

    def dict(self):
        return {
            "contour": self.predicted_contour.xyxy,
            "probability": self.contour_probability,
            "class": self.names[int(self.contour_class)],
        }


class Detector(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def detect_contours(self, image: np.ndarray) -> List[DetectorPrediction]:
        """
        Return boxes of all detected contours from image.
        :param image: np.ndarray RGB image
        :return: List[Contour]
        """
        pass


class DummyDetector(Detector):

    def __init__(self, detection_model_path: str):
        logging.info('Loading Detector')
        self.model_path = detection_model_path

    def detect_contours(self, image: np.ndarray) -> List[DetectorPrediction]:
        dummy_contour = Contour(bounding_rect=(0, 0, 50, 50))
        prediction = DetectorPrediction(predicted_contour=dummy_contour, contour_probability=0.98)
        return [prediction]


class YoloV5Detector(DummyDetector):

    def __init__(self, detection_model_path: str):
        super().__init__(detection_model_path)
        self._load_model()

    def _load_model(self):
        self.model = YOLO(self.model_path)

    def detect_contours(self, img_path: str):
        predictions = []
        img = Image.open(img_path)
        results = self.model(img)
        for result in results:
            data = result.boxes.data[0]

            contour = Contour(bounding_rect=(data[0], data[1], data[2], data[3]))
            prediction = DetectorPrediction(contour, float(data[4]), int(data[-1]))
            predictions.append(prediction)

        return predictions

    def save_predictions(self, img_path: str, path: str):
        predictions = self.model(img_path)
        return predictions.save(filepath=path)
