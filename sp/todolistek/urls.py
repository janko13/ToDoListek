from django.conf.urls import url
from . import views

urlpatterns = [
	#/todolistek/
    url(r'^$', views.index , name='index' ),
	
	#/todolistek/71/
	url(r'^(?P<opravilo_id>[0-9]+)/$', views.podrobnosti , name='podrobnosti' ),
]