from django.db import models
from django.urls import reverse


# Create your models here.


class Women(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    content = models.TextField(blank=True, verbose_name='Текст статьи')
    photo = models.ImageField(upload_to="photos/%Y/%m/%d", verbose_name='Фото')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категории')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'Известные женщины'
        verbose_name_plural = 'Известные женщины'
        #ordering = ['-time_create', 'title']


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Категория')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']


# from women.models import *
# Women.objects.all()
# Women.objects.all()[:3]
# from django.db import connection
# connection.queries
# Women.objects.all()[3:8]
# Women.objects.order_by('pk')
# Women.objects.all().reverse()
# Women.objects.filter(pk__lte=2)  # __lte <=, __gte >=
# Women.objects.get(pk=2)

# In [15]: w = Women.objects.get(pk=1)
# In [16]: w.cat
# Out[16]: <Category: Актрисы>
# In [17]: w.cat.name
# Out[17]: 'Актрисы'

# In [22]: Women.objects.filter(pk__gt=13) # >=
# Out[22]: <QuerySet [<Women: fhfhfh hgfhfh>]>

# In [24]: Women.objects.filter(title__contains='ли')  # фрагмент в строке
# Out[24]: <QuerySet [<Women: Анастасия Эшли>, <Women: Джулия Робертс>, <Women: Анджелина Джоли>]>
#
# In [26]: Women.objects.filter(pk__in=[2,5,11,12])
# Out[26]: <QuerySet [<Women: енгегнкеуке>, <Women: Ариана Гранде>, <Women: Ума Турман>, <Women: Дженнифер Лоуренс>]>
# In [27]: Women.objects.filter(pk__in=[2,5,11,12], is_published=True)
# In [29]: Women.objects.filter(cat__in=[1, 2])
# In [30]: Women.objects.filter(cat_id__in=[1, 2])
# In [31]: cats = Category.objects.all()
# In [32]: Women.objects.filter(cat__in=cats)

# In [34]: from django.db.models import Q
#
# In [35]: Women.objects.filter(pk__lt=5, cat_id=2)
# Out[35]: <QuerySet []>
# In [36]: Women.objects.filter(Q(pk__lt=5) | Q(cat_id=2))  # ИЛИ
#
# In [37]: Women.objects.filter(Q(pk__lt=5) & Q(cat_id=2))  # И
# Out[37]: <QuerySet []>
# In [38]: Women.objects.filter(~Q(pk__lt=5) | Q(cat_id=2))  # НЕ(<=) >= # ИЛИ

# In [39]: Women.objects.first()
# Out[39]: <Women: fhfhfh hgfhfh>
# In [40]: Women.objects.order_by('pk').first()
# Out[40]: <Women: Анджелина Джоли>
# In [41]: Women.objects.order_by('-pk').first()
# Out[41]: <Women: fhfhfh hgfhfh>
# In [43]: Women.objects.order_by('-pk').last()
# Out[43]: <Women: Анджелина Джоли>

# In [44]: Women.objects.latest('time_update')
# Out[44]: <Women: fhfhfh hgfhfh>
# In [45]: Women.objects.earliest('time_update')
# Out[45]: <Women: Анджелина Джоли>
# In [46]: Women.objects.order_by('title').earliest('time_update')
# Out[46]: <Women: Анджелина Джоли>

# In [47]: w = Women.objects.get(pk=7)
# In [48]: w
# Out[48]: <Women: Бейонсе>
# In [49]: w.get_previous_by_time_update()
# Out[49]: <Women: Кэтти Перри>
# In [50]: w.get_next_by_time_update()
# Out[50]: <Women: Ариана Гранде>
# In [51]: w.get_next_by_time_update(pk__gt=10)  # следующая запись с условием >=10
# Out[51]: <Women: fhfhfh hgfhfh>

# In [52]: Category.objects.create(name='Спортсменки', slug='sportsmenky')
# Out[52]: <Category: Спортсменки>
# In [56]: c3 = Category.objects.get(pk=3)
# In [57]: c3
# Out[57]: <Category: Спортсменки>
# In [58]: c3.women_set.exists()
# Out[58]: False
# In [59]: c2 = Category.objects.get(pk=2)
# In [60]: c2
# Out[60]: <Category: Певицы>
# In [61]: c2.women_set.exists()
# Out[61]: True
# In [62]: c2.women_set.count()
# Out[62]: 6
# In [63]: c3.women_set.count()
# Out[63]: 0
# In [64]: Women.objects.filter(pk__gt=4).count()
# Out[64]: 10

# In [65]: Women.objects.filter(cat__slug='aktrisy')
# In [66]: Women.objects.filter(cat__in=[1])
# In [67]: Women.objects.filter(cat__name='Певицы')
# In [70]: Women.objects.filter(cat__name__contains='ки')
# Out[70]: <QuerySet []>
# In [72]: Category.objects.filter(women__title__contains='ли').distinct() # уникальные категории
# Out[72]: <QuerySet [<Category: Актрисы>, <Category: Певицы>]>

# агрегирующие функции
# In [2]:  Women.objects.count()
# Out[2]: 14
# In [8]: from django.db.models import *
# In [9]: Women.objects.aggregate(Min('cat_id'))
# Out[9]: {'cat_id__min': 1}
# In [10]: Women.objects.aggregate(Min('cat_id'), Max('cat_id'))
# Out[10]: {'cat_id__min': 1, 'cat_id__max': 2}
# In [11]: Women.objects.aggregate(cat_min=Min('cat_id'), cat_max=Max('cat_id'))
# Out[11]: {'cat_min': 1, 'cat_max': 2}
# In [12]: Women.objects.aggregate(res=Sum('cat_id') - Count('cat_id'))
# Out[12]: {'res': 6}
# In [13]: Women.objects.aggregate(Avg('cat_id'))
# Out[13]: {'cat_id__avg': 1.4285714285714286}
# In [14]: Women.objects.filter(pk__gt=4).aggregate(res=Avg('cat_id'))
# Out[14]: {'res': 1.6}

# In [15]: Women.objects.values('title', 'cat_id').get(pk=1)
# Out[15]: {'title': 'Анджелина Джоли', 'cat_id': 1}
# In [16]: Women.objects.values('title', 'cat__name').get(pk=1)
# Out[16]: {'title': 'Анджелина Джоли', 'cat__name': 'Актрисы'}
# In [18]: w = Women.objects.values('title', 'cat__name')
# In [20]: for p in w:
#     ...:     print(p['title'], p['cat__name'])
#     ...:

# группировка и агрегация
# In [4]: Women.objects.values('cat_id').annotate(Count('id'))
# Out[4]: <QuerySet [{'cat_id': 1, 'id__count': 8}, {'cat_id': 2, 'id__count': 6}]>
#
# c = Category.objects.annotate(Count('women'))
# In [6]: c
# Out[6]: <QuerySet [<Category: Актрисы>, <Category: Певицы>, <Category: Спортсменки>]>
# In [8]: c[0].women__count
# Out[8]: 8
# In [9]: c[1].women__count
# Out[9]: 6
# In [14]: c[2].women__count
# Out[14]: 0
# In [15]: c = Category.objects.annotate(total=Count('women'))
# In [16]: c[0].total
# Out[16]: 8
# In [17]: len(c)
# Out[17]: 3
# In [18]:  c = Category.objects.annotate(total=Count('women')).filter(total__gt=0)
# In [19]: c
# Out[19]: <QuerySet [<Category: Актрисы>, <Category: Певицы>]>

# class F
# In [20]: from django.db.models import F
# In [21]: Women.objects.filter(pk__gt=F('cat_id')) # id > cat_id
# In [22]: Women.objects.filter(slug='bejonse').update(views=F('views')+1)
# In [22]: w = Women.objects.get(pk=1)
# In [23]: w
# Out[23]: <Women: Анджелина Джоли>
# In [24]: w.views = F('views')+1
# In [25]: w.save()

#функции
# In [26]: from django.db.models.functions import Length
# In [27]: ps = Women.objects.annotate(len=Length('title'))
# In [28]: for item in ps:
#     ...:     print(item.title, item.len)
#     ...:
# Анджелина Джоли 15
# Дженнифер Лоуренс 17
# Джулия Робертс 14
# Марго Робби 11
# Ума Турман 10
# Ариана Гранде 13
# Бейонсе 7
# Кэтти Перри 11
# Рианна 6
# Шакира 6
# Ариана Гранде 13
# енгегнкеуке 11
# Анастасия Эшли 14
# fhfhfh hgfhfh 13

#raw
# In [29]: Women.objects.raw('SELECT * FROM women_women')
# Out[29]: <RawQuerySet: SELECT * FROM women_women>
# In [30]: w = _
# In [31]: for p in w:
#     ...:     print(p.pk, p.title)
# 1 Анджелина Джоли
# 2 Дженнифер Лоуренс
# 3 Джулия Робертс
# 4 Марго Робби
# 5 Ума Турман
# 6 Ариана Гранде
# 7 Бейонсе
# 8 Кэтти Перри
# 9 Рианна
# 10 Шакира
# 11 Ариана Гранде
# 12 енгегнкеуке
# 13 Анастасия Эшли
# 14 fhfhfh hgfhfh

# In [32]: from django.db import reset_queries
# In [33]: reset_queries()
# In [34]: connection.queries
# Out[34]: []
# In [35]: w = Women.objects.raw('SELECT * FROM women_women')
# In [36]: connection.queries
# Out[36]: []  # неодного SQL запроса
# In [37]: w[0]
# Out[37]: <Women: Анджелина Джоли>
# In [38]: connection.queries
# Out[38]: [{'sql': 'SELECT * FROM women_women', 'time': '0.016'}]
# In [39]: w = Women.objects.raw('SELECT id, title FROM women_women') # поле id обязательно
# In [40]: w[0].is_published
# Out[40]: True
# #передаем параметры в запрос
# In [41]: Women.objects.raw("SELECT id, title FROM women_women WHERE slug='shakira'")
# Out[41]: <RawQuerySet: SELECT id, title FROM women_women WHERE slug='shakira'>
# In [42]: slug='shakira'
# In [43]: Women.objects.raw("SELECT id, title FROM women_women WHERE slug='" + slug +"'")
# Out[43]: <RawQuerySet: SELECT id, title FROM women_women WHERE slug='shakira'>
# #безопасный путь
# In [44]: Women.objects.raw("SELECT id, title FROM women_women WHERE slug='%s'", [slug])
# Out[44]: <RawQuerySet: SELECT id, title FROM women_women WHERE slug='shakira'>































