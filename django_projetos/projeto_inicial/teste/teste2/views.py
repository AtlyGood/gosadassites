from django.shortcuts import render, redirect
from .forms import BancoForm
from django.http import HttpRequest

def pagina_inic(request):
    return render(request, 'pagina_inicial.html')

def atracoes(request):
    return render(request, 'atracoes.html')

def produtos(request):
    return render(request, 'produtos.html')

def login(request):
    return render(request, 'Login.html')

def cadastro(request:HttpRequest):
    if request.method == "POST":
        formulario = BancoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect("loginsite")
    cadastra_dados = {
        "form":BancoForm
    }
    return render(request, 'Cadastro.html', cadastra_dados)