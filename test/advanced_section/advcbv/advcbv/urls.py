from django.contrib import admin
from django.conf.urls import url, include
from basic_app import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.IndexView.as_view()),
    url(r'^basic_app/', include('basic_app.urls', namespace='basic_app')),
]