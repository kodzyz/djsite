from django import forms
from django.core.exceptions import ValidationError

from .models import *


class AddPostForm(forms.ModelForm):
    # у списка установить свойство: empty_label = "Категория не выбрана"
    def __init__(self, *args, **kwargs):  # конструктор у класса формы
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = "Категория не выбрана"  # присвоим атрибуту empty_label нужное значение
        # так же в нашей форме появились и методы базового класса - метод save()

    class Meta:
        model = Women  # связь формы с моделью
        # fields = '__all__'  # все поля # в результате увидим готовую форму
        fields = ['title', 'slug', 'content', 'photo', 'is_published', 'cat']  # рекомендуется явно указывать список полей
        widgets = {  # стили оформления для каждого поля
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10}),  # 60 колонок 10 строчек
        }
    #  пользовательские валидаторы
    def clean_title(self):  # обычные методы, имена которых начинаются с префикса clean_
        title = self.cleaned_data['title']  # считываем заголовок, переданный из формы, из словаря очищенных данных cleaned_data
        if len(title) > 200:
            raise ValidationError('Длина превышает 200 символов')

        return title
