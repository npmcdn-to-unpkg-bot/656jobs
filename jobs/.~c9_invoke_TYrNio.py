from django import forms
from django.contrib.auth.models import User
from django.forms import TextInput
from .models import Profile


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password','email', 'first_name', 'last_name']
        widgets = {
            'first_name' : TextInput(attrs={'class' : 'form-control', 'name': 'Nombre', 'placeholder' : 'Ingresa tu nombre', 'aria-describedby': 'basic-addon1' ,'required' : 'required' }),
            'last_name' : TextInput(attrs={'class' : 'form-control', 'name': 'Apellido', 'placeholder' : 'Ingresa tu Apellido', 'aria-describedby': 'basic-addon2', 'required' : 'required' }),
            'email' : TextInput(attrs={'type': 'email', 'class' : 'form-control', 'name': 'email', 'placeholder' : 'Ingresa tu email', 'aria-describedby': 'basic-addon1' ,'required' : 'required' }),
            'username' : TextInput(attrs={'class' : 'form-control', 'name': 'Usuario', 'placeholder' : 'usuario', 'aria-describedby': 'basic-addon1' ,'required' : 'required' }),
            'password' : TextInput(attrs={'type' : 'password', 'class' : 'form-control', 'name': 'Password', 'placeholder' : 'password', 'aria-describedby': 'basic-addon2', 'required' : 'required' }),
        }

'''
class EditProfile(forms.ModelForm):
    professional_name = forms.CharField(widget = forms.TextInput(attrs={'class' : 'form-control', 'name': 'email', 'placeholder' : 'ej. Ingeniero en sistemas, Mecanico, Medico', 'aria-describedby': 'basic-addon1'  }),)
    profile_image = forms.ImageField()
    resume = forms.FileField(help_text='PDF')
    summary = forms.CharField(widget=forms.Textarea,help_text='Escribe un breve resumen de tus habilidades')
    contact = forms.CharField(widget=forms.Textarea,help_text='Agrega todas las formas en que podamos contactarte')
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']
        widgets = {
            'email' : TextInput(attrs={'type': 'email', 'class' : 'form-control', 'name': 'email', 'placeholder' : 'email', 'aria-describedby': 'basic-addon1' ,'required' : 'required' }),
            'first_name' : TextInput(attrs={'class' : 'form-control', 'name': 'nomnbre', 'placeholder' : 'nombre', 'aria-describedby': 'basic-addon2', 'required' : 'required' }),
            'last_name' : TextInput(attrs={'class' : 'form-control', 'name': 'apellido', 'placeholder' : 'apellido', 'aria-describedby': 'basic-addon2', 'required' : 'required' }),
            
        }
'''
class EditProfile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['professional_name','profile_image','resume','summary','contact']
        exclude = ('user',)
        widgets = {
            'professional_name' : TextInput(attrs = {'class' : 'form-control', 'name' : 'professionalname', 'placeholder': 'ej. Ingeniero en sistemas, Mecanico, Medico', 'aria-describedby': 'basic-addon1' })
        }
        
        
class WorkExperience(forms.)