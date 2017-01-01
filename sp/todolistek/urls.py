from django.conf.urls import url
from . import views

urlpatterns = [
	#ni cool za vsaga uporabnika mors met vedn drug url
	
	#/todolistek/
    url(r'^$', views.prijava , name='prijava' ),
	
	#/todolistek/registracija/
    url(r'^registracija/$', views.registracija , name='registracija' ),
	
	#/todolistek/433543/
    url(r'^(?P<user_id>[0-9]+)/$', views.home , name='home' ),
	
	#/todolistek/433543/urediOpraviala
    url(r'^(?P<user_id>[0-9]+)/urediOpraviala/$', views.urediOpraviala , name='urediOpraviala' ),
	
	#/todolistek/433543/grafAktivnosti
    url(r'^(?P<user_id>[0-9]+)/grafAktivnosti/$', views.grafAktivnosti, name='grafAktivnosti' ),
	
	#/todolistek/433543/nastavitve
    url(r'^(?P<user_id>[0-9]+)/nastavitve/$', views.nastavitve , name='nastavitve' ),

]