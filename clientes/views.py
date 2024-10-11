from django.shortcuts import render
from .models import Cliente

# Create your views here.

def lista_clientes(request):
    clientes = Cliente.objects.all()  # Pega todos os clientes do banco de dados
    return render(request, 'clientes/lista_clientes.html', {'clientes': clientes})