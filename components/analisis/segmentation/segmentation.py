from components.analisis.segmentation.unet_CellSegmentation import Cell_Segmentation
from django.core.files.uploadedfile import InMemoryUploadedFile
import cloudinary
from PIL import Image
import requests
from io import BytesIO
from io import StringIO




def segmentacion_imagen(url):
    modelo = Cell_Segmentation(weights_path='components/analisis/segmentation/pre_0_3_5.h5', saveImgs=True)
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    resultado = modelo.predict([img])[0]

    cld = cloudinary.uploader.upload(resultado)

    return cld['url']




