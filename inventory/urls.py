"""
URL configuration for djangodelights project.

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
from django.urls import path
from inventory.views.ingredient import Ingredient
from inventory.views.routeNotFound import RouteNotFound
import django.conf.urls

urlpatterns = [
    path(Ingredient.list_path, Ingredient.as_view(), name='get_all_ingredients'),
    path(Ingredient.single_path, Ingredient.as_view(), name='get_ingredient'),
]

django.conf.urls.handler404 = RouteNotFound.as_view()