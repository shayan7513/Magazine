from distutils.command.upload import upload
from django.db.models import Model, CharField, TextField, BooleanField, ForeignKey, CASCADE, ManyToManyField, ImageField
from django.contrib.auth.models import User



class Article(Model):
    title = CharField(max_length=128)
    description = TextField()
    content = TextField()
    is_active = BooleanField(default=True)
    related_user = ForeignKey(User, on_delete=CASCADE, related_name='article_related_user')
    authors = ManyToManyField(User)
    image = ImageField(upload_to='article_images')

    def __str__(self):
        return self.title

class Comment(Model):
    content = TextField()
    related_article = ForeignKey(Article, on_delete=CASCADE)
    related_user = ForeignKey(User, on_delete=CASCADE)
    is_active = BooleanField(default=True)

    def __str__(self):
        return self.content