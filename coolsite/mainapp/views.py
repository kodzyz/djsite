from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from .models import Article
from .serializers import ArticleSerializer
from rest_framework.response import Response  # из DRF
#  APIView базовый класс для Views в DRF
from rest_framework.views import APIView
#@api_view
from rest_framework.decorators import api_view, renderer_classes

class ArticleAPIView(APIView):
    renderer_classes = [JSONRenderer]  #список Renderers

    def get(self, request, format=None): #отвечает за get-запрос
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True) #преобразуем выборку в простые типы данных
        return Response(serializer.data)  # возвращаем объект Response

@api_view(['GET']) #Для указания доступных запросов
@renderer_classes([JSONRenderer]) # а для Renderers
def article_view(request):
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)