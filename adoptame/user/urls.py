from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('index', views.index, name='index'),
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:pk>/delete/', views.delete, name='delete'),
]