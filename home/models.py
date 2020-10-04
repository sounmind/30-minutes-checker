from django.db import models
from django.utils import timezone


class Author(models.Model):
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=50, default="")

    def __str__(self):
        return self.name


# 행동에 기록되는 Tag 모음
class Tag(models.Model):
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=50, default="")

    def __str__(self):
        return self.title


# 행동이 기록되는 테이블
class Action(models.Model):
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=200)
    memo = models.TextField(blank=True)
    # Tag model이 위에 있기 때문에 문자열로 표현해야 한다.
    tag = models.ManyToManyField('Tag', blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} | Tag: {self.tag.all()} | Author: {self.author}"


class Comment(models.Model):
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)
    content = models.TextField()
    # author가 사라지면 모든 comment가 삭제됨
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    # action이 사라지면 모든 comment가 삭제됨
    action = models.ForeignKey(Action, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.content}"
