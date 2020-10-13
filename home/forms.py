from django.forms.models import ModelForm
from .models import Action, Tag, Comment


class ActionForm(ModelForm):
    class Meta:
        model = Action
        fields = ["author", "title", "tag", "memo"]
        # 태그 추가도 가능하게 해야 함


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ["content", "author"]
        # 어떤 행동에 대한 댓글인지 자동으로 입력이 되어야 함


class SettingForm(ModelForm):
    class Meta:
        pass

    pass


class TagForm(ModelForm):
    class Meta:
        model = Tag
        fields = "__all__"
