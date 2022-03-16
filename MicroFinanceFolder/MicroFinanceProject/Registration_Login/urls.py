from django.urls import path
from .views import *

urlpatterns=[
    path('signup/', SignUpView, name='signup'),
    path('login/', LogInView, name='login'),
    path('logout/', LogOutView, name='logout')
]