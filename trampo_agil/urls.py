"""trampo_agil URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from django.conf.urls import include, url
from django.conf import settings
from site_trampo_agil.views import render_home, render_candidatos, render_empresas, render_login_candidatos, render_login_empresas
# from cadastro.views import index, special, include, user_logout


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', render_home),
    path('candidatos', render_candidatos, name='candidatos'),
    path('empresas', render_empresas),
    path('entrar/login_candidatos', render_login_candidatos, name='login_candidatos'),
    path('entrar/login_empresas', render_login_empresas),
    url('vagas', include('mural_vagas.urls')),
    # url('',index,name='index'),
    # url('special/',special,name='special'),
    # url('dappx/',include('dappx.urls')),
    # url('logout/', user_logout, name='logout'),

]

