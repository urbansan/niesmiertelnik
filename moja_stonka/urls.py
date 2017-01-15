"""moja_stonka URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from blogs.views import *
from moja_stonka.views import index

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^about/$', about, name='about'),
    url(r'^sidebar/$', sidebar, name='sidebar'),
    url(r'^$', blob, name='blob'),
    url(r'^zawijanie/$', zawijanie, name='zawijanie'),
    url(r'^it_blog/$', it_blog, name='it_blog'),
    url(r'^moto/$', moto, name='moto'),
    url(r'^climbing/$', moto, name='moto'),
    url(r'^guitar/$', moto, name='moto'),
    url(r'^(?P<article_link>.*)/', post, name='post'),
]
