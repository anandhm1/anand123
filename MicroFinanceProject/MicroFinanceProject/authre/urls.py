from django.urls import path
from . import views
urlpatterns = [
    path('loginre/',views.loginViewRE,name='loginre'),
    path('logoutre/',views.logoutViewRE,name='logoutre'),

]