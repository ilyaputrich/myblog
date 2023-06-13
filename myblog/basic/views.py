from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.views.generic import ListView
from .models import Post
from .form import CommentsForm


class PostView(View):
    "Вывод записей"
    def get(self, request):
        posts = Post.objects.all()
        return render(request, "basic/basic.html", {"post_list": posts})

class PostDetail(View):
    "отдельная страница записи"
    def get(self, request, pk):
        post = Post.objects.get(id=pk)
        return render(request, "basic/blog_detail.html", {"post": post})
class AddComments(View):
    "добавление коментариев"
    def post(self, request, pk):
        form = CommentsForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.post_id = pk
            form.save()
        return redirect(f"/{pk}")

class Search(View):
    "Вывод записей"
    def get(self, request):
        posts = Post.objects.filter(title__contains=self.request.GET.get("search"))
        return render(request, "basic/basic.html", {"post_list": posts})

