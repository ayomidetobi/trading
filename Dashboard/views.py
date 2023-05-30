from django.shortcuts import render,redirect

# Create your views here.
from django.views.generic import TemplateView,CreateView,UpdateView,View
from .forms import SignUpForm
from .models import Trade,Trader
import time
import json
from rest_framework import serializers
# from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from django.contrib.staticfiles.storage import staticfiles_storage
from celery import shared_task
from django.http import HttpResponse, JsonResponse
import random
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class SignUp(CreateView):
    template_name = "registration/signup.html"
    form_class= SignUpForm
    success_url='/'

class IndexView(LoginRequiredMixin,TemplateView):
    template_name = "index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        trader = self.request.user
        Trades = Trade.objects.filter(trader=trader)
        time_data=self.get_time_data()
        total_profit_loss=Trade.get_total_profit_loss(trader)
        total_balance=Trade.get_total_balance(trader)
        # random_trades = generate_random_trades_periodically.delay(self, minutes=1.0)
        total_trade_count = Trade.get_total_trade(trader)
        profit_loss_data = self.get_profit_loss_data()
        percentage_increase, percentage_decrease = self.calculate_percentage_changes(profit_loss=total_profit_loss, balance=100)
        percentage_increase_balance, percentage_decrease_balance = self.calculate_percentage_changes_balance(total_balance=total_balance)

        
        context={
            'Trades':Trades,'profit_loss_data':profit_loss_data,
            'time_data':time_data,'total_profit_loss':total_profit_loss,
            'total_balance':total_balance,'total_trade_count':total_trade_count,
            'percentage_increase':percentage_increase,'percentage_decrease':percentage_decrease,
            'percentage_increase_balance':percentage_increase_balance,'percentage_decrease_balance':percentage_decrease_balance}
        
        return context
    


    def get_profit_loss_data(self):
        trader = self.request.user
        trades = Trade.objects.filter(trader=trader)
        data = [float( trade.profit_loss) for trade in trades]
        return data
    def get_time_data(self):
        trader = self.request.user
        trades = Trade.objects.filter(trader=trader)
        data = [( trade.timestamp.strftime('%m/%d %H:%M')) for trade in trades]
        return data
    def calculate_percentage_changes(self, profit_loss, balance):
        if balance == 0:
            return 0.0, 0.0
        percentage_increase = round((profit_loss / balance) * 100, 2)
        percentage_decrease = round(((balance - profit_loss) / balance) * 100, 2)
        return percentage_increase, percentage_decrease
    
    def calculate_percentage_changes_balance(self, total_balance):
        account_balance = 100  # Get the initial account balance
        if account_balance == 0:
            return 0.0, 0.0
        percentage_increase = round(((total_balance - account_balance) / account_balance) * 100, 2)
        percentage_decrease = round(((account_balance - total_balance) / account_balance) * 100, 2)
        return percentage_increase, percentage_decrease

    def generate_random_trade(self):
        profit_loss = round(random.uniform(-100, 100), 2)
        trade = Trade(trader=self.request.user, profit_loss=profit_loss)
        trade.save()
        return trade
    

    def generate_random_trades_periodically(self, minutes):
        trade=0
        while True:
            total_balance = Trade.get_total_balance(self.request.user)
            total_trade_count = Trade.get_total_trade(self.request.user)

            if total_balance < 0 or total_trade_count > 200:
                break
            
            trade=generate_random_trade.delay(self)
            time.sleep(minutes * 60)
        return trade
class UpdateChartDataView(View):
     def get(self, request, *args, **kwargs):
        view = IndexView.as_view()
        response = view(request, *args, **kwargs)
        generate_random_trade(self)
        random_trades = IndexView.generate_random_trades_periodically(self, minutes=1.0)
        new_profit_loss_data = response.context_data['profit_loss_data']
        time_data = response.context_data['time_data']
        
        context={
            'new_profit_loss_data': new_profit_loss_data, 
            'time_data': time_data,
            }
        
        return JsonResponse(context, content_type="application/json")
# class ChartDataSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Trade
#         fields = ('profit_loss', 'timestamp')
    

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
    