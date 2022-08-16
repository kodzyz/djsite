from django.shortcuts import render
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
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
#создавать набор данных и прописывать методы
from  rest_framework import viewsets
from django.shortcuts import get_object_or_404
#Доп. действия
from rest_framework.decorators import action
#Custom ViewSet
from rest_framework import mixins

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

class ArticleViewSet(viewsets.ViewSet): #обработка сразу нескольких REST-запросов #использовать Router
    renderer_classes = [JSONRenderer]
    # свой метод
    @action(detail=True, methods=['get']) # выдавать не всю информацию , а только её текст
    def article_text_only(self, request, pk=None):
        article = get_object_or_404(Article, pk=pk)
        return Response({'article.text': article.text}) # /viewsets/base/1/article_text_only/

    def list(self, request): #get-набора данных
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data) #/viewsets/base/

    def retrieve(self, request, pk=None): # get-информации об одном объекте
        article = get_object_or_404(Article, pk=pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data) #/viewsets/base/1/

class ArticleModelViewSet(viewsets.ModelViewSet): # все REST API-запросы
    queryset = Article.objects.all()
    renderer_classes = [JSONRenderer]
    serializer_class = ArticleSerializer

class ArticleCustomViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin,
                            mixins.ListModelMixin, viewsets.GenericViewSet): #GenericViewSet + нужные классы примеси для запросов REST API #через Router
    queryset = Article.objects.all()
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    serializer_class = ArticleSerializer

class ArticleQuerysetFilterViewSet(viewsets.ModelViewSet): #актуально и для других Views и Viewset
    serializer_class = ArticleSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = Article.objects.all()

    def get_queryset(self): #переопределив get_queryset, можем пользоваться методом filter
        return Article.objects.filter(name__contains='python') #фильтруем- имя должно содержать слово python

class ArticleKwargsFilterView(ListAPIView):
    serializer_class = ArticleSerializer
# вводить данные для фильтрации через url
    def get_queryset(self):
        name = self.kwargs['name'] # берётся по ключу
        return Article.objects.filter(name__contains=name)

class ArticleParamFilterView(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get_queryset(self):
        name = self.request.query_params.get('name','')
        articles = Article.objects.all()
        if name:
            articles = articles.filter(name__contains=name)
        return articles  #/filters/param/?name=name #GET, POST











