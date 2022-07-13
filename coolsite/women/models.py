from django.db import models


# Create your models here.
class Women(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title

# In [2]: from women.models import Women
#
# In [3]: Women(title='Анджелина Джоли', content='Биография Анджелины Джоли')
# Out[3]: <Women: Women object (None)>
#
# In [4]: w1 = _
#
# In [5]: w1
# Out[5]: <Women: Women object (None)>
#
# In [6]: w1.save()
#
# In [7]: w1
# Out[7]: <Women: Women object (1)>
#
# In [8]: w1.id
# Out[8]: 1
#
# In [9]: w1.title
# Out[9]: 'Анджелина Джоли'
#
# In [10]: w1.time_create
# Out[10]: datetime.datetime(2022, 7, 13, 17, 59, 40, 744167, tzinfo=<UTC>)
#
# In [11]: w1.pk
# Out[11]: 1
#
# In [12]: from django.db import connection
#
# In [13]: connection.queries
# Out[13]:
# [{'sql': 'INSERT INTO "women_women" ("title", "content", "photo", "time_create", "time_update", "is_published") VALUES (\'Анджел
# ина Джоли\', \'Биография Анджелины Джоли\', \'\', \'2022-07-13 17:59:40.744167\', \'2022-07-13 17:59:40.744167\', 1)',
#   'time': '0.000'}]
#
# In [14]: w2 = Women(title='Энн Хэтэуэй', content='Биография Энн Хэтэуэй')
#
# In [15]: w2.save()
#
# In [16]: connection.queries
# Out[16]:
# [{'sql': 'INSERT INTO "women_women" ("title", "content", "photo", "time_create", "time_update", "is_published") VALUES (\'Анджел
# ина Джоли\', \'Биография Анджелины Джоли\', \'\', \'2022-07-13 17:59:40.744167\', \'2022-07-13 17:59:40.744167\', 1)',
#   'time': '0.000'},
#  {'sql': 'INSERT INTO "women_women" ("title", "content", "photo", "time_create", "time_update", "is_published") VALUES (\'Энн Хэ
# тэуэй\', \'Биография Энн Хэтэуэй\', \'\', \'2022-07-13 18:09:40.162176\', \'2022-07-13 18:09:40.162176\', 1)',
#   'time': '0.000'}]
#
# In [17]: w3 = Women()
#
# In [18]: w3
# Out[18]: <Women: Women object (None)>
#
# In [19]: w3.title = 'Джулия Робертс'
#
# In [20]: w3.content = 'Биография Джулии Робертс'
#
# In [21]:  w3.save()
#
# In [22]: # objects
#
# In [23]: Women.objects
# Out[23]: <django.db.models.manager.Manager at 0x4020ba8>
#
# In [24]: w4 = Women.objects.create(title='Ума Турман', content='Биография Ума Турман')
#
# In [25]: w4.pk
# Out[25]: 4
#
# In [26]: Women.objects.create(title='Кира Найтли', content='Биография Киры Найтли')
# Out[26]: <Women: Women object (5)>
#
# In [27]: Women.objects.all()
# Out[27]: <QuerySet [<Women: Women object (1)>, <Women: Women object (2)>, <Women: Women object (3)>, <Women: Women object (4)>,
# <Women: Women object (5)>]>

# In [1]: from women.models import Women
#
# In [2]:  Women.objects.all()
# Out[2]: <QuerySet [<Women: Анджелина Джоли>, <Women: Энн Хэтэуэй>, <Women: Джулия Робертс>, <Women: Ума Турман>, <Women: Кира На
# йтли>]>
#
# In [3]: w = _
#
# In [4]: w[0]
# Out[4]: <Women: Анджелина Джоли>
#
# In [5]: w[1]
# Out[5]: <Women: Энн Хэтэуэй>
#
# In [6]: w[0].title
# Out[6]: 'Анджелина Джоли'
#
# In [7]: w[0].content
# Out[7]: 'Биография Анджелины Джоли'
#
# In [8]: len(w)
# Out[8]: 5
#
# In [9]: for wi in w:
#    ...:     print(wi.title)
#    ...:
# Анджелина Джоли
# Энн Хэтэуэй
# Джулия Робертс
# Ума Турман
# Кира Найтли
#
# In [10]:  Women.objects.filter(title='Энн Хэтэуэй')
# Out[10]: <QuerySet [<Women: Энн Хэтэуэй>]>
#
# In [11]: from django.db import connection
#
# In [12]: connection.queries
# Out[12]:
# [{'sql': 'SELECT "women_women"."id", "women_women"."title", "women_women"."content", "women_women"."photo", "women_women"."time_
# create", "women_women"."time_update", "women_women"."is_published" FROM "women_women" LIMIT 21',
#   'time': '0.000'},
#  {'sql': 'SELECT "women_women"."id", "women_women"."title", "women_women"."content", "women_women"."photo", "women_women"."time_
# create", "women_women"."time_update", "women_women"."is_published" FROM "women_women" LIMIT 1',
#   'time': '0.000'},
#  {'sql': 'SELECT "women_women"."id", "women_women"."title", "women_women"."content", "women_women"."photo", "women_women"."time_
# create", "women_women"."time_update", "women_women"."is_published" FROM "women_women" LIMIT 1 OFFSET 1',
#   'time': '0.000'},
#  {'sql': 'SELECT "women_women"."id", "women_women"."title", "women_women"."content", "women_women"."photo", "women_women"."time_
# create", "women_women"."time_update", "women_women"."is_published" FROM "women_women" LIMIT 1',
#   'time': '0.000'},
#  {'sql': 'SELECT "women_women"."id", "women_women"."title", "women_women"."content", "women_women"."photo", "women_women"."time_
# create", "women_women"."time_update", "women_women"."is_published" FROM "women_women" LIMIT 1',
#   'time': '0.000'},
#  {'sql': 'SELECT "women_women"."id", "women_women"."title", "women_women"."content", "women_women"."photo", "women_women"."time_
# create", "women_women"."time_update", "women_women"."is_published" FROM "women_women"',
#   'time': '0.000'},
#  {'sql': 'SELECT "women_women"."id", "women_women"."title", "women_women"."content", "women_women"."photo", "women_women"."time_
# create", "women_women"."time_update", "women_women"."is_published" FROM "women_women" WHERE "women_women"."title" = \'Энн Хэтэуэ
# й\' LIMIT 21',
#   'time': '0.000'}]
#
# In [13]: Women.objects.filter(pk=2)
# Out[13]: <QuerySet [<Women: Энн Хэтэуэй>]>
#
# In [14]: Women.objects.filter(pk__gte=2)
# Out[14]: <QuerySet [<Women: Энн Хэтэуэй>, <Women: Джулия Робертс>, <Women: Ума Турман>, <Women: Кира Найтли>]>
#
# In [15]: Women.objects.exclude(pk=2)
# Out[15]: <QuerySet [<Women: Анджелина Джоли>, <Women: Джулия Робертс>, <Women: Ума Турман>, <Women: Кира Найтли>]>
#
# In [16]: Women.objects.get(pk=2)
# Out[16]: <Women: Энн Хэтэуэй>
#
# In [17]: Women.objects.filter(pk__lte=4).order_by('title')
# Out[17]: <QuerySet [<Women: Анджелина Джоли>, <Women: Джулия Робертс>, <Women: Ума Турман>, <Women: Энн Хэтэуэй>]>
#
# In [18]: Women.objects.order_by('title')
# Out[18]: <QuerySet [<Women: Анджелина Джоли>, <Women: Джулия Робертс>, <Women: Кира Найтли>, <Women: Ума Турман>, <Women: Энн Хэ
# тэуэй>]>
#
# In [19]: Women.objects.order_by('-time_update')
# Out[19]: <QuerySet [<Women: Кира Найтли>, <Women: Ума Турман>, <Women: Джулия Робертс>, <Women: Энн Хэтэуэй>, <Women: Анджелина
# Джоли>]>
#
# In [20]: Women.objects.order_by('time_update')
# Out[20]: <QuerySet [<Women: Анджелина Джоли>, <Women: Энн Хэтэуэй>, <Women: Джулия Робертс>, <Women: Ума Турман>, <Women: Кира Н
# айтли>]>
#
# In [21]: wu = Women.objects.get(pk=2)
#
# In [22]: wu
# Out[22]: <Women: Энн Хэтэуэй>
#
# In [23]: wu.title = 'Марго Робби'
#
# In [24]: wu.content = 'Биография Марго Робби'
#
# In [25]: wu.save()
#
# In [26]: w2 = Women(title='Энн Хэтэуэй', content='Биография Энн Хэтэуэй')
#
# In [27]: w2.save()
#
# In [28]: wd = Women.objects.filter(pk__gte=4)
#
# In [29]: wd
# Out[29]: <QuerySet [<Women: Ума Турман>, <Women: Кира Найтли>, <Women: Энн Хэтэуэй>]>
#
# In [30]: wd.delete()

