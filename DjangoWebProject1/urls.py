from datetime import datetime
from django.urls import path

"""Активация администраивного раздела"""
from django.urls import include
from django.contrib import admin
admin.autodiscover()

from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views

from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings


urlpatterns = [
    path('', views.home, name='home'), #ссылка на обработку Главная страница
    path('accounts/profile/', views.home, name='home'), #избавляемся от бага при логине (только в vs19)
    path('contact/', views.contact, name='contact'), #ссылка на обработку Контакты
    path('links/', views.links, name='links'), #ссылка на обработку Полезные ресурсы
    path('about/', views.about, name='about'), #ссылка на обработку О нас
    path('pool/', views.pool, name='pool'), #ссылка на обработку Отзыв
    path('video/', views.video, name='video'), #ссылка на обработку Видео
    path('blog/', views.blog, name='blog'), #ссылка на обработку Блог
    path('newpost/', views.newpost, name='newpost'), #ссылка на обработку Новая статья
    path('(?P<parametr>\d+)/', views.blogpost, name='blogpost'), #ссылка на обработку Статья блога
    path('registration/', views.registration, name='registration'), #ссылка на обработку Регистрация
    path('games/', views.games, name='games'), #ссылка на обработку Игры
    path('orders/', views.orders, name='orders'), #ссылка на обработку Игры
    path('addticket/(?<id>\d+)/', views.addticket, name='addticket'), #ссылка на обработку кнопки Купить билет
    path('buyticket/(?<bid>\d+)/', views.buyticket, name='buyticket'), #ссылка на обработку кнопки Оплатить
    path('delticket/(?<did>\d+)/', views.delticket, name='delticket'), #ссылка на обработку кнопки Удалить
    path('login/', #обработка стандартной авторизации
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Вход',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
]

"""Для загрузки изображений"""
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()