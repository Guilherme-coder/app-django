from django.contrib import admin

from .models import Produto, Usuario, Evento, Reserva

# Register your models here.

admin.site.register(Produto)
admin.site.register(Usuario)
admin.site.register(Evento)
admin.site.register(Reserva)