from django.conf.urls import url	
from . import views

urlpatterns=[
	url(r'^$', views.gato, name='gato'),
	url(r'^perros/',views.gato_segun_perro,name='gato')
]