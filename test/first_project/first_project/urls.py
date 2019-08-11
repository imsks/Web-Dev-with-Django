from django.contrib import admin
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^users/', include('first_app.urls')),
    url('admin/', admin.site.urls),
]
