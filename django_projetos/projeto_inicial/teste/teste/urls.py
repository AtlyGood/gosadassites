"""
URL configuration for teste project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from teste2.views import pagina_inic, atracoes, produtos, cadastro, login, delete_account, editar_informacoes

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Home/', pagina_inic, name = "homeatalho"),
    path('atracoes/', atracoes, name = "atracoesatalho"),
    path('Produtos/', produtos, name='produtossite'),
    path('Cadastro/', cadastro, name='cadastro'),
    path('Login/', login, name='loginsite'),
    path('delete-account/', delete_account, name='delete_account'),
    path('editar-informacoes/', editar_informacoes, name='editar_informacoes'),
]
