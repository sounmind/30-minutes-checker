from django.db import models
from django.utils import timezone

# 행동에 기록되는 Tag 모음


class Tag(models.Model):
    title = models.CharField(max_length=50, null=True, default="Default Tag")
    # created_time = models.DateTimeField( auto_now_add=True, primary_key=True, default=timezone.now)

    def __str__(self):
        return self.title


# 행동이 기록되는 테이블


class Action(models.Model):
    created_time = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=200)
    memo = models.TextField()
    # 어떻게 Tag가 여러 개 입력되도록 할 것인가?
    # on_delete=models.SET_NULL 일 때, Tag 테이블에서 해당 Tag가 삭제되면 default 값이 아니라 'None'이라고 된다.
    # on_delete=models.SET_DEFAULT 일 때, Tag 테이블에서 해당 Tag가 삭제되면, default 값인 No Tag가 생성되길 예상했는데, ValueError at /admin/home/tag/4/delete/ Field 'id' expected a number but got 'No tag'. 오류 발생한다.
    # on_delete=models.SET_DEFAULT = 0 일 때, Tag 테이블에서 Action에 있는 Tag를 삭제할 때 오류 발생, FOREIGN KEY constraint failed
    # 내 예측대로라면, Tag가 default 값으로 변경될 때, Tag의 primary key에 접근해서 변경하려는 것으로 간주되어 오류가 발생하는 듯 하다.
    tag = models.ForeignKey(Tag, on_delete=models.SET_DEFAULT,
                            null=True, default="Deleted")

    def __str__(self):
        return f"{self.title} | Tag: {self.tag}"
