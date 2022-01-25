
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from sympy import re

def check_vegan(request):
    return render( request, 'search/search.html' )

def check_result(request):

    if request.method == 'POST':
        p = request.POST.get('p')
        vt = request.POST.get('veganType')    
        result = '%s %s' % (p, vt)
        return HttpResponse(result)
    return render(request, 'search/test.html')



