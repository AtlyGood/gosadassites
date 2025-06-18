from django.shortcuts import render, redirect
from .forms import BancoForm
from django.http import HttpRequest
from django.contrib import messages  # Para mensagens mais robustas
from .models import BancoModel  # Importação adicionada

def pagina_inic(request):
    return render(request, 'pagina_inicial.html')

def atracoes(request):
    return render(request, 'atracoes.html')

def produtos(request):
    return render(request, 'produtos.html')

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        
        if not email or not senha:
            messages.error(request, 'Por favor, preencha todos os campos.')
            return render(request, 'login.html')
        
        try:
            usuario = BancoModel.objects.get(email=email)
            if usuario.senha == senha: 
                return redirect('produtossite')  
            else:
                messages.error(request, 'email ou Senha incorreta.')
        except BancoModel.DoesNotExist:
            messages.error(request, 'Email não cadastrado.')
        except Exception as e:
            messages.error(request, f'Ocorreu um erro: {str(e)}')
    
    return render(request, 'login.html')
    
    return render(request, 'login.html', {'form': form, 'mensagem': mensagem})

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