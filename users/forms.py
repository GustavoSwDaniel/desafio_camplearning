from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import CustomUser
from django.contrib.auth.forms import AuthenticationForm

class UserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'name', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({
            'class': 'w-full px-3 py-2 leading-tight text-gray-700 bg-gray-200 border rounded shadow appearance-none focus:outline-none focus:shadow-outline'
        })
        self.fields['name'].widget.attrs.update({
            'class': 'w-full px-3 py-2 leading-tight text-gray-700 bg-gray-200 border rounded shadow appearance-none focus:outline-none focus:shadow-outline'
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'w-full px-3 py-2 leading-tight text-gray-700 bg-gray-200 border rounded shadow appearance-none focus:outline-none focus:shadow-outline'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'w-full px-3 py-2 leading-tight text-gray-700 bg-gray-200 border rounded shadow appearance-none focus:outline-none focus:shadow-outline'
        })

class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring focus:ring-blue-500 focus:border-blue-500',
            'placeholder': 'Email'
        })
        self.fields['password'].widget.attrs.update({
            'class': 'mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring focus:ring-blue-500 focus:border-blue-500',
            'placeholder': 'Senha'
        })
