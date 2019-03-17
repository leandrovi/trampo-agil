from django import forms
from site_trampo_agil.models import LoginCandidatos 

class LoginCriarForm(forms.ModelForm):
   class Meta:
        model = LoginCandidatos
        fields =  [
                'email',
                'senha',
        ]
        