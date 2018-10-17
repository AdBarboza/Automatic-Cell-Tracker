from django.contrib import admin
from components.analisis.models import Resultado
from components.bitacora.models import Bitacora
from components.experimento.models import Experimento
from components.tratamiento.models import Tratamiento,ObservacionTratamiento
# Register your models here.


admin.site.register(Resultado)
admin.site.register(Bitacora)
admin.site.register(Experimento)
admin.site.register(Tratamiento)
admin.site.register(ObservacionTratamiento)
