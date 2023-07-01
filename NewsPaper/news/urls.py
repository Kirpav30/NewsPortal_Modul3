from . import views
from django.urls import path
from .views import PostsList, PostDetail, PostCreate, PostUpdate, PostDelete, ArticlesCreate, ArticlesUpdate, \
   ArticlesDelete, subscriptions

urlpatterns = [
   path('', PostsList.as_view()),
   path('news/', views.PostsList.as_view(), name='news_list'),
   path('<int:pk>', PostDetail.as_view()),
   path('news/create/', PostCreate.as_view(), name='post_create'),
   path('news/<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
   path('news/<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
   path('article/', views.ArticleList.as_view(), name='article_list'),
   path('article/create/', ArticlesCreate.as_view(), name='article_create'),
   path('article/<int:pk>/update/', ArticlesUpdate.as_view(), name='article_update'),
   path('article/<int:pk>/delete/', ArticlesDelete.as_view(), name='article_delete'),
   path('search/', views.PostSearch.as_view(), name='post_search'),
   path('subscriptions/', subscriptions, name='subscriptions'),
]
