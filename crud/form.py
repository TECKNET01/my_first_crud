from django import forms

class loginForm(forms.Form):
    email = forms.EmailField(max_length=50)
    senha = forms.PasswordInput()
    