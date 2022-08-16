from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from .models import Article
from .serializers import ArticleSerializer
from rest_framework.response import Response  # из DRF
#  APIView базовый класс для Views в DRF
from rest_framework.views import APIView

class ArticleAPIView(APIView):
    renderer_classes = [JSONRenderer]  #список Renderers

    def get(self, request, format=None): #отвечает за get-запрос
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True) #преобразуем выборку в простые типы данных
        return Response(serializer.data)  # возвращаем объект Response
