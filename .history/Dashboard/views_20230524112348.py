from django.shortcuts import render,redirect

# Create your views here.
from django.views.generic import TemplateView,CreateView,UpdateView,View
from .forms import SignUpForm
from .models import Trade,Trader
import time
# import threading
from django.http import JsonResponse
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
        total_trade_count = Trade.get_total_trade(trader)
        profit_loss_data = self.get_profit_loss_data()
        
        context={
            'Trades':Trades,'profit_loss_data':profit_loss_data,
            'time_data':time_data,'total_profit_loss':total_profit_loss,
            'total_balance':total_balance,'total_trade_count':total_trade_count,
            }
        
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

    def generate_random_trade(self):
        profit_loss = round(random.uniform(-100, 100), 2)
        trade = Trade(trader=self.request.user, profit_loss=profit_loss)
        trade.save()
        return trade
    
    def generate_random_trades_periodically(self, minutes):
        trade = IndexView.generate_random_trade(self)
        profit_loss = trade.profit_loss
        trade=IndexView.get_profit_loss_data(self).append(float(profit_loss))
        
        time.sleep(minutes * 60)
        return trade
    
    
class UpdateChartDataView(View):
    def get(self, *args, **kwargs):
        view = IndexView.as_view()
        response = view(self.request, *args, **kwargs)
        IndexView.generate_random_trade(self)
        random_trades=IndexView.generate_random_trades_periodically(self, minutes=0.25)
        new_profit_loss_data = response.context_data['profit_loss_data']
        time_data = response.context_data['time_data']
        co
        return ({'new_profit_loss_data': new_profit_loss_data,'time_data':time_data},) 


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
    