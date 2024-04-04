'''
Proyecto 2 Visión por Computadora.
Detector de rostros

Integrantes:
- Diego Córdova
- Paola Contreras
- Paola de León

'''

from facedetector import FaceDetector


faceDetector = FaceDetector()

opc = ''
menu = """
DETECTOR DE ROSTROS

1. Evaluar imágenes
2. Video Capturing
3. Salir
"""


print(menu)
opc = input(" • Ingrese la opción: ")
match(opc):
    case '1':
        cantidad_imagenes = 3
        faceDetector.processImage(cant=cantidad_imagenes)
    case '2':
        faceDetector.videoCapturing()