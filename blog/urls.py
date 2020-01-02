from django.urls import path
from .views import (
    article_detail_view,
    article_create_view,
    article_list_view,
    article_lookup_view,
    article_delete_view,
    article_edit_view,
    
)

app_name = 'blog'

urlpatterns = [
    path('detail/', article_detail_view, name='article-detail'),
    path('<int:my_id>/', article_lookup_view, name='article-lookup'),
    path('create/', article_create_view, name = 'article-create'),
    path('', article_list_view, name = 'article-list'),
    path('<int:my_id>/delete/', article_delete_view, name='article-delete'),
    path('<int:my_id>/edit/', article_edit_view, name='article-edit'),
    
]