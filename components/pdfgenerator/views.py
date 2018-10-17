from django.shortcuts import render
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from io import BytesIO
from django.http import FileResponse
from reportlab.lib.utils import ImageReader

from components.experimento.models import Experimento
from components.bitacora.models import Bitacora
from components.analisis.models import Resultado
from components.tratamiento.models import Tratamiento

def generate(request,id):
    experimento = Experimento.objects.get(id=id)
    resultados_list = Resultado.objects.all().filter(experimento=experimento)

    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=' + experimento.nombre + "_" + str(experimento.id)+ ".pdf"

    buffer = BytesIO()

    # Create the PDF object, using the BytesIO object as its "file."
    p = canvas.Canvas(buffer)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.setTitle("Experimento - "+ experimento.nombre + " - " + str(experimento.id))
    p.drawString(100, 760, "Informe")

    p.drawString(100,700, "Nombre experimento: " + experimento.nombre)
    p.drawString(100,680, "Sexo: " + experimento.sexo)
    p.drawString(100,660, "Grupo Sanguineo: " + experimento.gp_sanguineo)
    p.drawString(100,640, "Factor H: " + experimento.factor_h)
    p.drawString(100,620, "Alergias: " + experimento.alergias)
    p.drawString(100,600, "Padecimientos: " + experimento.padecimiento)
    
    row_level = 600

    p.drawString(100,row_level-50, "Resultados de analisis: ")
    for resultado in resultados_list:
        row_level-=100
        p.drawString(100, row_level, "Código: "+ str(resultado.id))
        p.drawString(100, row_level-20, "Fecha Analisis: "+ str(resultado.fch_analisis))
        p.drawString(100, row_level-40, "Observaciones: "+ resultado.observaciones)
        logo = ImageReader(str(resultado.url_resultado))
        p.drawImage(logo, 100, row_level-325, mask='auto')
        row_level=700
        p.showPage()

    # Close the PDF object cleanly.
    p.showPage()
    p.save()

    # Get the value of the BytesIO buffer and write it to the response.
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response