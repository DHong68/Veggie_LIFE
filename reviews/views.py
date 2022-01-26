from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from .models import Review
from django.core.paginator import Paginator
from user.models import User

# Create your views here.
# def write(request):
#     if request.method == 'POST':
#         title = request.POST.get('title')
#         store_name = request.POST.get('store_name')
#         body = request.POST.get('body')

#         try:
#             user_id = request.session['user_id']

#             member = Member.objects.get(user_id=user_id)

#             review = Review(title = title, store_name = store_name,
#                 body = body, member = member)
#             review.date = timezone
#             review.save()
#             return render(request, 'reviews/write_success.html')
        
#         except:
#             return render(request, 'reviews/write_fail.html')
    
#     return render(request, 'reviews/write.html')

# def upload(request):
#     if request.method == 'POST':
#         upload_files = request.FILES.getlist('file')

#         result = ''
#         for upload_file in upload_files:
#             name = upload_file.name
#             size = upload_file.size

#             with open(name, 'wb') as file:
#                 for chunk in upload_file.chunks():
#                     file.write(chunk)
#             result += '%s<br>%s<hr>' % (name, size)
#         return HttpResponse(result)
    
#     return render(request, 'reviews/write.html')

# def delete(request, id):
#     try:
#         # select * from article where id = ?
#         review = Review.objects.get(id=id)
#         review.delete()
#         return render(request, 'delete_success.html')
    
#     except:
#         return render(request, 'delete_fail.html')

# def update(request, id):
#     review = Review.objects.get(id=id)

#     if request.method == 'POST':
#         title = request.POST.get('title')
#         store_name = request.POST.get('store_name')
#         body = request.POST.get('body')
    
#         try:
#             review.title = title
#             review.store_name = store_name
#             review.body = body
#             review.save()
#             return render(request, 'update_success.html')
        
#         except:
#             return render(request, 'update_fail.html')

#     context = { 
#         'review' : review 
#     }

#     return render(request, 'update.html', context)

def list(request):


    now_page = request.GET.get('page', 1)
    store_name = request.GET.get('store_name', '')
    review_list = Review.objects.order_by('-date')

    # store_name=''
    # if request.method == 'POST':
    #     store_name = request.POST.get('store_name')
    # else:
    #     store_name = request.GET.get('store_name', '')

    if store_name != '':
        review_list = Review.objects.filter(store_name=store_name).order_by('-date')


    # review_list = Review.objects.order_by('-date')

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

# def list_search(request):
#     review_list = Review.objects.order_by('-date')
#     search = request.GET.get('search', '')
#     if search:
#         review_list = review_list.filter(store_name=search)

