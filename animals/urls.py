"""RAMS_SKELETON URL Configuration

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
from django.urls import path
from . import views

app_name = 'animals'

urlpatterns = [
    path('<int:pk>/', views.AnimalDetailView.as_view(), name='animal_detail'),
    path('<int:pk>/delete', views.AnimalDeleteView.as_view(), name='animal_delete'),
    path('<species>/new', views.AnimalNewView, name="animal_new"),
    path('<int:pk>/edit', views.AnimalEditView, name="animal_edit"),
    #path('owner/<owner_pk>/animal', views.owner_animal_landing, name='owner_animal_landing'),
    path('', views.AnimalListView.as_view(), name="animal_list"),
    path('<species>/<pk>/new', views.new_owned_animal, name='new_owned_animal'),
]
