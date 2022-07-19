from django import template
from women.models import *

# регистрация собств. шаблонных тегов
register = template.Library()


@register.simple_tag(name='getcats')
def get_categories():
    return Category.objects.all()


# включающий тег - формир. фрагмента HTML страницы
@register.inclusion_tag('women/list_categories.html')
def show_categories():
    cats = Category.objects.all()
    return {"cats": cats}  # "cats" будет передаваться шаблону 'women/list_categories.html'
