from django.urls import path
from django.contrib.auth import views as auth_views

from .forms import LoginForm
from . import views
app_name = 'core'


urlpatterns = [
    path('', views.home, name='home'),
    path('registro/', views.signup, name='registro'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html', authentication_form=LoginForm), name='login'),
]
