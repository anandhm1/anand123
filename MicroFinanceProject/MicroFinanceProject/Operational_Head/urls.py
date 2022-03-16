from django.urls import path
from . import views

urlpatterns = [
    path('show/',views.showdata,name = 'oprshowdata'),
    path('sanction/<int:id>',views.sanctionloan,name ='sanction'),
    path('approved/',views.approved,name = 'approved'),

    path('opr_head_dashboard/',views.opr_head_dashboard_view,name = 'opr_dashboard'),

]