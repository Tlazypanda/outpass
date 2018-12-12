from django.urls import path
from . import views

urlpatterns = [
    path('/list', views.request_list, name='request_list'),
    path('/request/new', views.request_new, name='request_new'),
    path('/request/<int:pk>/', views.request_detail, name='request_detail'),
]
