from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'slug', 'author', 'publish','status')#Какие поля отображаются
	list_filter = ('status', 'created', 'publish', 'author')#По каким полям фильтруется
	search_fields = ('title', 'body')#ПО каким полям можно искать
	prepopulated_fields = {'slug': ('title',)}#Какое поле заполняется автоматически и каким полем оно заполняется
	raw_id_fields = ('author',)#поле поиска 
	date_hierarchy = 'publish'# Под поиском благодаря атрибуту date_hierarchy добавлены ссылки для навигации по датам
	ordering = ('status', 'publish')#
# Register your models here.
admin.site.register(Post, PostAdmin)