from django import forms


class LoginForm(forms.Form):
    user = forms.CharField(max_length=100, required=True)
    password = forms.CharField(max_length=100, required=True)

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=100, required=True)
    email = forms.CharField()
    password = forms.CharField(max_length=100, required=True)
    repassword = forms.CharField(max_length=100, required=True)