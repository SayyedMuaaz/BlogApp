from django import forms
from .models import Article

class ArtileForm(forms.ModelForm):
    title = forms.CharField(max_length=200)
    content = forms.Textarea()
    active = forms.BooleanField()

    class Meta:
        model = Article
        fields = [
            'title',
            'content',
            'active'
        ]