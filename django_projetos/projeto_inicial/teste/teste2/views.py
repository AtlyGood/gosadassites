from django.shortcuts import render

def pagina_inic(request):
    return render(request, 'pagina_inicial.html')

def atracoes(request):
    return render(request, 'atracoes.html')

def produtos(request):
    return render(request, 'produtos.html')

def login(request):
    return render(request, 'Login.html')

def cadastro(request):
    return render(request, 'Cadastro.html')