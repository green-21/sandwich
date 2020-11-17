from django import forms

class LoginForm(forms.Form):
    user_id = forms.CharField(max_length=100)
    user_pw = forms.CharField(max_length=100)