from django import forms

class LoginForm (forms.Form):
    login = forms.CharField( widget=forms.TextInput(
                attrs={

                    'size': '30',
                    'id': 'username',
                    'placeholder': 'enter your login',
                }),label='Login', max_length=100)
    password = forms.CharField(
            widget=forms.TextInput(
                attrs={

                    'size': '30',
                    'id': 'username',
                    'placeholder': 'enter your password',
                }),
            min_length=5, label='Password')