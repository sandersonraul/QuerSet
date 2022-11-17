from django.shortcuts import render
from .models import Cliente, Produto, Pedido

# Create your views here.
def home(request):
  clientes = Cliente.objects.all()
  return render(request, "home.html", {"clientes": clientes})

def produtos(request):
  produtos = Produto.objects.all()
  return render(request, "produtos.html", {"produtos": produtos})

def pedidos(request):
  pedidos = Pedido.objects.all().values("cliente_id__nome","produtos__titulo", "status", "valor")
  return render(request, "pedidos.html", {"pedidos": pedidos})