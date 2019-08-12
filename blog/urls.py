from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/', views.BlogPostListView.as_view(), name='all-posts'),
    path('post/<int:pk>', views.BlogPostDetailView.as_view(), name='post-detail'),
    path('authors/', views.AuthorListView.as_view(), name='all-authors'),
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
    path('post/<int:pk>/addcomment', views.BlogCommentAdd.as_view(), name='add-comment'),
    path('post/publish', views.BlogPostCreate.as_view(), name='publish-post'),
    path('post/<int:pk>/delete', views.BlogPostDelete.as_view(), name='delete-post'),
]