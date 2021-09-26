from django.shortcuts import render
from .models import Produto

# Create your views here.

def index(request):
    produtos = Produto.objects.order_by('data')

    parametros = {
        'produtos': produtos
    }

    return render(request, 'bazarapp/index.html', parametros)

# def store(request):
