from django.urls import path
from .views import UserProfileView, PostListView, PostDetailView, LikePostView, CommentView

urlpatterns = [
    path('profile/<int:pk>/', UserProfileView.as_view(), name='profile'),
    path('posts/', PostListView.as_view(), name='posts'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/<int:post_id>/like/', LikePostView.as_view(), name='like-post'),
    path('posts/<int:post_id>/comments/', CommentView.as_view(), name='comments'),
]
