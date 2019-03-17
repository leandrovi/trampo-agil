from django import forms
from site_trampo_agil.models import Logincandidatos

class LoginCriarForm(forms.ModelForm):
    class Meta:
        models = Contato
        fields =  [
                'Email'
                'Senha'
        ]

