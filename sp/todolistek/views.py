from django.http import HttpResponse
from django.template import loader
from .models import Uporabnik, Opravilo

def index (request):
	vsa_opravila = Opravilo.objects.all()
	template = loader.get_template('todolistek/index.html')
	context = {
		'vsa_opravila': vsa_opravila,
	}
	return HttpResponse(template.render(context,request))
	
def podrobnosti(request,opravilo_id):
	return HttpResponse("<h1>Opravilo id "+ str(opravilo_id) +"</h1>")
