from . import views
from django.urls import path

urlpatterns = [
    path('posts', views.PostList.as_view(), name='posts'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]