from django.shortcuts import render,redirect

# Create your views here.
from django.views.generic import TemplateView,CreateView,UpdateView,View
from .forms import SignUpForm
from .models import Trade,Trader
import time
from django.contrib.staticfiles.storage import staticfiles_storage
# import threading
from django.http import JsonResponse
import random
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class SignUp(CreateView):
    template_name = "registration/signup.html"
    form_class= SignUpForm
    success_url='/'


class ProfileView(LoginRequiredMixin,View):
    template_name = "users-profile.html"
    model =Trader
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    fields= ('name')

class FAQ(TemplateView):
    template_name='pages-faq.html'


def error_404_view(request, exception):
    data = {}
    # we add the path to the 404.html file
    # here. The name of our HTML file is 404.html
    return render(request, '404.html',data)

def error_500(request):
        data = {}
        response= render(request,'404.html', data)
        response.status_code = 404
        return response

# class Header(View):
#     template_name='header.html'
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         trader = self.request.user
#         context["traders"] = Trader.objects.filter()
#         return context
# class Aside(View):
#     template_name='aside.html'
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["traders"] = Trader.objects.filter(self.request.user) 
#         return context
    