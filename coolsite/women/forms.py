from django import forms
from .models import *


class AddPostForm(forms.Form):
    title = forms.CharField(max_length=255, label='Заголовок')  # атрибут label, который и позволяет задавать свои имена
    slug = forms.SlugField(max_length=255, label='URL')
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}), label='Контент',
                              required=False)  # сделаем поле content необязательным
    is_published = forms.BooleanField(label='Публикация', initial=True)  # поле is_published с установленной галочкой
    cat = forms.ModelChoiceField(queryset=Category.objects.all(), label='Категории',
                                 empty_label='Категория не выбрана')  # фраза вместо черточек
