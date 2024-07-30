from django.urls import path

from . import views

app_name = 'board'

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.list, name='list'),
    path('regist/', views.regist, name='regist'),
    path('read/<int:id>/', views.read, name='read'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('remove/<int:id>/', views.remove, name='remove'),
]
