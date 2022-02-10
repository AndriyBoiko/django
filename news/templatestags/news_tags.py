from django import template
from django.db.models import Count, F
from news.models import Category

register = template.Library()

@register.simple_tag(name='get_list_categories')
def get_categories():
    return Category.objects.all()
    
@register.inclusion_tag('news/iclude_tags.html')
def show_categories():
    # categories = Category.objects.all()
    # categories = Category.objects.annotate(cnt=Count('news')).filter(cnt__gt=0)
    categories = Category.objects.annotate(cnt=Count('news', filter=F('news__in_publisher'))).filter(cnt__gt=0)
    return {'categories':categories}