from django.urls import path
from blog_app import views

app_name = 'blog'#Создам нейм спейс чтобы обращаться из любого уровня программы

urlpatterns = [
    path('', views.post_list, name = 'post_list'),
    path('tag/<slug:tag_slug>/', views.post_list, name = 'post_list_by_tag'),
    path('<int:year>/<int:month>/<int:day>/<int:pk>/<slug:post>/', views.post_detail, name = 'post_detail'),
    path('<int:post_id>/share/', views.post_share, name='post_share'),
    path('post/new/', views.post_new, name = 'post_new'), 
]