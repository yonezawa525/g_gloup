from django.shortcuts import render, redirect
from django.shortcuts import render
from django.views.generic import ListView
from .models import User
from django.http import Http404
from .forms import LoginForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout

def user_login(request):
    form = LoginForm()
    return render(request, 'polls/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect ('login')

def authentication(request):
    form = LoginForm(request.POST)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('polls:index')
    form.add_error(None, 'LOGIN_ID、またはPASSWORDが違います。')
    return render(request, 'polls/login.html', {'form': form})

class Listattendview(ListView):
    template_name = 'html/itiran.html'
    login_url = '/login/'
    model = User

    


class Listtikokuview(LoginRequiredMixin,ListView):
    template_name = 'html/report.html'
    model = User

    

    def post(self, request, *args, **kwargs):
            input_date = request.POST["date"]
            input_report = request.POST["report"]
            user = User(userUp = input_date, userTxt = input_report)
            user.save()
            return render(request,'html/top.html')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class Listtopview(LoginRequiredMixin, ListView):
    template_name = 'html/top.html'
    model = User
    def logout_view(request):
        logout(request)
        return redirect ('login')

class MypageView(LoginRequiredMixin, ListView):
  template_name = 'login.html'
    

def index(request):
    return render(request, 'html/test1.html')
    
# Create your views here.

# 404エラー用
#class MyView(View):
#    def index(self):
#        raise Http404