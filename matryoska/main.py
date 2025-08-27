"""Punto de entrada del bot Matryoska."""
import time

from .controller import Controller


def main():
    ctrl = Controller()
    ctrl.register_hotkeys()
    print("Matryoska listo. Usa F10 para marcar ROI, F8 para iniciar, F9 para detener.")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
