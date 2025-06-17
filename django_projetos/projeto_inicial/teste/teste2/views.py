from django.shortcuts import render

def pagina_inic(request):
    return render(request, 'pagina_inicial.html')

def atracoes(request):
    return render(request, 'atracoes.html')