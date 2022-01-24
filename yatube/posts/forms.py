from django import forms
from .validators import clean_text
from .models import Group


class PostForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea, validators=[clean_text])
    group = forms.ChoiceField(choices=Group.objects.all, required=False)
