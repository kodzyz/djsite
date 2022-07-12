from django.urls import path
from .views import *

urlpatterns = [

    path('', index),  # /
    path('cats/<slug:cat>/', categories),  # /cats/ASCII/
    path('archive/<slug:year>/', archive),

]
