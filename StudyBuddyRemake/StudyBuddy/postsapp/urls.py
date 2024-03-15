from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.mainpage, name='postslink'),
    path('<int:pk>', views.postsDetailView.as_view(), name='posts-detail')
]
