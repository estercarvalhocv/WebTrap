from django import forms

class HoneypotForm(forms.Form):
    nome = forms.CharField(max_length=100)
    email = forms.EmailField()