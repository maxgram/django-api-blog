# from django.http import Http404, HttpResponse, HttpResponseForbidden, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404

def index(request):
    return render( request, 'base.html', {  } )
