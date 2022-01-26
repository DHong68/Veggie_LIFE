from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.utils import timezone

from reviews.forms import ReviewForm
from django.core.paginator import Paginator
from reviews.models import Review
from user.models import User
from django.db.models import Q

def write(request):
    if request.method == 'POST':
        if not request.session.get('user_id'):
            return render(request, 'reviews/write_fail.html')

        form = ReviewForm(request.POST, request.FILES)
        user_id = request.session['user_id']

        if form.is_valid():
            review = form.save(commit=False)
            review.member_id = User.objects.get(user_id = user_id)
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
        form = ReviewForm(request.POST, request.FILES)

        if form.is_valid():
            review.member_id = User.objects.get(user_id = 'abcd')
            review.date = timezone.now()
            review.store_name = form.cleaned_data['store_name']
            review.title = form.cleaned_data['title']
            review.body = form.cleaned_data['body']
            review.file = form.cleaned_data['file']

            review.save()
            return render(request, 'reviews/update_success.html')
    
    else:
        form = ReviewForm()
    
    context = { 
        'review' : review 
    }
    return render(request, 'reviews/update.html', context)

def list(request):

    review_list = Review.objects.order_by('-date')


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
    'store_name' : store_name
    }
    return render(
        request, 'reviews/list.html', context)




def details(request):
    id = request.GET.get('id')
    review = Review.objects.get(id=id)

    context = {
        'id' : id,
        'review' : review,
    }
    return render(request, 'reviews/details.html', context)


