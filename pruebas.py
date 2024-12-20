import os
import cv2
from PIL import Image
import numpy as np
import pydicom
import mritopng


dicom_path = "C:/Users/samue/Documents/UNI/TFG/Prueba/Calc-Test_P_00038_LEFT_CC.dcm"
png_path = "C:/Users/samue/Documents/UNI/TFG/Prueba/Calc-Test_P_00038_LEFT_CC.png"
#PEPEPEPEPEP
def convertirDCMtoPNG(dicom_path, png_path):
    # Leer el archivo DICOM
    ds = pydicom.dcmread(dicom_path)

    # Obtener la matriz de píxeles
    pixel_array = ds.pixel_array

    # Convertir la matriz de píxeles a imagen PIL
    img = Image.fromarray(pixel_array)

    # Guardar la imagen en formato PNG, asegurando 16 bits
    img.save(png_path)
    print('Conversión realizada')

def leerPixeles(png_path):
    pixeles = cv2.imread(png_path)
    return pixeles
convertirDCMtoPNG(dicom_path, png_path)
print(leerPixeles(png_path))        
