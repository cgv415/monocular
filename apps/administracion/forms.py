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
    telefono = forms.IntegerField()
    ciudad = forms.CharField()
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']
        widgets = {
            'password': forms.PasswordInput(),
        }
        
        
class UserForm(UserCreationForm):
    telefono = forms.IntegerField()
    ciudad = forms.CharField()
    
class FormNoticia(forms.Form):
    titulo= forms.CharField()
    texto=forms.Textarea()
    imagen = forms.ImageField()
    resumen = forms.Textarea()
    fecha = forms.DateField()