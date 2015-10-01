from django.shortcuts import *
from django.http import *
from django.core.context_processors import csrf
from django.template import RequestContext

from bsscultural.course.models import *

def index(request):
	response = {}

	return render_to_response('index.html', response, context_instance=RequestContext(request))


def courses(request):
	response = {}

	response.update({'courses':Course.objects.all().order_by('name')})
	return render_to_response('courses.html', response, context_instance=RequestContext(request))