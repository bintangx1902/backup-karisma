from django.apps import apps
from django.forms import ModelForm, DateTimeInput
from django.contrib.auth.models import User
from django import forms

Files = apps.get_model('file_control', 'Files')
Recap = apps.get_model('presence', 'Recap')
ClassName = apps.get_model('presence', 'ClassName')
GenerateQRCode = apps.get_model('presence', 'GenerateQRCode')
UserData = apps.get_model('presence', 'UserData')
BoardingHouse = apps.get_model('presence', 'BoardingHouse')


class ClassCreationForms(ModelForm):
    class Meta:
        model = ClassName
        fields = '__all__'


class GenerateQRCodeForms(ModelForm):
    class Meta:
        model = GenerateQRCode
        fields = ['valid_until']

        widgets = {
            'valid_until': DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'})
        }


class UserChangeDataForms(ModelForm):
    class Meta:
        model = User
        fields = ['username']


class CreateClassForms(ModelForm):
    class Meta:
        model = ClassName
        fields = ["name"]

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'})
        }


class BoardingHouseForms(ModelForm):
    class Meta:
        model = BoardingHouse
        fields = ['name', 'spec', 'link']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'spec': forms.TextInput(attrs={'class': 'form-control w-100'}),
            'link': forms.TextInput(attrs={'class': 'form-control'}),
        }
