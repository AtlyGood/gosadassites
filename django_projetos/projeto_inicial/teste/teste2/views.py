from django.shortcuts import render, redirect
from .forms import BancoForm
from django.http import HttpRequest
from django.contrib import messages  # Para mensagens mais robustas
from .models import BancoModel  # Importação adicionada
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views.decorators.http import require_POST

def pagina_inic(request):
    return render(request, 'pagina_inicial.html')

def atracoes(request):
    return render(request, 'atracoes.html')

def produtos(request):
    return render(request, 'produtos.html')

def login(request):
    mensagem = None
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        
        if not email or not senha:
            messages.error(request, 'Preencha todos os campos')
            return render(request, 'login.html')
        
        try:
            usuario = BancoModel.objects.get(email=email)
            if usuario.check_password(senha):
                request.session['usuario_email'] = email
                return redirect('produtossite')
            else:
                messages.error(request, 'Senha incorreta')
        except BancoModel.DoesNotExist:
            messages.error(request, 'Email não cadastrado')
        except Exception as e:
            messages.error(request, f'Erro no login: {str(e)}')
    
    return render(request, 'login.html')  # Removi as variáveis não definidas
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

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

@csrf_exempt  # Temporariamente para testes
@require_POST
def delete_account(request):
    try:
        if 'usuario_email' not in request.session:
            return JsonResponse({'success': False, 'message': 'Não autenticado'}, status=401)
            
        email = request.session['usuario_email']
        user = BancoModel.objects.get(email=email)
        user.delete()
        
        # Limpeza da sessão
        request.session.flush()
        
        return JsonResponse({'success': True})
        
    except BancoModel.DoesNotExist:
        return JsonResponse({'success': False, 'message': 'Usuário não encontrado'}, status=404)
    except Exception as e:
        return JsonResponse({'success': False, 'message': str(e)}, status=500)