from django import forms

class Formulario(forms.Form):
    nombre = forms.CharField(max_length=100)
    mensaje = forms.CharField(widget = forms.Textarea)
    mail = forms.EmailField()