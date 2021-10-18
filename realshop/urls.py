"""realshop URL Configuration

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
from django.urls import path

from categories.views import render_app, load_categories_app, load_offers_app, read_json, qwery_app, menu_app,  \
    update_categories_upp


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', render_app),
    path('loadcategories/', load_categories_app),
    path('loadoffers/', load_offers_app),
    path('updoff/', update_categories_upp),
    path('readjson/', read_json),
    path('cat/<str:cat_id>/', menu_app),
    path('menu/', menu_app),
]
