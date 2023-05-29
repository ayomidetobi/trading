from celery import shared_task
import time
import random
from .models import Trade
@shared_task
def generate_random_trade(self):
    profit_loss = round(random.uniform(-100, 100), 2)
    trade = Trade(trader=self.request.user, profit_loss=profit_loss)
    trade.save()
    return trade
    
@shared_task
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