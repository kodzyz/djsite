from django import forms
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
        fields = ['title', 'slug', 'content', 'is_published', 'cat']  # рекомендуется явно указывать список полей
        widgets = {  # стили оформления для каждого поля
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10}),  # 60 колонок 10 строчек
        }
