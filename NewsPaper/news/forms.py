from django import forms
from django.core.exceptions import ValidationError
from django.views.generic import CreateView

from .models import Post


class PostForm(forms.ModelForm):
   description = forms.CharField(min_length=20)
   class Meta:
       model = Post
       fields = ['title', 'description', 'author']

   def clean(self):
       cleaned_data = super().clean()
       description = cleaned_data.get("description")
       title = cleaned_data.get("title")
       author = cleaned_data.get("author")

       if title == description:
           raise ValidationError(
               "Описание не должно быть идентично названию."
           )
       return cleaned_data

class PostCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.categoryType = 'NEWS'
        return super().form_valid(form)

class ArticlesCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'articles_edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.categoryType = 'ARTICLE'
        return super().form_valid(form)

