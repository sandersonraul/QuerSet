from django.contrib import admin

from .models import (
  Cliente, 
  Produto, 
  Pedido
)

admin.site.register(Cliente)
admin.site.register(Produto)
admin.site.register(Pedido)

