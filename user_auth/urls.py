from django.urls import path
from . import views

app_name = 'user_auth'

urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('login_or_register/', views.login_register, name='login_register'),
    path('approve_users/', views.approve_users, name='approve_users'),
    path('await_approval/', views.await_approval, name='await_approval'),
]
