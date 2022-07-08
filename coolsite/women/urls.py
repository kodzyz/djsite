from django.urls import path
from .views import *

urlpatterns = [

    path('', index), # /women/
    path('cats/', categories), # /women/cats/

]