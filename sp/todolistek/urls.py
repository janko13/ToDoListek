from django.conf.urls import url
from . import views

urlpatterns = [
	#ni cool za vsaga uporabnika mors met vedn drug url
	
	#/todolistek/
    url(r'^$', views.prijava , name='prijava' ),
	
	#/todolistek/registracija/
    url(r'^registracija/$', views.registracija , name='registracija' ),
	
	#/todolistek/home/
    url(r'^home/$', views.home , name='home' ),
	
	#/todolistek/urediOpraviala
    url(r'^urediOpraviala/$', views.urediOpraviala , name='urediOpraviala' ),
	
	#/todolistek/grafAktivnosti
    url(r'^grafAktivnosti/$', views.grafAktivnosti, name='grafAktivnosti' ),
	
	#/todolistek/nastavitve
    url(r'^nastavitve/$', views.nastavitve , name='nastavitve' ),
	
	#/todolistek/odjava
    url(r'^odjava/$', views.odjava , name='odjava' ),

]