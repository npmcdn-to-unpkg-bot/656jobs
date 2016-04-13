from django import forms
from django.contrib.auth.models import User
from django.forms import TextInput

class UserForm(forms.ModelForm):
    #usuario = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class' : 'form-control', 'name': 'Usuario', 'placeholder' : 'usuario', 'aria-describedby': 'basic-addon1' }))
    #password = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class' : 'form-control','name': 'Password', 'type' : 'password', 'placeholder' : 'password', 'aria-describedby': 'basic-addon2'}))
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'username' : TextInput(attrs={'class' : 'form-control', 'name': 'Usuario', 'placeholder' : 'usuario', 'aria-describedby': 'basic-addon1' ,'required' : 'required' }),
            'password' : TextInput(attrs={'type' : 'password', 'class' : 'form-control', 'name': 'Password', 'placeholder' : 'password', 'aria-describedby': 'basic-addon2', 'required' : 'required' }),
            
        }


