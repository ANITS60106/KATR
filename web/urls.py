from django.urls import path
from . import views

app_name = 'web'

urlpatterns = [
    path('', views.index, name="index"),
<<<<<<< HEAD
    path('home', views.home, name='home'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
=======
>>>>>>> 1b6ad91097e8102e128dce4a5b3b8c78c03332c0
]