# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello World. You are on the the poll index')

def results(request, poll_id):
    return HttpResponse('You are looking at the results of the poll %s' % poll_id)

def vote(request, poll_id):
    return HttpResponse("You are voting on poll %s" % poll_id)
