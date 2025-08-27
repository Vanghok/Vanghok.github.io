"""Configuración global del bot Matryoska."""
from dataclasses import dataclass
import random

# Lista de colores de la paleta y sus coordenadas en pantalla
PALETTE_LIST = [
    {'pos': (42, 920),   'rgb': (0, 0, 0)},
    {'pos': (90, 921),   'rgb': (60, 60, 60)},
    {'pos': (160, 923),  'rgb': (120, 120, 120)},
    {'pos': (212, 925),  'rgb': (210, 210, 210)},
    {'pos': (265, 920),  'rgb': (255, 255, 255)},
    {'pos': (333, 924),  'rgb': (96, 0, 24)},
    {'pos': (393, 921),  'rgb': (237, 28, 36)},
    {'pos': (458, 926),  'rgb': (255, 127, 39)},
    {'pos': (513, 925),  'rgb': (246, 170, 9)},
    {'pos': (564, 923),  'rgb': (249, 221, 59)},
    {'pos': (625, 927),  'rgb': (255, 250, 188)},
    {'pos': (689, 926),  'rgb': (14, 185, 104)},
    {'pos': (749, 922),  'rgb': (19, 230, 123)},
    {'pos': (807, 919),  'rgb': (135, 255, 94)},
    {'pos': (863, 918),  'rgb': (12, 129, 110)},
    {'pos': (939, 923),  'rgb': (16, 174, 166)},
    {'pos': (988, 931),  'rgb': (19, 225, 190)},
    {'pos': (1051, 920), 'rgb': (40, 80, 158)},
    {'pos': (1116, 915), 'rgb': (64, 147, 228)},
    {'pos': (1173, 915), 'rgb': (96, 247, 242)},
    {'pos': (1231, 927), 'rgb': (107, 80, 246)},
    {'pos': (1295, 919), 'rgb': (153, 177, 251)},
    {'pos': (1344, 922), 'rgb': (120, 12, 153)},
    {'pos': (1397, 920), 'rgb': (170, 56, 185)},
    {'pos': (1464, 912), 'rgb': (224, 159, 249)},
    {'pos': (1520, 922), 'rgb': (203, 0, 122)},
    {'pos': (1584, 921), 'rgb': (236, 31, 128)},
    {'pos': (1640, 920), 'rgb': (243, 141, 169)},
    {'pos': (1692, 924), 'rgb': (104, 70, 52)},
    {'pos': (1762, 920), 'rgb': (149, 104, 42)},
    {'pos': (1816, 912), 'rgb': (248, 178, 119)}
]

# Parámetros ajustables
COLOR_TOL = 12  # tolerancia Euclidiana para considerar que un color coincide
SCAN_STEP = 1  # salto de pixel al escanear
MAX_RETRY = 2  # repintados máximos

# Pausa humana entre clicks

def human_sleep():
    """Genera un pequeño tiempo de pausa para evitar patrones mecánicos."""
    return random.uniform(0.008, 0.025)

# Hotkeys
HOTKEY_START = 'f8'
HOTKEY_STOP = 'f9'
HOTKEY_CAPTURE = 'f10'
HOTKEY_RESET = 'f4'

# Sonidos opcionales
try:
    import winsound
except Exception:  # pragma: no cover - winsound solo existe en Windows
    winsound = None


@dataclass
class ROI:
    """Región de interés en pantalla."""
    x1: int
    y1: int
    x2: int
    y2: int

    def normalized(self) -> 'ROI':
        """Devuelve la ROI con coordenadas normalizadas."""
        x1, x2 = sorted((self.x1, self.x2))
        y1, y2 = sorted((self.y1, self.y2))
        return ROI(x1, y1, x2, y2)

    @property
    def width(self) -> int:
        return abs(self.x2 - self.x1)

    @property
    def height(self) -> int:
        return abs(self.y2 - self.y1)
