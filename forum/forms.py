from django import forms
from .models import ForumTopic, ForumPost

class TopicForm(forms.ModelForm):
    class Meta:
        model = ForumTopic
        fields = ['title']

class PostForm(forms.ModelForm):
    class Meta:
        model = ForumPost
        fields = ['content']
