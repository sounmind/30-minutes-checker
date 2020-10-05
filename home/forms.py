from django.forms.models import ModelForm
from .models import Action, Tag


class ActionForm(ModelForm):
    class Meta:
        model = Action
        fields = ('title', 'memo', 'tag', 'author')
        # 태그 추가도 가능하게 해야 함


class SettingForm(ModelForm):
    class Meta:
        pass
    pass


class TagForm(ModelForm):
    class Meta:
        model = Tag
        fields = '__all__'
