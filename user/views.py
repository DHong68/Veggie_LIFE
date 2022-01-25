from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from .models import User
from .forms import SignupForm

def home(request):
     return render(request, 'user/home.html')

          
def signup(request):
     if request.method == 'POST':
          form = SignupForm(request.POST)
          context = {}
          if form.is_valid():
               signupform = form.save(commit=False)
               if User.objects.filter(user_id = signupform.user_id).exists():
                    context['error'] = '이미 가입된 아이디입니다.'
                    return render(request, "user/signup.html", context)
               elif signupform.password != signupform.re_password:
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
