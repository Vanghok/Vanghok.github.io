"""Pintado de pixeles y corrección."""
import random
import time
from typing import Dict, Iterable, List, Tuple
import pyautogui

from . import config
from .palette import click_palette, color_distance

Task = Tuple[int, int, Dict]


def verify_pixel(x: int, y: int, rgb: Tuple[int, int, int]) -> bool:
    """Verifica si el pixel en pantalla coincide con el rgb dado."""
    current = pyautogui.pixel(x, y)
    return color_distance(current, rgb) <= config.COLOR_TOL


def paint_tasks(tasks_by_color: Dict[Tuple[int, int, int], List[Task]]):
    """Pinta las tareas agrupadas por color."""
    for color_rgb, tasks in tasks_by_color.items():
        if not tasks:
            continue
        color = tasks[0][2]
        click_palette(color)
        for x, y, _ in tasks:
            pyautogui.moveTo(x, y)
            pyautogui.click()
            time.sleep(config.human_sleep())
            if not verify_pixel(x, y, color_rgb):
                retry = 0
                while retry < config.MAX_RETRY:
                    pyautogui.moveTo(x, y)
                    pyautogui.click()
                    time.sleep(config.human_sleep())
                    if verify_pixel(x, y, color_rgb):
                        break
                    retry += 1


def paint_corrections(anomalies: Iterable[Task]):
    """Repinta pixeles detectados como incorrectos."""
    for x, y, color in anomalies:
        click_palette(color)
        pyautogui.moveTo(x, y)
        pyautogui.click()
        time.sleep(config.human_sleep())
