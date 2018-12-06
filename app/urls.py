from django.conf.urls import url
 
from . import views
from . import apis
 
urlpatterns = [
	url(r'^$', views.robot),
	url(r'^talk$', views.talk),
	url(r'^robot$', views.robot),
	url(r'^talk$', views.talk),
	url(r'^api/getWeather', apis.getWeather),
	url(r'^api/getTypes', apis.getTypes),
	url(r'^api/addType', apis.addType),
	url(r'^api/updateType', apis.updateType),
	url(r'^api/deleteTypes', apis.deleteTypes),
	url(r'^api/getChatRecords', apis.getChatRecords),
	url(r'^api/sendMessage', apis.sendMessage)
]
