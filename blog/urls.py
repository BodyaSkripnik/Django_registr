from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('login/', LoginUser.as_view(), name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('home/', home, name='home'),
    path('logout/', logout_user, name='logout'),
]