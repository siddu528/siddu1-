"""
URL configuration for bloodbank project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from student import views

urlpatterns = [
      path('admin/', admin.site.urls),
      path("hospital",views.hospital),
      path('hospitaldata',views.hospitaldata),
      path('search',views.search),
      path('reciver',views.reciver),
      path('reciverdata',views.reciverdata),
      path('rsearch',views.rsearch),
      path('donor',views.donor),
      path('donordata',views.donordata),
      path('dsearch',views.dsearch),
      path('adminregistration',views.adminregistration),
      path('admindata',views.admindata),
      path('asearch',views.asearch),
      path('adminlogin',views.adminlogin),
      path('adminhome',views.adminhome),
      path('adminchangepassword',views.adminchangepassword),
      path('menu',views.menu),
]
