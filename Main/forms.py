from django import  forms

from Main.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'images']

    images = forms.FileField(
        label='Upload Images',
        widget=forms.ClearableFileInput(
            attrs={
                'class': 'form-control'
            }
        )
    )


