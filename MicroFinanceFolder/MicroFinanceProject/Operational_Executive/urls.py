from django.urls import path
from . import views

urlpatterns=[
    path("check/<int:id>/",views.check,name="check"),
    path("show1/",views.show1,name="show1"),
]