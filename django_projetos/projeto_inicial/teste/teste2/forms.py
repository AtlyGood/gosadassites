from django import forms
from .models import BancoModel

class BancoForm(forms.ModelForm):
    class Meta:
        model = BancoModel
        fields = ['email', 'senha', 'nome', 'sobrenome']