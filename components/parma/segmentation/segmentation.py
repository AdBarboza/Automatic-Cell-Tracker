from components.parma.segmentation.unet_CellSegmentation import Cell_Segmentation
from django.core.files.uploadedfile import InMemoryUploadedFile
from PIL import Image
from io import BytesIO

def segmentacion_imagen(img_bytes, imgName):
    modelo = Cell_Segmentation(weights_path='components/parma/segmentation/pre_0_3_5.h5', saveImgs=True, imgName = imgName)
    img = Image.open(BytesIO(img_bytes))
    resultado = modelo.predict([img])[0]

    return resultado




