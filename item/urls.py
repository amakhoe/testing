from django.urls import path
from . import views
app_name = 'item'

urlpatterns = [
     path('add/', views.newAdd, name="add"),
     path('<int:pk>/', views.detail, name='detalhes'),
     path('<int:pk>/delete/', views.delete, name='delete'),
     path('<int:pk>/edit/', views.newEdit, name='edit')
]
