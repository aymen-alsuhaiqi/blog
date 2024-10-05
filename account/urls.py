from django.urls import path
from . import views

urlpatterns = [
    # path('/accounts/login',),
    path('login',views.login_user,name='login'),
    path('logout',views.logout_user,name='logout'),
    path('profile',views.profile,name='profile'),
    path('register',views.register,name='register'),
    
]
