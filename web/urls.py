"""web URL Configuration

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
from django.conf.urls import url
from django.contrib import admin

from inventory import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^map/', views.map, name='map'),
    url(r'^list/', views.list, name='list'),
    url(r'^house/', views.house, name='house'),
    # VR
    url(r'^panorama/', views.panorama, name='panorama'),
    url(r'^hackingroom1/',views.hackingroom1, name='hackingroom1'),
    url(r'^hackingroom2/',views.hackingroom2, name='hackingroom2'),
    url(r'^hallway/', views.hallway, name='hallway'),
    url(r'^lobby/', views.lobby, name='lobby'),
    url(r'^toilet4man/', views.toilet4man, name='toilet4man'),
    url(r'^office/', views.office, name='office'),
    url(r'^customer_center/', views.customer_center, name='customer_center'),
]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    )