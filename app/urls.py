from django.conf.urls import url
from django.contrib import admin
 
from . import views
 
urlpatterns = [
  url(r'^$', views.robot),
  url(r'^statistics$', views.statistics),
  url(r'^talk$', views.talk),
  url(r'^admin/', admin.site.urls),
]