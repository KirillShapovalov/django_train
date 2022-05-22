from django.db import models
from django.utils.timezone import now


class Article(models.Model):
    title = models.CharField('Название статьи', max_length=200)
    text = models.TextField('Текст статьи')
    pub_date = models.DateTimeField('Дата публикации', default=now)


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author = models.CharField('Имя автора', max_length=50)
    text = models.CharField('Текст комментария', max_length=200)
