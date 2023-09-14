from django.shortcuts import render,HttpResponseRedirect
from django.http import HttpResponse
from .forms import UsersReg
from .models import UserRegistration
from django.views.generic.base import TemplateView,RedirectView
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import get_object_or_404
# Create your views here.
# NEW ITEMS AND RETRIEVE DATA FROM DB
class Home(LoginRequiredMixin,TemplateView):
    template_name = 'addshow.html'
    login_url = '/login/'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        data = UserRegistration.objects.all()
        fm = UsersReg()
        context = {'form': fm, 'data': data}
        return context
    def post(self, request):
        fm = UsersReg(request.POST)
        if fm.is_valid():
            name1 = fm.cleaned_data['name']
            email1 = fm.cleaned_data['email']
            passcode1 = fm.cleaned_data['passcode']
            reg =  UserRegistration(name=name1, email=email1, passcode=passcode1)
            reg.save()
        return HttpResponseRedirect('/')





# DELETE FUNCTION
class Delete(LoginRequiredMixin,RedirectView):
    url = '/'
    def get_redirect_url(self, *args,**kwargs):
        pk = kwargs['id']
        pi = UserRegistration.objects.get(id=pk)
        pi.delete()
        return super().get_redirect_url(*args,**kwargs)

# EDIT Class
class Update(LoginRequiredMixin,View):
    def get(self,request,id):
        pi = UserRegistration.objects.get(pk=id)
        fm = UsersReg(instance=pi)
        return render(request,'update.html',context={'form':fm})
    def post(self, request,id):
        pi = UserRegistration.objects.get(pk=id)
        fm = UsersReg(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
        return HttpResponseRedirect('/')



def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')  # Replace 'dashboard' with the URL where you want to redirect after login
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html')  # Replace 'login.html' with the actual login template name


def logout_view(request):
    logout(request)
    return redirect('/')



class ProfileView(TemplateView):
    template_name = 'profile.html'  # Replace with your profile template name

    def get_context_data(self, **kwargs):
        name = self.kwargs['name']  # Get the 'name' parameter from the URL
        user = get_object_or_404(UserRegistration, name=name)
        context = {'user': user}
        return context



def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        passcode = request.POST['password']
        email = request.POST['email']

        reg = UserRegistration(name=username, email=email, passcode=passcode)
        reg.save()

        # Use f-string to include the username in the URL
        return redirect(f'/profile/{username}/')

    return render(request, 'register.html')

