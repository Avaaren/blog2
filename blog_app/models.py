from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class PublishedManager(models.Manager):#Свой менеджер запросов к модели
	def get_queryset(self):
		return super().get_queryset().filter(status='published')

class Post(models.Model):
	STATUS_CHOICES = (
	('draft', 'Draft'),
	('published', 'Published'),
	)

	title = models.CharField(max_length=250)
	slug = models.SlugField(max_length=250,unique_for_date='publish')
	author = models.ForeignKey(User,on_delete=models.CASCADE,
	related_name='blog_posts')

	body = models.TextField()
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)#автоматически при создании объекта
	updated = models.DateTimeField(auto_now=True)#Автоматически при сохранении объекта
	status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')#список определенных значений

	objects = models.Manager()#Чтобы делать запросы к бд как обычно
	published = PublishedManager()#Модифицированный менеджер запросов

# 	Мы можем использовать URL post_detail, о котором речь шла в предыдущем
# разделе, для построения канонического URL’а для объектов Post. В Django есть
# соглашение о том, что метод модели get_absolute_url() должен возвращать канонический URL объекта. 
# Для реализации этого поведения мы будем использовать функцию reverse(), которая дает возможность получать URL, указав имя
# шаблона и параметры. Добавьте следующий фрагмент в файл models.py:
	def get_absolute_url(self):
		return reverse('blog:post_detail', args=[self.publish.year,
		self.publish.month, self.publish.day, self.slug])


	class Meta:
		ordering = ('-publish',)

	def __str__(self):
		return self.title