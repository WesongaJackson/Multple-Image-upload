from django import forms
from multiupload.fields import MultiFileField
from Main.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["images"]

    images = MultiFileField(label="Upload Images", min_num=1, max_num=10)
