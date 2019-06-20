"""sris URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from testapp import views
urlpatterns = [
    url(r'^admin/blog/info/me', admin.site.urls),
    url(r'^photos/', views.photos_view,name='photos'),
    url(r'^price/', views.pricing_view,name='price'),
    url(r'^contact/', views.contactview),
    url(r'^brand/', views.brand_view),
    url(r'^aboutme/', views.aboutme_view,name='aboutme'),



    url(r'^$', views.homeintro_view,name='home'),



]
