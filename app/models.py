from django.db import models
from datetime import datetime
from django.contrib import admin
from django.urls import reverse
from django.contrib.auth.models import User

#Модель Блог
class Blog(models.Model):
    title = models.CharField(max_length = 100, unique_for_date = "posted", verbose_name = "Заголовок")
    description = models.TextField(verbose_name = "Краткое содержание")
    content = models.TextField(verbose_name = "Полное содержание")
    author = models.ForeignKey(User, null=True, blank=True, on_delete = models.SET_NULL, verbose_name = "Автор")
    posted = models.DateTimeField(default = datetime.now(), db_index = True, verbose_name = "Опубликована")
    image = models.FileField(default = 'temp.jpg', verbose_name ="Путь к изображению") #Для загрузки изображения

    def get_absolute_url(self):
        return reverse("blogpost", args=[str(self.id)])

    def _str_(self):
        return self.title

    class Meta:
        db_table = "Posts"
        ordering = ["-posted"]
        verbose_name = "Статья блога"
        verbose_name_plural = "Статья Блога"

#Модель Комментарий
class Comment(models.Model):
    text = models.TextField(verbose_name = "Комментарий")
    date = models.DateTimeField(default = datetime.now(), db_index = True, verbose_name = "Дата")
    author = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name = "Автор")
    post = models.ForeignKey(Blog, on_delete = models.CASCADE, verbose_name = "Статья")

    def _str_(self):
        return 'Комментарий %s к %s' % (self.author, self.post)

    class Meta:
        db_table = "Comments"
        ordering = ["-date"]
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарий к статьям блога"

#Модель Игры
class Games(models.Model):
    title = models.CharField(max_length = 100, unique_for_date = "posted", verbose_name = "Название")
    description = models.TextField(verbose_name = "Описание")
    posted = models.DateTimeField(default = datetime.now(), db_index = True, verbose_name = "Дата выхода")
    image = models.FileField(default = 'temp.jpg', verbose_name ="Баннер")

    def get_absolute_url(self):
        return reverse("game", args=[str(self.id)])

    def _str_(self):
        return self.title

    class Meta:
        db_table = "Games"
        ordering = ["-posted"]
        verbose_name = "Игра"
        verbose_name_plural = "Игра"

#Модель Корзина
class Orders(models.Model):
    date = models.DateTimeField(default = datetime.now(), db_index = True, verbose_name = "Дата покупки")
    author = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name = "Покупатель")
    post = models.ForeignKey(Games, on_delete = models.CASCADE, verbose_name = "Игра")
    ready = models.BooleanField(default=False, verbose_name = "Оплачено")

    def _str_(self):
        return 'Покупка игры %s от %s' % (self.post, self.author)

    class Meta:
        db_table = "Orders"
        ordering = ["-date"]
        verbose_name = "Корзина"
        verbose_name_plural = "Корзина"

#Отображение моделей в административном разделе
admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(Games)
admin.site.register(Orders)