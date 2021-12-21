from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.cache import cache
from django.views import View
from django.contrib.auth import views as auth
from django.http import HttpRequest
from apps.post.forms import FormularioPost
from .forms import ComentarioForm
from .models import Post, Comentario
# Create your views here.


def ListarPostPorCategoria(request, categoria):
	cache.clear()
	posts = Post.objects.filter(categoria=categoria)
	cache.set('posts', posts)
	context = { 
		'titulo': categoria,
		'posts': posts}
	return render(request,'post/base.html', context)

def ListarPostPorFecha(request, fecha):
	cache.clear()
	posts = Post.objects.filter(fecha=fecha)
	cache.set('posts', posts)
	context = {
		'titulo': fecha,
		'posts': posts
	}
	return render(request,'post/base.html', context)

def GetTopPost(request):
	cache.clear()
	posts = Post.objects.raw('SELECT pp.*, (SELECT count(*) FROM post_comentario as pc where pc.post_id = pp.id) as comentario FROM post_post as pp order by comentario desc limit 10')
	cache.set('posts', posts)
	context = {
		'titulo': 'top 10',
		'posts': posts
	}
	return render(request,'post/base.html', context)


""" class ReadPost(View):



	def get(self, request, id, *args, **kwargs):
		try:
			posts = ExistePost(id)
		except Exception:
			posts = Post.objects.get(id=id)
		comentarios = Comentario.objects.filter(post=id)
		form = ComentarioForm()
		context = {
			'titulo': 'post',
			'posts': posts,
			'form': form,
			'comentarios': comentarios
		}
		return render(request,'post/post.html', context)

	def post(self, request, id, *args, **kwargs):
		try:
			posts = ExistePost(id)
		except Exception:
			posts = Post.objects.get(id=id)
		comentarios = Comentario.objects.filter(post=id)

		form = ComentarioForm(request.POST)
		if form.is_valid():
			aux =  form.save(commit=False)
			aux.post = posts
			aux.save()
			form = ComentarioForm()

		context = {
			'titulo': 'post',
			'posts': posts,
			'form': form,
			'comentarios': comentarios
		}
		return render(request,'post/post.html', context)
 """
def ReadPost(request, id):
	try:
		posts = ExistePost(id)
	except Exception:
		posts = Post.objects.get(id=id)
	comentarios = Comentario.objects.filter(post=id)

	form = ComentarioForm(request.POST or None)
	if form.is_valid():
		if request.user.is_authenticated:
			aux =  form.save(commit=False)
			aux.post = posts
			aux.user = request.user
			aux.save()
			form = ComentarioForm()
		else:
			return redirect('usuario:login')
	
	context = {
		'titulo': 'post',
		'posts': posts,
		'form': form,
		'comentarios': comentarios
	}
	return render(request,'post/post.html', context)


def ExistePost(id):
	for i in cache.get('posts'):
		if i.id == id:
			return i
	return None


class FormularioPostView(HttpRequest):
	

	def index(request):
		post = FormularioPost()
		return render(request, "post/crearpost.html", {"form":post})

	def guardarPost(request):
		post = FormularioPost(request.POST)
		if post.is_valid():
			post.save()
			post = FormularioPost()

		return render(request, "post/crearpost.html", {"form":post, "mensaje": 'OK'})
	
	def listar_MisPost(request):
		post = Post.objects.all()#.select_related('user_id')
		return render(request, "post/ListaMisPost.html", {"post": post})

	def editPost(request, id):
		post = Post.objects.filter(id = id).first()
		form = FormularioPost(instance=post)
		return render (request, "post/PostEdit.html", {"form":form, 'post':post})

	def actualizarPost(request, id):
		post = Post.objects.get(pk = id)
		form = FormularioPost(request.POST, instance = post)
		if form.is_valid():
			form.save()
		post = Post.objects.all()
		return render(request, "post/ListaMisPost.html", {"post": post})
########################################################################
#                       views Comentario                               #
########################################################################


def AddComentario(request):
	form = ComentarioForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = ComentarioForm()
	context={
		'form': form,
	}
	return render(request,'comentario/addcomentario.html', context)

def Comentarios(request):
	return render(request,'comentario/listarcomentario.html')