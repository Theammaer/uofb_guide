from django.shortcuts import render
from django.views.generic import View
from rest_framework.response import Response
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.filters import SearchFilter
from django_filters.rest_framework.backends import DjangoFilterBackend
from .filters import TopicFilter

from .models import Chapter, GuideTopic
from .serializers import ChapterSerializer, GuideTopicSerializer


class GuideViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin, SearchFilter):
    serializer_class = GuideTopicSerializer
    queryset = GuideTopic.objects.all() #filter(chapter__number=1) # Filter to return topics with specific chapter number
    authentication_classes = []
    filter_backends = [TopicFilter, ]
    
    # search_fields = ['id', 'title', 'content', 'chapter__name']
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)   


class ChaptersViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    serializer_class = ChapterSerializer
    queryset = Chapter.objects.all()
    authentication_classes = []
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
    
    
class WebIndex(View):
    def get(self, request):
        return render(request, 'index.html')