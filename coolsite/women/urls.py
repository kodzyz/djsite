from django.urls import path
from .views import *

urlpatterns = [

    path('home/', index, name='home'),  # уникальное имя для URL
    path('cats/<slug:cat>/', categories),  # /cats/ASCII/
    path('archive/<slug:year>/', archive),

]
