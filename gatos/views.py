from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Gato

# Create your views here.

def gato(request):
	gatos = Gato.objects.order_by('id')
	template = loader.get_template('gato.html')
	title = 'los gatos van a dominar el mundo'
	context ={
		'gatos': gatos,
		'title': title
	} 
	return HttpResponse(template.render(context, request))

def gato_segun_perro(request):
	template = loader.get_template('gato-segun-perro.html')
	title = 'aqui no hay gatos'
	perrosPiensan = 'los gatos pueden ser amigos'
	culo ={
		'title':title,
		'perrosPiensan':perrosPiensan
	}
	return HttpResponse(template.render(culo, request))