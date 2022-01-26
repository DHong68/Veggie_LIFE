from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.utils import timezone

from reviews.forms import ReviewForm
from django.core.paginator import Paginator
from user.models import User

def write(request):
    if request.method == 'POST':
        if not request.session.get('user_id'):
            return render(request, 'reviews/write_fail.html')

        form = ReviewForm(request.POST, request.FILES)

        if form.is_valid():
            review = form.save(commit=False)
            review.member_id = User.objects.get(user_id = 'abcd')
            review.date = timezone.now()

            review.save()
            return render(request, 'reviews/write_success.html')
    
    else:
        form = ReviewForm()

    return render(request, 'reviews/write.html', { 'form':form })


def delete(request, id):
    try:
        review = Review.objects.get(id=id)
        review.delete()

        return render(request, 'reviews/delete_success.html')
    
    except:
        return render(request, 'reviews/delete_fail.html')

def update(request, id):
    review = Review.objects.get(id=id)

    if request.method == 'POST':
        title = request.POST.get('title')
        store_name = request.POST.get('store_name')
        body = request.POST.get('body')
    
        try:
            review.title = title
            review.store_name = store_name
            review.body = body
            review.date = timezone.now()
            review.save()
            return render(request, 'reviews/update_success.html')
        
        except:
            return render(request, 'reviews/update_fail.html')

    context = { 
        'review' : review 
    }
    return render(request, 'reviews/update.html', context)

def list(request):
    now_page = request.GET.get('page', 1)
    
    review = Review.objects.order_by('-date')
    p = Paginator(review, 10)
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

    }
    return render(
        request, 'reviews/list.html', context)

def insert(request):
    for i in range(103, 200):
        Review.objects.create(member_id=i, date='2020-12-12',store_name='1',
        title='1', body='1')
    return HttpResponse('데이터 입력 완료')
