from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from .models import Article
from .serializers import ArticleSerializer
from rest_framework.response import Response  # из DRF
#  APIView базовый класс для Views в DRF
from rest_framework.views import APIView
#@api_view
from rest_framework.decorators import api_view, renderer_classes
#При добавлении некоторых классов примесей (mixins) и использования GenericAPIView можно
#получить конкретные классы для той или иной задачи (REST-запроса)
from  rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView

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

class ArticleCreateAPIView(CreateAPIView): #  метод post
    renderer_classes = [JSONRenderer]
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ArticleListAPIView(ListAPIView): #  метод get  список данных
    renderer_classes = [JSONRenderer]
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ArticleRetrieveAPIView(RetrieveAPIView): # метод get об одном объекте требуется pk
    renderer_classes = [JSONRenderer]
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ArticleDestroyAPIView(DestroyAPIView): #  метод delete по pk
    renderer_classes = [JSONRenderer]
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ArticleUpdateAPIView(UpdateAPIView): #   put и patch по pk
    renderer_classes = [JSONRenderer]
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer




