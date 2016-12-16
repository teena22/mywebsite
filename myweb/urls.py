from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home,name="home"),
    url(r'^readmore', views.readmore,name="redamore"),
    url(r'^error', views.error,name="error"),
]
