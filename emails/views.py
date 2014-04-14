# Create your views here.
from django.shortcuts import render_to_response
from .models import *
from simplejson.encoder import JSONEncoder
import simplejson
import urllib2
import urllib
from django.views.decorators.csrf import csrf_exempt



@csrf_exempt
def qmView(request):
    m = request.GET['m']
    e = request.GET['e']
    
    plantilla = EmailTemplate.objects.get(pk=m)
    header_html = '<html><body>'
    footer_html = '</body></html>'
    html_content = '%s%s%s' % (header_html,plantilla.htmlContent.replace('cid:', 'ADJUNTOS/zipfile/' + os.path.basename(plantilla.zipFile.path) + '/img/'),footer_html)
    email = Email.objects.get(pk=e)
    nombre = '%s %s' % (email.nombre,email.apellido)
    
    response = render_to_response('jsonList.html',{'json':html_content},content_type='application/json', mimetype='text/html')
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS, PUT, DELETE"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "*"
    return response
    