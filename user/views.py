from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from .models import User
from reviews.models import Review
from .forms import SignupForm

def home(request):
     return render(request, 'user/home.html')

          
def signup(request):
     if request.method == 'POST':
          form = SignupForm(request.POST)
          re_password = request.POST.get('re_password')
          context = {}
          if form.is_valid():
               signupform = form.save(commit=False)
               if signupform.password != re_password:
                    context['error'] = '비밀번호가 일치하지 않습니다.' 
                    return render(request, "user/signup.html", context)
               signupform.save()
               return redirect('/user/login')
     else:
          form = SignupForm()
     return render(request, 'user/signup.html', {'form': form})


def login(request):
     if request.method == 'POST':
          user_id = request.POST.get('user_id')
          password = request.POST.get('password')
          context = {}
          try:
               user = User.objects.get(user_id = user_id)
               if password != user.password:
                    context['error'] = '비밀번호가 틀렸습니다.'
                    return render(request, 'user/login.html', context)
          except User.DoesNotExist:
               context['error'] = '존재하지 않는 아이디입니다'
               return render(request, 'user/login.html', context)
          else:
               request.session['user_id'] = user.user_id
               request.session['password'] = user.password
          return redirect('/')
     else:
          return render(request, 'user/login.html')

def logout(request):
     request.session.flush()
     return redirect('/')

def delete(request):
     user_id = request.session['user_id']
     delete_user = User.objects.get(user_id = user_id)
     delete_user.delete()
     logout(request)
     return redirect('/')

def mypage(request):
     user_id = request.session['user_id']
     user = User.objects.get(user_id = user_id)
     posts = Review.objects.filter(member_id = user.id).values()
     if len(posts) >= 5:
          posts = posts[0:5]
     context = {}
     context['posts'] = posts
     if user:
          context['user'] = user
          return render(request, 'user/mypage.html', context)
     else:
          return redirect('/')

def update(request, user_id):
     user = get_object_or_404(User, user_id = user_id)
     if request.method == 'POST':
          form = SignupForm(request.POST, instance=user)
          re_password = request.POST.get('re_password')
          context = {}
          if form.is_valid():
               signupform = form.save(commit=False)
               if signupform.password != re_password:
                    context['error'] = '비밀번호가 일치하지 않습니다.' 
                    return render(request, "user/signup.html", context)
               signupform.save()
               return redirect('/user/login')
     else:
          form = SignupForm(instance=user)
     return render(request, 'user/update.html', {'form': form})
