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
from it_blog.views import it_blog
from moja_stonka.views import index
from moto.views import moto
from climbing.views import climbing
from guitar.views import guitar

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^it_blog/', it_blog, name='it_blog'),
    url(r'^moto/', moto, name='moto'),
    url(r'^climbing/', climbing, name='climbing'),
    url(r'^guitar/', guitar, name='guitar'),
    url(r'^', index, name='index'),
    # url(r'^it_blog/', include('it_blog.urls')),
]
