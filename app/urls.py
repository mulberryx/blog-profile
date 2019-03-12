from django.conf.urls import url
 
from . import views
from . import apis
 
urlpatterns = [
	url(r'^$', views.robot),
	url(r'^talk$', views.talk),
	url(r'^robot$', views.robot),
	url(r'^talk$', views.talk),
	url(r'^api/getWeather', apis.getWeather),
	url(r'^api/sendMessage', apis.sendMessage)
]
