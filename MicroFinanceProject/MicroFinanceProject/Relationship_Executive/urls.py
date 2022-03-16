from django.urls import path
from . import views

urlpatterns= [
    path("form/",views.baseiformview, name= "form"),
    path("bank/",views.bankformview, name= "back"),
    path("documentUpload/",views.documentupload, name= "document"),
    path("priview/",views.priView, name= "priview"),
    path('show/',views.showview, name = 'reshow'),

]