from django.db import models
from django.utils import timezone

# Create your models here.

# 행동에 기록되는 Tag 모음
class Tag(models.Model):
    title = models.CharField(max_length = 50)

    def __str__(self):
        return self.title

# 행동이 기록되는 테이블
class Action(models.Model):
    created_time = models.DateTimeField(default = timezone.now)
    title = models.CharField(max_length = 200)
    memo = models.TextField()
    # 어떻게 Tag가 여러 개 입력되도록 할 것인가?
    tag = models.ForeignKey(Tag, on_delete = models.SET_NULL, null=True) 
    
    def __str__(self):
        return self.title




