from django.conf.urls import url
from . import views


urlpatterns = [

    url(r'^$', views.login, name='login'),
    url(r'^login/$', views.login, name='login'),
    url(r'^index/$', views.index, name='index'),
]

app_name = 'myappweb'