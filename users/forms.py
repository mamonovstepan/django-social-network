from django import forms


class LoginForm(forms.Form):
    username = forms.Charfield()
    password = forms.CharField(widget=forms.PasswordInput)
