from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

app_name="post"

urlpatterns = [
    path('listarCategoria/<str:categoria>', views.ListarPostPorCategoria, name="listarCategoria"),
    re_path(r'^listarFecha/(?P<fecha>[0-9]{4}-?[0-9]{2}-?[0-9]{2})', views.ListarPostPorFecha, name="postFecha"),
    path('addcomentario/', views.AddComentario, name="addcomentario"),
    path('toppost/', views.GetTopPost, name='toppost'),
    path('readpost/<int:id>', views.ReadPost, name="readpost"),
    path('comentarios/', views.Comentarios, name="comentarios"),
    path('crearpost/', views.FormularioPostView.index, name="crearpost"),
    path('guardarpost/', views.FormularioPostView.guardarPost, name="guardarpost"),
]