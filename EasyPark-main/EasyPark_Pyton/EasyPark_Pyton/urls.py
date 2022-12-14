"""EasyPark_Pyton URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from EasyPark_Pyton.views import inicio,buscar,login,publicar
from EasyPark_Pyton.views import registropersona,Actualizarpersona,Listadopersonas,Borrarpersona

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index.html/', inicio, name='inicio'),
    path('buscar.html/', buscar, name='buscar'),
    path('login.html/', login,name='login'),
    path('publicar.html/', publicar,name='publicar'),
    
    
    path('registro.html/', registropersona, name='registropersona'),

]
