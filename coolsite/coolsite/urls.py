"""coolsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from coolsite import settings
from women.views import *

from mainapp import views
from mainapp.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('base', views.ArticleViewSet, basename='article') # укажите basename при регистрации в роутере

filter_router = DefaultRouter()
filter_router.register('param', views.ArticleParamFilterView)
filter_router.register('django_filter_param', views.ArticleDjangoFilterViewSet)
filter_router.register('custom_filter_param', views.ArticleCustomDjangoFilterViewSet)

handler404 = pageNotFound

urlpatterns = [
    path('admin/', admin.site.urls),

    #women
    path('', include('women.urls')),

    #mainapp
    path('views/api-view/', views.ArticleAPIView.as_view()),
    path('article_view/', article_view),

    path('generics/create/', views.ArticleCreateAPIView.as_view()),
    path('generics/list/', views.ArticleListAPIView.as_view()),
    path('generics/retrieve/<int:pk>/', views.ArticleRetrieveAPIView.as_view()),
    path('generics/delete/<int:pk>/', views.ArticleDestroyAPIView.as_view()),
    path('generics/update/<int:pk>/', views.ArticleUpdateAPIView.as_view()),

    path('viewsets/', include(router.urls)),

    path('filters/kwargs/<str:name>/', views.ArticleKwargsFilterView.as_view()),

    path('filters/', include(filter_router.urls)),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
