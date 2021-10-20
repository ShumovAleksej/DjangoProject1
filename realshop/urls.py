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

from categories.views import load_categories_app, load_offers_app, qwery_app, menu_app, \
    update_categories_upp, boot_app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cat/<str:cat_id>/', menu_app),
    path('', menu_app),
    path('boot/', boot_app),
    path('loadcategories/', load_categories_app),
    path('loadoffers/', load_offers_app),
    path('updoff/', update_categories_upp),

]
