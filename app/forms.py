from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from django.db import models
from .models import Comment
from .models import Blog
from .models import Orders
from .models import Games

class BootstrapAuthenticationForm(AuthenticationForm):
    """Форма стандартной авторизации"""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Имя пользователя'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Пароль'}))


class PoolForm(forms.Form):
    """Форма Отзыв"""
    name = forms.CharField(label='Ваше имя', min_length = 2, max_length = 100)
    receiver = forms.ChoiceField(label='Тип купленной игры',
                             choices=[('1','Цифровой ключ'),
                                      ('2','Аккаунт')],
                             widget=forms.RadioSelect, initial=1)
    score = forms.ChoiceField(label='Общее впечатление',
                             choices=[('1','Отлично'),('2','Хорошо'),
                                      ('3','Плохо')],initial=1)
    message = forms.CharField(label='Отзыв', widget=forms.Textarea(attrs={'rows':10,'cols':100}))
    agree = forms.BooleanField(label='Я согласен на отправление моего отзыва', required=True)


class CommentForm (forms.ModelForm):
    """Форма Комментарий"""
    class Meta:
        model = Comment
        fields = ('text',)
        labels = {'text': "Добавить комментарий"}


class BlogForm (forms.ModelForm):
    """Форма Новая статья"""
    class Meta:
        model = Blog
        fields = ('title','description','content','image')
        labels = {'title': "Заголовок",'description': "Краткое содержание",'content': "Полное содержание",'image': "Изображение"}

class ActsForm (forms.ModelForm):
    class Meta:
        model = Orders
        fields = ()