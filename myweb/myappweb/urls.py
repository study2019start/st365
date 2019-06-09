from django.conf.urls import url
from . import views
from django.views.static import serve
from django.conf import settings


urlpatterns = [

    url(r'^$', views.login, name='login'),
    url(r'^login/$', views.login, name='login'),
    url(r'^index/$', views.index, name='index'),
    url(r'^datatable/$', views.vtable, name='vtable'),
    url(r'^gtable$', views.cdatatable, name='cdatatable'),
    url(r'down/(?P<id>\d+)', views.down, name='down'),
    url(r'^meida/(?P<path>.*)$', serve, {'document_root' : settings.MEDIA_ROOT}),
]

app_name = 'myappweb'