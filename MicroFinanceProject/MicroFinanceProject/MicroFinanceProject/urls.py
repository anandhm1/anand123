"""MicroFinanceProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Customer.views import IndexView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', IndexView, name='index'),
    path('registration_login/', include("Registration_Login.urls")),
    path('customer/', include("Customer.urls")),
    path('relationship_executive/', include("Relationship_Executive.urls")),
    path('re/',include('Relationship_Executive.urls')),
    path('op/',include('Operational_Executive.urls')),
    path('authre/',include('authre.urls')),

    path('finance/',include('Registration_Login.urls')),
    path('oprhead/',include('Operational_Head.urls')),
    path('a_head/',include('Accounts_Head.urls')),
    path('auth_section/',include('Authentication_Section.urls')),


]
