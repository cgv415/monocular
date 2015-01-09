from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.contrib.auth.models import User
 
SERVICIO_CONTRATADO = (
   ('cortometraje', 'Cortometraje'),
   ('publicidad', 'Publicidad'),
   ('etanolaje', 'Etanolaje'),
   ('videoclip', 'Videoclip'),
   ('otro', 'Otro'),
) 

class SignUpForm(ModelForm):
    servicio_Contratado = forms.ChoiceField(choices=SERVICIO_CONTRATADO)
    proyecto =forms.CharField(max_length=50)
    telefono = forms.IntegerField()
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']
        widgets = {
            'password': forms.PasswordInput(),
        }
        
        
class UserForm(UserCreationForm):
    servicio_Contratado = forms.CharField(max_length=50)
    proyecto =forms.CharField(max_length=50)
    telefono = forms.IntegerField()