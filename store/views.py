from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Q
from django.core.paginator import Paginator

from .models import Store

def show(request):
    stores = Store.objects.exclude(name='상호명').order_by('name')

    # set current page - initialize it as 1
    try:
        cur_page = int(request.GET.get('page'))
    except TypeError:
        cur_page = 1
    
    # pagination
    p = Paginator(stores, 10)
    info = p.page(cur_page)

    start_page = ((cur_page-1) // 10) * 10 + 1
    end_page = start_page + 9 

    if end_page > p.num_pages:
        end_page = p.num_pages

    # prev, next page
    is_prev = False
    is_next = False
    if start_page > 1:
        is_prev = True
    if end_page < p.num_pages:
        is_next = True

    context = {
        'stores': info,
        'page_range': range(start_page, end_page+1), 
        'is_prev': is_prev, 
        'is_next': is_next, 
        'start_page': start_page, 
        'end_page': end_page
    }

    return render(
        request, 'store/show_results.html', 
        context
    )


def search(request):
    stores = Store.objects.exclude(name='상호명').order_by('name')

    key = False

    gu = request.GET.get('gu')
    if gu:
        stores = stores.filter(
            Q(gu__icontains=gu)
        )

    type = request.GET.get('type')
    if type:
        stores = stores.filter(
            Q(type__icontains=type)
        )

    searched = request.GET.get('searched')
    if searched:
        stores = stores.filter(
            Q(name__icontains=searched) |
            Q(menu__icontains=searched)
        )

    if gu or searched or type:
        key = True


    ### pagination ###
    # set current page - initialize it as 1
    try:
        cur_page = int(request.GET.get('page'))
    except TypeError:
        cur_page = 1
    
    # pagination
    p = Paginator(stores, 10)
    info = p.page(cur_page)

    start_page = ((cur_page-1) // 10) * 10 + 1
    end_page = start_page + 9 

    if end_page > p.num_pages:
        end_page = p.num_pages

    # prev, next page
    is_prev = False
    is_next = False
    if start_page > 1:
        is_prev = True
    if end_page < p.num_pages:
        is_next = True

    context = {
        'stores': info,
        'page_range': range(start_page, end_page+1), 
        'is_prev': is_prev, 
        'is_next': is_next, 
        'start_page': start_page, 
        'end_page': end_page,
        'searched': searched, 
        'gu': gu,
        'type': type,
        'key': key
    }

    return render(
        request, 'store/search.html', 
        context
    )


def details(request):
    store_name = request.GET.get('menu')
    store = Store.objects.filter(name=store_name)

    return render(request, 'store/details.html', {})