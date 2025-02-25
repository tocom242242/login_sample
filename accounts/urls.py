from django.urls import path
from accounts import views

urlpatterns = [
    path('singup', views.signup, name='signup'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
]
