"""Control del estado global y gestión de hotkeys."""
import threading
import time
import keyboard
import pyautogui

from . import config
from .roi import ROIManager
from .scanner import scan_image, find_anomalies
from .painter import paint_tasks, paint_corrections


class Controller:
    def __init__(self):
        self.running = False
        self.roi_manager = ROIManager()
        self.paint_thread: threading.Thread | None = None
        self.stop_event = threading.Event()

    # --- Hotkeys ---
    def register_hotkeys(self):
        keyboard.add_hotkey(config.HOTKEY_START, self.start)
        keyboard.add_hotkey(config.HOTKEY_STOP, self.stop)
        keyboard.add_hotkey(config.HOTKEY_CAPTURE, self.capture_corner)
        keyboard.add_hotkey(config.HOTKEY_RESET, self.reset)

    # --- Acciones ---
    def capture_corner(self):
        x, y = pyautogui.position()
        self.roi_manager.set_corner(x, y)
        if config.winsound:
            config.winsound.Beep(880, 100)

    def start(self):
        if self.running or not self.roi_manager.has_roi():
            return
        self.running = True
        self.stop_event.clear()
        self.paint_thread = threading.Thread(target=self.loop, daemon=True)
        self.paint_thread.start()
        if config.winsound:
            config.winsound.Beep(440, 100)

    def stop(self):
        self.running = False
        self.stop_event.set()
        if config.winsound:
            config.winsound.Beep(220, 100)

    def reset(self):
        if self.running:
            self.stop()
        self.roi_manager = ROIManager()

    # --- Loop de trabajo ---
    def loop(self):
        while not self.stop_event.is_set():
            img = self.roi_manager.screenshot()
            tasks = scan_image(img, self.roi_manager.roi)
            paint_tasks(tasks)
            anomalies = find_anomalies(img, self.roi_manager.roi)
            paint_corrections(anomalies)
            time.sleep(0.05)
