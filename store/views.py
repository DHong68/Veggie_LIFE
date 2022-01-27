from django.shortcuts import render
from django.db.models import Q
from django.core.paginator import Paginator

from os import path
from django.core.exceptions import ImproperlyConfigured
import json

from .models import Store
from user.views import if_session


def search(request):
    stores = Store.objects.exclude(name='상호명').order_by('name')

    key = False

    gu = request.GET.get('gu', '')
    if gu and gu != '전체':
        stores = stores.filter(
            Q(gu__icontains=gu)
        )

    type = request.GET.get('type', '')
    if type and type != '전체':
        stores = stores.filter(
            Q(type__icontains=type)
        )

    searched = request.GET.get('searched', '')
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
        'key': key,
        "cur_page": cur_page
    }
    if if_session(request):
        context['user_session_id'], context['user_session_veg_type'] = if_session(request)
        print(context['user_session_id'], context['user_session_veg_type'])


    return render(
        request, 'store/search.html', 
        context
    )


def details(request):
    store_name = request.GET.get('store')
    store = Store.objects.get(name=store_name)

    file_path = path.abspath(__file__)
    dir_path = path.dirname(file_path)
    key_path = path.join(dir_path, 'key.json')

    with open(key_path) as f:
        secret_key = json.loads(f.read())

    def get_secret(setting):
        try:
            return secret_key[setting]
        except KeyError:
            error_msg = "Set the {} environment variable".format(setting)
            raise ImproperlyConfigured(error_msg)


    SECRET_KEY = get_secret("GOOGLE_MAP_KEY")
    google_map_src = "https://maps.googleapis.com/maps/api/js?key=" + SECRET_KEY + "&callback=initMap"

    return render(request, 'store/details.html', {"store": store, "google_map_src": google_map_src})
