from django.forms.models import ModelForm
from .models import Action


class ActionForm(ModelForm):
    class Meta:
        model = Action
        fields = ('title', 'memo', 'tag', 'author')
