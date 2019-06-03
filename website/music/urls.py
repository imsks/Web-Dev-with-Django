from django.conf.urls import url
from . import views

app_name = 'music'

urlpatterns = [
    # /music/
    url(r'^$', views.index, name = 'index'),

    # /music/712/
    url(r'^([0-9]+)/$', views.detail, name = 'detail'),

    # /music/712/favorite
    url(r'^([0-9]+)/favorite/$', views.favorite, name = 'favorite')
]