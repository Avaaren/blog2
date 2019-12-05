from django.db.models import Count
from django import template
from ..models import Post

register = template.Library()


@register.simple_tag
def total_posts():
    return Post.published.count()


@register.inclusion_tag('blog_app/post/latest_posts.html')
def show_latest_posts(count=5):
    latest_posts = Post.published.order_by('-publish')[:count]
    return {'latest_posts': latest_posts}


@register.inclusion_tag('blog_app/post/most_commented.html')
def get_most_commented_posts(count=5):
    most_commented = Post.published.annotate(total_comments=Count('comments')).order_by('-total_comments')[:count]#most_commented[0].total_comments
    return {'most_commented':most_commented}
    #annotate добавляет к каждой строке колво комментариев а потом идет упорядочение по этому полю      