from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.mostrarTabla, name='mostrarTabla'),
	url(r'insertar/', views.formulario, name='formulario'),
]