from django.shortcuts import render,redirect

# Create your views here.
from django.views.generic import TemplateView,CreateView
from .forms import SignUpForm
from .models import Trade
import time
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
        time_data=Trade.get_time_data()
        total_profit_loss=Trade.get_total_profit_loss(trader)
        total_balance=Trade.get_total_balance(trader)
        total_trade_count = Trade.get_total_trade(trader)
        profit_loss_data = self.get_profit_loss_data()
        random_trades=self.generate_random_trades_periodically( minutes=1, num_trades=1)
        
        get_all_data=profit_loss_data.extend(random_trades)
        print()
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

    def generate_random_trade(self):
        profit_loss = round(random.uniform(-100, 100), 2)
        trade = Trade(trader=self.request.user, profit_loss=profit_loss)
        trade.save()
        return trade
    
    def generate_random_trades_periodically(self, minutes, num_trades):
        trades = []
        for _ in range(num_trades):
            trade = self.generate_random_trade()
            trades.append(trade.profit_loss)
            time.sleep(minutes * 60)
        return trades
    

class ProfileView(TemplateView):
    template_name = "users-profile.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context["users"] = Trade.objects.filter(trader=user)
        return context
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