from . import views
from django.urls import path

urlpatterns = [
    path('posts', views.PostList.as_view(), name='posts'),
    path('', views.PostHome.as_view(), name='home')
]