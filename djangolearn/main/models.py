from django.db import models
from djmoney.models.fields import MoneyField
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

class Task(models.Model):
    title = models.CharField('Название', max_length=50)
    Task = models.TextField('Описание')
    cena = MoneyField('Цена', decimal_places=2, max_digits=6, default=0, default_currency='RUB')

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
class News(models.Model):
    NewsTitle = models.CharField('Название', max_length=50)
    AboutNews = models.TextField('Описание')
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.NewsTitle


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают')
        return cd['password2']


class LoginForm(forms.Form):
    username = forms.CharField(label='Логин')
    password = forms.CharField(label='Пароль',widget=forms.PasswordInput)



