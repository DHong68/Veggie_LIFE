from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User
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
     context = {}
     if user:
          context['user'] = user
          return render(request, 'user/mypage.html', context)
     else:
          return redirect('/')

# def update(request, user_id):

#      if request.method == 'POST':
#           form = SignupForm(request.POST)
#           re_password = request.POST.get('re_password')
#           context = {}
#           if form.is_valid():
#                signupform = form.save(commit=False)
#                if signupform.password != re_password:
#                     context['error'] = '비밀번호가 일치하지 않습니다.' 
#                     return render(request, "user/signup.html", context)
#                signupform.save()
#                return redirect('/user/login')
#      else:
#           form = SignupForm()
#      return render(request, 'user/signup.html', {'form': form})

# from .forms import CustomUserChangeForm
# from django.contrib.auth.decorators import login_required

# @login_required
# def update(request):
#     if request.method == 'POST':
#           user_change_form = CustomUserChangeForm(request.POST, instance=request.user)
#           re_password = request.POST.get('re_password')
#           context = {}
#           if user_change_form.is_valid():
#                updateform = user_change_form.save(commit=False)
#                if updateform.password != re_password:
#                     context['error'] = '비밀번호가 일치하지 않습니다.' 
#                     return render(request, "user/update.html", context)
#                updateform.save()
#                return redirect('/user/login')
#     else:
#           user_change_form = CustomUserChangeForm(instance = request.user)
#           return render(request, 'user/update.html', {'user_change_form':user_change_form})