
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from sympy import re
from user.views import if_session

def check_vegan(request):
    context = {}
    if if_session(request):
        context['user_session_id'], context['user_session_veg_type'] = if_session(request)

    return render( request, 'search/search.html', context)

def check_result(request):
    context = {}
    if if_session(request):
        context['user_session_id'], context['user_session_veg_type'] = if_session(request)

    if request.method == 'POST':
        p = request.POST.get('p')
        vt = request.POST.get('veganType')    
        result = '%s %s' % (p, vt)
        return HttpResponse(result)
    return render(request, 'search/test.html', context)



