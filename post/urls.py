from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.PostList.as_view(),name='postlist'),
    path('<int:pk>/',views.PostDetail.as_view())
]
