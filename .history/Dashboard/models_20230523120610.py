from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from django.utils import timezone
import random

# Create your models here.
class Trader(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    account_balance = models.DecimalField(max_digits=10, decimal_places=2,default=100.00)
    
    def __str__(self):
        return str(self.name)
    

def generate_random_float():
    return round(random.uniform(-100, 100), 2)

class Trade(models.Model):
    trader = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    profit_loss = models.DecimalField(max_digits=10, decimal_places=2,default=generate_random_float)
    
    def get_time_data():
        trades = Trade.objects.all()
        data = [( trade.timestamp.strftime('%H:%M')) for trade in trades]
        return data
    
   

    @staticmethod
    def get_total_profit(user):
        total_profit = Trade.objects.filter(trader=user).aggregate(profit=Sum('profit_loss', filter=models.Q(profit_loss__gt=0)))['profit']
        return total_profit or 0

    @staticmethod
    def get_total_loss(user):
        total_loss = Trade.objects.filter(trader=user).aggregate(loss=Sum('profit_loss', filter=models.Q(profit_loss__lt=0)))['loss']
        return total_loss or 0

    @staticmethod
    def get_total_profit_loss(user):
        total_profit = Trade.get_total_profit(user)
        total_loss = Trade.get_total_loss(user)
        total_profit_loss = total_profit + total_loss
        return total_profit_loss

    @staticmethod
    def get_total_balance(user):
        total_profit_loss=Trade.get_total_profit_loss(user)
        acct_balance=Trader.account_balance
        total_balance = (total_profit_loss + 100)
        return total_balance or 0
    
    def get_total_trade(user):
        return Trade.objects.filter(trader=user).count()

