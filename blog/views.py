
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.views import View
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Post, Comment
from .forms import RegistrationForm, CommentForm


# Create your views here.
class UserCreateView(CreateView):
    model = User
    form_class = RegistrationForm
    template_name = "registration/register.html"
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.set_password(form.cleaned_data['password'])
        self.object.save()
        return super().form_valid(form)


# Post CRUD Views here
class PostListView(ListView):
    model = Post
    template_name = "blog/home.html"
    context_object_name = "posts"


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/detail.html"
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comment_form"] = CommentForm()
        return context


class PostCreateView(CreateView, LoginRequiredMixin):
    model = Post
    template_name = "blog/new.html"
    fields = ["title", "body"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        response = super().form_valid(form)
        return response


class PostDeleteView(DeleteView, LoginRequiredMixin):
    model = Post
    template_name = "blog/delete.html"
    context_object_name = "post"
    success_url = reverse_lazy("post-list")


class PostUpdateView(UpdateView, LoginRequiredMixin):
    model = Post
    template_name = "blog/update.html"
    fields = ["title", "body"]


# Comment CRUD Views here
class CommentCreateView(View):
    http_method_names = ['post'] # allow only post requests

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment.objects.create(
                user=request.user,
                post=Post.objects.get(id=int(kwargs["pk"])),
                body=form.cleaned_data["body"]
            )
            comment.save()
        return redirect(reverse_lazy('post-detail', args=[str(kwargs["pk"])]))
