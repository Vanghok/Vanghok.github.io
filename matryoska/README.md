# Matryoska

Bot educativo para pintar automáticamente en **wplace** siguiendo el calco de *Blue Marble*.

> **Uso responsable**: este código es solo para entornos autorizados. Respeta los términos de servicio del sitio donde lo utilices.

## Instalación

```bash
pip install pyautogui pillow keyboard
```

En Windows, los sonidos opcionales requieren `winsound` (incluido por defecto).

## Uso

1. Ejecuta `python -m matryoska.main`.
2. Define el área de trabajo con **F10**: presiona una vez para la esquina superior izquierda y otra vez para la inferior derecha.
3. Pulsa **F8** para iniciar el ciclo de pintado.
4. Usa **F9** para detener el bot de forma segura.
5. Opcional: **F4** restablece el estado interno.

## Parámetros ajustables

Edita `config.py` para modificar:

- `COLOR_TOL`: tolerancia de color (predeterminado 12).
- `SCAN_STEP`: salto de píxel al escanear (1 = todos los pixeles).
- `MAX_RETRY`: repintados máximos por pixel.

## Calibración de ROI

La selección mediante F10 guarda las coordenadas absolutas de la pantalla. Asegúrate de que el calco esté visible y que la paleta se encuentre en las posiciones establecidas en `PALETTE_LIST`.

## Buenas prácticas

- Ejecuta el bot solo cuando tengas permiso para automatizar el lienzo.
- Supervisa la actividad y detén el bot si la ventana pierde el foco.
- Ajusta los parámetros de `config.py` para adaptarse a tu equipo.
