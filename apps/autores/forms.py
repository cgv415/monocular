from django import forms

'''
Created on 15/12/2014

@author: Carlos
'''

class Formulario(forms.Form):
    nombre = forms.CharField(max_length=100)
    mensaje = forms.CharField()
    mail = forms.EmailField()