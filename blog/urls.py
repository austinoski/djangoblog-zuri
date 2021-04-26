
from django.urls import path

from .views import PostListView, PostDetailView, PostCreateView, PostDeleteView,\
    PostUpdateView, UserCreateView, CommentCreateView


urlpatterns = [
    path('', PostListView.as_view(), name="post-list"),
    path('post/<int:pk>/', PostDetailView.as_view(), name="post-detail"),
    path('post/new/', PostCreateView.as_view(), name="post-new"),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name="post-delete"),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name="post-update"),
    path('post/<int:pk>/comment/new', CommentCreateView.as_view(), name="comment-new"),
]

urlpatterns += [
    path('user/register', UserCreateView.as_view(), name='register'),
]
