from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework import filters
from .models import Article
from .serializers import ArticleSerializer


# TODO Declare a Search for News Article Then redo it in other models
class ArticleViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin, filters.SearchFilter):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    
    search_fields = ['id', 'title', 'content']
    


    
    
    
    