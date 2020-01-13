from django import forms

from django_girls.blog.models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text')
