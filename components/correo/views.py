from django.shortcuts import render
from django.shortcuts import redirect
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
from django.core.mail import EmailMessage
import os
from io import BytesIO

def index_correo(request):
    return render(request, "index_correo.html")


def enviar_correo(request):
    if request.method == 'GET' or request.method == 'POST':
        f = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+"\correo\static\zPython.png"

        subject = 'Thank you for registering to our site'
        message = ' it  means a world to us '
        email_from = settings.EMAIL_HOST_USER

        # buffer
        buffer = BytesIO()
        buffer.write(b"Hello world")
        pdf = buffer.getvalue()
        buffer.close()

        # el email se saca de request post
        recipient_list = ['ivanfelipecp@gmail.com']

        email = EmailMessage(
            subject, message, email_from, recipient_list
        )
        
        #email.attach_file(f)
        email.attach("adrian.pdf",pdf,"txt/pdf")
        email.send()

    return redirect('index_correo')