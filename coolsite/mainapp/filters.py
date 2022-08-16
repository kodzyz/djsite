# Если, кроме указания полей,
# необходимо настроить их отображение и тип, то сначала создаём
# фильтр:

from django_filters import rest_framework as filters
from .models import Article


class ArticleFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='contains') # к фильтру в поле name нужно добавить contains для поиска по части имени

    class Meta:
        model = Article
        fields = ['name']
