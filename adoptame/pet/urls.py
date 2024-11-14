from django.urls import path
from . import views

app_name = 'pet'

urlpatterns = [
    path('new/', views.new, name='new'),
    path('<int:pk>/', views.detail, name='detail'),
    path('get-races/', views.get_races, name='getRaces'),
]

