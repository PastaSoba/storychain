from django.forms import ModelForm
from .models import Story, Storybone

class StoryForm(ModelForm):
    class Meta:
        model = Story
        fields = ['title', 'text', 'is_finish']

class StoryboneForm(ModelForm):
    class Meta:
        model = Storybone
        fields = ['starttext', 'lasttext']