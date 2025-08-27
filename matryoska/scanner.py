"""Escaneo del calco y generación de la cola de trabajo."""
from collections import defaultdict
from typing import Dict, List, Tuple
from PIL import Image

from . import config
from .palette import nearest_color


Task = Tuple[int, int, Dict]


def scan_image(img: Image.Image, roi: config.ROI) -> Dict[Tuple[int, int, int], List[Task]]:
    """Genera tareas agrupadas por color desde la imagen dada.

    Devuelve un dict {(r,g,b): [tasks...]}
    """
    width, height = img.size
    tasks_by_color: Dict[Tuple[int, int, int], List[Task]] = defaultdict(list)
    for y in range(0, height, config.SCAN_STEP):
        for x in range(0, width, config.SCAN_STEP):
            rgb = img.getpixel((x, y))[:3]
            color = nearest_color(rgb)
            if color:
                abs_x = roi.x1 + x
                abs_y = roi.y1 + y
                tasks_by_color[tuple(color['rgb'])].append((abs_x, abs_y, color))
    return tasks_by_color


def find_anomalies(img: Image.Image, roi: config.ROI) -> List[Task]:
    """Busca pixeles oscuros que deberían tener un color de la paleta.

    Usa una ventana 3x3 para evitar repeticiones innecesarias.
    """
    width, height = img.size
    anomalies: List[Task] = []
    for y in range(1, height - 1):
        for x in range(1, width - 1):
            rgb = img.getpixel((x, y))[:3]
            if sum(rgb) < 30:  # pixel oscuro
                # revisa vecindad
                neighbors = [img.getpixel((x + dx, y + dy))[:3]
                             for dx in (-1, 0, 1) for dy in (-1, 0, 1)
                             if not (dx == 0 and dy == 0)]
                for n in neighbors:
                    color = nearest_color(n)
                    if color:
                        abs_x = roi.x1 + x
                        abs_y = roi.y1 + y
                        anomalies.append((abs_x, abs_y, color))
                        break
    return anomalies
