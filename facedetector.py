'''
Proyecto 2 Visión por Computadora.
Detector de rostros

Integrantes:
- Diego Córdova
- Paola Contreras
- Paola de León

'''

import cv2
import os
import glob
import random


class FaceDetector:

    def __init__(self) -> None:
        self.classifier_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
        self.face_cascade = cv2.CascadeClassifier(self.classifier_path)

    def getImagesPaths(self):
        '''
            Obtener lista con rutas de las imágenes.
        '''
        folderPath = "./imagenes/" 
        extension = '*.jpg'
        
        pics = glob.glob(os.path.join(folderPath, extension))
        random.shuffle(pics)

        return pics

    def predict(self, image):
        '''
            Reconocimiento de rostros de una imagen.

            Parámetros:
            - image

            Returns:
            faces.
        '''
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        
        return faces

    def showDetectedFaces(self, faces, imagen):
        '''
            Mostrar las caras detectadas

            Parámetros:
            - faces: Lista con coordenadas de rostros encontrados.
            - imagen
        '''
        for (x, y, w, h) in faces:
            cv2.rectangle(imagen, (x, y), (x+w, y+h), (255, 0, 0), 2)

    def processImage(self, cant=1):
        '''
            Identificar rostros en imágenes.
        '''
        pics = self.getImagesPaths()

        for i, imagen_path in enumerate(pics[:cant]):
            imagen = cv2.imread(imagen_path)
            faces = self.predict(imagen)
            
            self.showDetectedFaces(faces, imagen)
            
            cv2.imshow(f'Imagen {i+1}', imagen)
            cv2.waitKey(0)
            cv2.destroyAllWindows()


    def processSingleImage(self, imagen_path):
        '''
            Identificar rostros en imágenes.
        '''
        imagen = cv2.imread(imagen_path)
        faces = self.predict(imagen)
        
        self.showDetectedFaces(faces, imagen)
        return imagen


    def videoCapturing(self):
        '''
            Identificación de rostros en tiempo real.
        '''
        cap = cv2.VideoCapture(0)

        if self.face_cascade.empty():
            raise IOError('No se pudo cargar el clasificador.')
        else:
            while True:
                # Leer frames del video
                ret, frame = cap.read()
                
                if not ret:
                    break
                    
                # Detectar caras en el frame
                faces = self.face_cascade.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
                self.showDetectedFaces(faces,frame)
                
                cv2.imshow('Face Detection', frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

            cap.release()
            cv2.destroyAllWindows()
