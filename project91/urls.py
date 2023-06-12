"""
URL configuration for project91 project.

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
from manyproductapps.views import home,InsertInput,Insert,Display,DeleteInput,delete,updateInput,updateDetails,update
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home',home.as_view()),
    path('InsertInput',InsertInput.as_view()),
    path('insert',Insert.as_view()),
    path('display',Display.as_view()),
    path('deleteInput',DeleteInput.as_view()),
    path('delete',delete.as_view()),
    path('updateInput', updateInput.as_view()),
    path('updateDetails', updateDetails.as_view()),
    path('update',update.as_view()),


 ]
