from django import forms

class loginForm(forms.Form):
    nome = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=50)
    senha = forms.PasswordInput()
    
        
            