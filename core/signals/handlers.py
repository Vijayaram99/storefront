from store.signals import order_created
from store.signals import order_created

def on_order_created(sender, **kwargs):
    print(kwargs['order'])