from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.utils import timezone

from reviews.forms import ReviewForm
from django.core.paginator import Paginator
from reviews.models import Review
from user.models import User
from django.db.models import Q
from user.views import if_session

def write(request):
    context = {}
    if if_session(request):
        context['user_session_id'], context['user_session_veg_type'] = if_session(request)
        print(context['user_session_id'], context['user_session_veg_type'])

    if request.method == 'POST':
        if not request.session.get('user_id'):
            return render(request, 'reviews/write_fail.html', context)

        form = ReviewForm(request.POST, request.FILES)
        user_id = request.session['user_id']

        if form.is_valid():
            review = form.save(commit=False)
            review.member_id = User.objects.get(user_id = user_id)
            review.date = timezone.now()

            review.save()
            return render(request, 'reviews/write_success.html', context)
    
    else:
        form = ReviewForm()
    context['form'] = form
    return render(request, 'reviews/write.html', context)


def delete(request, id):
    context = {}
    if if_session(request):
        context['user_session_id'], context['user_session_veg_type'] = if_session(request)
        print(context['user_session_id'], context['user_session_veg_type'])
    try:
        review = Review.objects.get(id=id)
        review.delete()

        return render(request, 'reviews/delete_success.html', context)
    
    except:
        return render(request, 'reviews/delete_fail.html', context)

# 세션 추가
def update(request, id):
    context={}
    review = Review.objects.get(id=id)
    
    if request.method == 'POST':
        if not request.session.get('user_id'):
            return render(request, 'reviews/update_fail.html')

        form = ReviewForm(request.POST, request.FILES)
        user_id = request.session['user_id']

        if form.is_valid():
            review.member_id = User.objects.get(user_id = user_id)
            review.date = timezone.now()
            review.store_name = form.cleaned_data['store_name']
            review.title = form.cleaned_data['title']
            review.body = form.cleaned_data['body']
            review.file = form.cleaned_data['file']

            review.save()
            return render(request, 'reviews/update_success.html')
    
    else:
        form = ReviewForm()
    
    context['form'] = form
    context['review'] = review
    return render(request, 'reviews/update.html', context)



def list(request):

    review_list = Review.objects.order_by('-date')


    user_id = request.GET.get('user_id', '')
    if user_id:
        review_list = review_list.filter(
            Q(member_id__user_id__icontains=user_id)
        )
    title = request.GET.get('title', '')
    if title:
        review_list = review_list.filter(
            Q(title__icontains=title)
        )
    store_name = request.GET.get('store_name', '')
    if store_name:
        review_list = review_list.filter(
            Q(store_name__icontains=store_name)
        )


    try:
        now_page = int(request.GET.get('page'))
    except TypeError:
        now_page = 1


    p = Paginator(review_list, 10)
    info = p.page(now_page)

    now_page = int(now_page)
    start_page = (now_page - 1) // 10 * 10 + 1
    end_page = start_page + 9
    if end_page > p.num_pages:
        end_page = p.num_pages  

    context = {
    'info' : info,
    'now_page' : now_page,
    'start_page' : start_page,
    'end_page' : end_page,
    'page_range' : range(start_page, end_page+1),
    'has_previous' : p.page(start_page).has_previous(),
    'has_next' : p.page(end_page).has_next(),
    'user_id' : user_id,
    'title' : title,
    'store_name' : store_name,
    }
    if if_session(request):
        context['user_session_id'], context['user_session_veg_type'] = if_session(request)
        print(context['user_session_id'], context['user_session_veg_type'])
    return render(
        request, 'reviews/list.html', context)




def details(request):
    id = int(request.GET.get('id'))
    review = Review.objects.get(id=id)

    is_logined = False
    if 'user_id' in request.session and review.member_id:
        if request.session['user_id'] == review.member_id.user_id:
            is_logined = True

    context = {
        'id' : id,
        'review' : review,
        'is_logined' : is_logined
    }

    if if_session(request):
        context['user_session_id'], context['user_session_veg_type'] = if_session(request)
        print(context['user_session_id'], context['user_session_veg_type'])
    return render(request, 'reviews/details.html', context)


from config import settings
import os


def download(request, id):
    #id = request.GET.get('id')
    review = Review.objects.get(id=id)
    
    filepath = str(settings.BASE_DIR) + ('/media/%s' % review.file.name)
    filename = os.path.basename(filepath)

    with open(filepath, 'rb') as f:
        response = HttpResponse(f, content_type='application/octet-stream')
        response['Content-Disposition'] = 'attachment; filename=%s' % filename
        
        return response



