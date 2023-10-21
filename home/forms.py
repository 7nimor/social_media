from django import forms
from account.models import Post
from .models import Comments


class PostCreateUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('body',)


class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('body',)
        widgets = {
            'body': forms.TextInput(attrs={'class': "form-control", 'id': "exampleFormControlTextarea1"}),
        }


class CommentReplyForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('body',)
        widgets = {
            'body': forms.TextInput(attrs={'class': "form-control", 'id': "exampleFormControlTextarea1"}),
        }


class SearchForm(forms.Form):
    search = forms.CharField(label='',widget=forms.TextInput(
        attrs={"class": "form-control me-2", 'type': "search", 'placeholder': "Search", 'aria-label': "Search"}))
