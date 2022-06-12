from django.contrib.auth.models import User

from rest_framework.serializers import ModelSerializer
from .models import Article, Comment


class UserSerializers(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class UserMiniSerializers(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name']


class ArticleSerializers(ModelSerializer):
    related_user = UserMiniSerializers(read_only=True)
    authors = UserMiniSerializers(many=True, read_only=True)
    class Meta:
        model = Article
        fields = '__all__'

class CommentSerializers(ModelSerializer):
    related_article = ArticleSerializers(read_only=True)
    related_user = UserMiniSerializers(read_only=True)
    class Meta:
        model = Comment
        fields = '__all__'