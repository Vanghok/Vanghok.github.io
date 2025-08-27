"""Funciones relacionadas a la paleta de colores."""
from typing import Dict, Optional, Tuple
import pyautogui
from math import sqrt

from . import config


Color = Dict[str, Tuple[int, int]]


def color_distance(c1: Tuple[int, int, int], c2: Tuple[int, int, int]) -> float:
    """Distancia euclidiana entre dos colores RGB."""
    return sqrt(sum((a - b) ** 2 for a, b in zip(c1, c2)))


def nearest_color(rgb: Tuple[int, int, int]) -> Optional[Dict]:
    """Devuelve el color de la paleta más cercano al RGB dado dentro de la tolerancia."""
    best = None
    best_dist = float('inf')
    for color in config.PALETTE_LIST:
        dist = color_distance(rgb, color['rgb'])
        if dist < best_dist:
            best = color
            best_dist = dist
    if best_dist <= config.COLOR_TOL:
        return best
    return None


def click_palette(color: Dict):
    """Realiza click en la posición de la paleta correspondiente."""
    pyautogui.moveTo(*color['pos'])
    pyautogui.click()
