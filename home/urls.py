from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('post/<int:post_id>/<slug:post_slug>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post_delete/<int:post_id>/', views.PostDeleteView.as_view(), name='post_delete'),
    path('post_update/<int:post_id>/',views.PostUpdateView.as_view(), name='post_update'),
    path('post_create/', views.PostCreateView.as_view(), name='post_create'),
    path('replay_comment/<int:post_id>/<int:comment_id>',views.CommentReplayView.as_view(), name='replay_comment'),
    path('like/<int:post_id>',views.LikePostView.as_view(), name='like_post'),
]
