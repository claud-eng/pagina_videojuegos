"""dalepausa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path,include
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from rest_framework.authtoken.views import obtain_auth_token  #--token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registro/', include('apps.Registro.urls')),
    path('usuario/', include('apps.Usuario.urls')),
    #path('login/', auth_views.LoginView.as_view(template_name='Usuario/login.html'), name='login'),

    # Login and Logout
    path('login/', LoginView.as_view(redirect_authenticated_user=True,template_name='Usuario/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='Usuario/logout.html'), name='logout'),
    path('', TemplateView.as_view(template_name='Usuario/index.html'), name='home'),

    # localhost:8000/api-token-auth
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),  #token

]
