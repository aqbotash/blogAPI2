from django.urls import path
from .views import PostListView, PostDetailView, RegisterCreateView, CommentListView, CommentDetailView

urlpatterns = [
    path('posts/', PostListView.as_view(), name='post_list_create'),
    path('posts/<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('posts/<int:pk>/comments/', CommentListView.as_view(), name='comment_list_create'),
    path('posts/<int:pk>/comments/<int:comment_pk>', CommentDetailView.as_view(), name='comment_detail'),
    path('register', RegisterCreateView.as_view(), name='sign-up'),
]