"""Gestión de la región de interés (ROI)."""
from typing import Optional
import pyautogui
from .config import ROI


class ROIManager:
    """Maneja la selección y captura de la región de interés."""
    def __init__(self):
        self.corner1: Optional[ROI] = None
        self.roi: Optional[ROI] = None

    def set_corner(self, x: int, y: int) -> None:
        if not self.corner1:
            self.corner1 = ROI(x, y, x, y)
        else:
            self.roi = ROI(self.corner1.x1, self.corner1.y1, x, y).normalized()
            self.corner1 = None

    def has_roi(self) -> bool:
        return self.roi is not None

    def screenshot(self):
        if not self.roi:
            raise RuntimeError("ROI no definida")
        return pyautogui.screenshot(region=(self.roi.x1, self.roi.y1,
                                            self.roi.width, self.roi.height))
