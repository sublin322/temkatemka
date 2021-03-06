# Generated by Django 2.2.16 on 2021-02-25 08:56

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique_for_date='posted', verbose_name='Заголовок')),
                ('description', models.TextField(verbose_name='Краткое содержание')),
                ('content', models.TextField(verbose_name='Полное содержание')),
                ('posted', models.DateTimeField(db_index=True, default=datetime.datetime(2021, 2, 25, 11, 56, 52, 965463), verbose_name='Опубликована')),
                ('image', models.FileField(default='temp.jpg', upload_to='', verbose_name='Путь к изображению')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Статья блога',
                'verbose_name_plural': 'Статья Блога',
                'db_table': 'Posts',
                'ordering': ['-posted'],
            },
        ),
        migrations.CreateModel(
            name='Games',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique_for_date='posted', verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('posted', models.DateTimeField(db_index=True, default=datetime.datetime(2021, 2, 25, 11, 56, 52, 966461), verbose_name='Дата выхода')),
                ('image', models.FileField(default='temp.jpg', upload_to='', verbose_name='Баннер')),
            ],
            options={
                'verbose_name': 'Игра',
                'verbose_name_plural': 'Игра',
                'db_table': 'Games',
                'ordering': ['-posted'],
            },
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(db_index=True, default=datetime.datetime(2021, 2, 25, 11, 56, 52, 966461), verbose_name='Дата покупки')),
                ('ready', models.BooleanField(default=False, verbose_name='Оплачено')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Покупатель')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Games', verbose_name='Игра')),
            ],
            options={
                'verbose_name': 'Корзина',
                'verbose_name_plural': 'Корзина',
                'db_table': 'Orders',
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Комментарий')),
                ('date', models.DateTimeField(db_index=True, default=datetime.datetime(2021, 2, 25, 11, 56, 52, 965463), verbose_name='Дата')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Blog', verbose_name='Статья')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарий к статьям блога',
                'db_table': 'Comments',
                'ordering': ['-date'],
            },
        ),
    ]
