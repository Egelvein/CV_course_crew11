from enum import Enum
from typing import Optional, Tuple

import cv2
import numpy as np


class Contour:
    """
    >>> Contour(bounding_rect=(1, 2, 3, 4)).x_min
    1
    >>> Contour(bounding_rect=(1, 2, 3, 4)).x_max
    4
    >>> Contour(bounding_rect=(1, 2, 3, 4)).y_min
    2
    >>> Contour(bounding_rect=(1, 2, 3, 4)).y_max
    6
    """

    def __init__(self,
                 contour: Optional[np.ndarray] = None,
                 bounding_rect: Optional[Tuple[int, int, int, int]] = None,
                 ):
        """
        :param contour: OpenCV-like contour with many points
        :param bounding_rect: tuple with four elements: x, y, width, height
        """
        if contour is None:
            if not len(bounding_rect) or any(isinstance(x, float) for x in bounding_rect):
                raise ValueError(f'bounding_rect is not correct. Got = {bounding_rect}')
            else:
                self._bounding_rect = bounding_rect
        else:
            self._bounding_rect = None
        self._contour = contour
        self._x_min = None
        self._y_min = None
        self._x_max = None
        self._y_max = None

    @property
    def x_min(self) -> float:
        if self._x_min is None:
            self._x_min = self._bounding_rect[0]
        return float(self._x_min)

    @property
    def y_min(self) -> float:
        if self._y_min is None:
            self._y_min = self._bounding_rect[1]
        return float(self._y_min)

    @property
    def x_max(self) -> float:
        if self._x_max is None:
            self._x_max = self._bounding_rect[2]
        return float(self._x_max)

    @property
    def y_max(self) -> float:
        if self._y_max is None:
            self._y_max = self._bounding_rect[3]
        return float(self._y_max)

    @property
    def xyxy(self) -> list:
        return [self.x_min, self.y_min, self.x_max, self.y_max]
