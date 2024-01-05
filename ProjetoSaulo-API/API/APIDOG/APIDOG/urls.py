"""
URL configuration for APIDOG project.

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
from APP_DOG import views

urlpatterns = [
    path('admin/', admin.site.urls), # URL do painel de ADMIN
    path('adotante/',views.getAdotantes,name="getAdotantes"), # URL para ver todos os adotantes
    path('dog/',views.getDogs,name="getDogs"), # URL para ver todos os dog
    path('adotante/<int:id>/',views.unigetAdotante,name="unigetAdotante"), # URL para ver um unico adotante
    path('dog/<int:id>/',views.unigetDog,name="unigetDog"), # URL para ver um unico dog 
    path('cadastraradotante/',views.createAdotantes,name="createAdotantes"), # URL para cadastrar um adotante
    path('cadastrardog/',views.createDogs,name="createDogs"), # URL para cadastrar um dog 
    path('deleteAdotante/<int:id>/',views.deleteAdotante,name="deleteAdotante"), # URL para deletar um adotante
    path('deleteDog/<int:id>/',views.deleteDog,name="deleteDog"), # URL para deletar um dog 
    path('editAdotante/<int:id>/',views.editAdotante,name="editAdotante"), # URL para editar um adotante
    path('editDog/<int:id>/',views.editDog,name="editDog"), # URL para editar um dog 
]

