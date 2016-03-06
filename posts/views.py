from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from .forms import PostForm
from .models import Post

def post_home(request):
	queryset = Post.objects.all()
	context = {
		"obj_list": queryset, 
		"title": "Home"
	}
	return render(request, "index.html", context)

def post_create(request):
	form = PostForm(request.POST)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()

	context = {
		"form": form
	}
	return render(request, "post_form.html", context)

def post_delete(request):
	return HttpResponse("<h1>post_delete</h1>")
