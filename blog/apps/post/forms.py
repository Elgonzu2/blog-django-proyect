from django import forms
from .models import Comentario, Post


class ComentarioForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['comentario'].widget.attrs.update({'rows': '3'})

    class Meta:
        model = Comentario
        fields = ['comentario']
        exclude = ['post']


class FormularioPost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'texto', 'categoria', 'image']

