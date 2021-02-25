from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpRequest
from .forms import PoolForm
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from .models import Blog
from .models import Comment
from .models import Games
from .models import Orders
from .forms import CommentForm
from .forms import BlogForm
from .forms import ActsForm

def home(request):
    """Обработка закроса на Главная страница"""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Главная',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Обработка закроса на Контакты"""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Контакты',
            'message':'Страница с нашими контактами.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Обработка закроса на О нас"""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'О нас',
            'message':'Сведения о нас.',
            'year':datetime.now().year,
        }
    )

def links(request):
    """Обработка закроса на Полезные ресурсы"""
    assert isinstance(request,HttpRequest)
    return render(
        request,
        'app/links.html',
        {
            'title':'Полезные ресурсы',
            'message':'Здесь вы можете найти ссылки, которые могут вам помочь.',
            'year':datetime.now().year,
        }
     )

def pool(request):
    """Обработка закроса на Отзыв"""
    assert isinstance(request, HttpRequest)
    data = None
    receiver = {'1':'Цифровой ключ', '2':'Аккаунт'}
    score = {'1':'Отлично','2':'Хорошо','3':'Плохо'}
    if request.method == 'POST':
        form = PoolForm(request.POST)
        if form.is_valid():
            data = dict()
            data['name'] = form.cleaned_data['name']
            data['receiver'] = receiver[form.cleaned_data['receiver']]
            data['score'] = score[form.cleaned_data['score']]
            data['message'] = form.cleaned_data['message']
            if(form.cleaned_data['agree'] == True):
                data['agree'] = 'Да'
            else:
                data['agree'] = 'Нет'

            form = None
    else:
        form = PoolForm()
    return render(
            request,
            'app/pool.html',
            {
                'title':'Отзыв',
                'form':form,
                'data':data,
                'year':datetime.now().year
            }
        )

def registration(request):
    """Обработка закроса на Регистрация"""
    if request.method == "POST":
        regform = UserCreationForm(request.POST)
        if regform.is_valid():
            reg_f = regform.save(commit=False)
            reg_f.is_staff = False
            reg_f.is_active = True
            reg_f.is_superuser= False
            reg_f.date_joined = datetime.now()
            reg_f.last_login = datetime.now()
            regform.save()
            return redirect('login')
    else:
        regform = UserCreationForm()
    assert isinstance(request, HttpRequest)
    return render(
            request,
            'app/registration.html',
            {
                'regform': regform,
                'year':datetime.now().year,
            }
        )

def blog(request):
    """Обработка закроса на Блог"""
    posts = Blog.objects.all()
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/blog.html',
        {
            'title': 'Блог',
            'posts': posts,
            'year': datetime.now().year,
        }
    )

def blogpost(request, parametr):
    """Обработка закроса на Статья блога"""
    post_1 = Blog.objects.get(id=parametr)
    comments = Comment.objects.filter(post=parametr)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment_f = form.save(commit=False)
            comment_f.author = request.user
            comment_f.date = datetime.now()
            comment_f.post = Blog.objects.get(id=parametr)
            comment_f.save()

            return redirect('blogpost',parametr=post_1.id)
    else:
        form = CommentForm()
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/blogpost.html',
        {
            'post_1': post_1,
            'comments': comments,
            'form': form,
            'year': datetime.now().year,
        }
    )

def newpost(request):
    """Обработка закроса на Новая статья"""
    assert isinstance(request, HttpRequest)
    if request.method == "POST":
        blogform = BlogForm(request.POST, request.FILES)
        if blogform.is_valid():
            blog_f = blogform.save(commit=False)
            blog_f.posted = datetime.now()
            blog_f.author = request.user
            blog_f.save()

            return redirect('blog')
    else:
        blogform = BlogForm()
    
    return render(
        request,
        'app/newpost.html',
        {
            'blogform': blogform,
            'title': 'Добавление новой статьи',
            'year': datetime.now().year,
        }
    )

def video(request):
    """Обработка закроса на Видео"""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/video.html',
        {
            'year':datetime.now().year,
        }
    )

def games(request):
    """Обработка закроса на Постановки"""
    posts = Games.objects.all()

    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/acts.html',
        {
            'title': 'Игры',
            'posts': posts,
            'year': datetime.now().year,
        }
    )

def orders(request):
    """Обработка закроса на Мои билеты"""
    posts = Orders.objects.filter(author = request.user)
    posts_all = Games.objects.all()

    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/ticket.html',
        {
            'title': 'Мои игры',
            'posts': posts,
            'posts_all': posts_all,
            'year': datetime.now().year,
        }
    )

def addticket(request,id):
    """Обработка закроса на Купить билет"""
    test = Games.objects.filter(id=id)

    assert isinstance(request, HttpRequest)
    if request.method == "POST":
        actsform = ActsForm(request.POST, request.FILES)
        if actsform.is_valid():
            acts_f = actsform.save(commit=False)
            acts_f.post_id = id
            acts_f.posted = datetime.now()
            acts_f.author = request.user
            acts_f.save()

            return redirect('orders')
    else:
        actsform = ActsForm()
    
    return render(
        request,
        'app/addticket.html',
        {
            'actsform': actsform,
            'posts': test,
            'title': 'Уверены, что хотите купить эту игру?',
            'year': datetime.now().year,
        }
    )

def buyticket(request, bid):
    """Обработка закроса Оплатить"""
    assert isinstance(request, HttpRequest)
    posts = Orders.objects.get(id = bid)

    posts.ready = True
    posts.save()
    
    return redirect('orders')  

def delticket(request, did):
    """Обработка закроса Удалить"""
    assert isinstance(request, HttpRequest)

    posts = Orders.objects.get(id = did)
    posts.delete()

    return redirect('orders')
