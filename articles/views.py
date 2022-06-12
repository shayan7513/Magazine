from django.shortcuts import render
from django.contrib.auth.models import User
from django.core.cache import cache

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.parsers import FormParser, MultiPartParser
from .serializers import ArticleSerializers, CommentSerializers, UserSerializers
from .models import Article, Comment


class UserViewSet(ModelViewSet):
    def get_queryset(self):
        if cache.get('queryset'):
            queryset = cache.get('queryset')
        else:
            queryset = User.objects.all()
            cache.set('queryset', queryset, 4 * 60)
        return queryset

    def get_serializer_class(self):
        return UserSerializers

  

class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.select_related('related_user').all()
    serializer_class = ArticleSerializers
    permission_classes = [IsAuthenticated]
    parser_classes = [FormParser, MultiPartParser]

class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.filter(is_active=True)
    serializer_class = CommentSerializers