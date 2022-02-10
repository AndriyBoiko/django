from django.db import models
from django.db.models.deletion import PROTECT
from django.db.models.fields import CharField
from django.urls import reverse

class News(models.Model):
    title = models.CharField(max_length=200, verbose_name = 'Новина')
    content = models.TextField(blank=True, verbose_name = 'Контент')
    created_at = models.TimeField(auto_now_add=True, verbose_name = 'Дата Публікації')
    upload_at = models.TimeField(auto_now=True, verbose_name = 'Обновлено')
    photo = models.ImageField(upload_to='photo/%Y/%m/%d/', verbose_name = 'Фото', blank=True)
    in_publisher = models.BooleanField(default=True, verbose_name = 'Опубліковано')
    category = models.ForeignKey('Category', on_delete=PROTECT) # ключ звязки таблиць нул дає можливість створити звязок коли є вже записи в таблиці
    views = models.IntegerField(default = 0)
    
    def get_absolute_url(self):
        return reverse('view_news', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Новина'
        verbose_name_plural = 'Новини'
        ordering = ['-created_at']

class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True,verbose_name = 'Категорії Новин' )


    def get_absolute_url(self):
        return reverse('category', kwargs={'category_id': self.pk})

    def __str__(self):
        return self.title #строкове представлення а не object
    class Meta:
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'
        ordering = ['title']
