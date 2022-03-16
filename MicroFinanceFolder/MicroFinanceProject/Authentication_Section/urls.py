from django.urls import path
from . import views

urlpatterns = [
    path('staff_login/',views.staff_loginview,name = 'staff_login'),
    path('logoutview/',views.logoutview,name = 'logoutview')

]