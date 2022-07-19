from django import template
from women.models import *

# регистрация собств. шаблонных тегов
register = template.Library()


# делаем ф-ю простым тегом
@register.simple_tag()  # связывание ф-и с тегом декоратором
def get_categories():  # ф-я для работы простого тега
    return Category.objects.all()
