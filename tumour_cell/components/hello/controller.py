from django.http import HttpResponse


def hola(request):
    return HttpResponse("Ivan se la come")