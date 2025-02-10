from django.contrib.auth.models import AbstractUser
from store.models import Cart, Order


# Create your models here.
class Shopper( AbstractUser ):
    pass

    def __str__(self):
        return self.username
    

    def add_to_cart(self, product):
        
        cart , _ = Cart.objects.get_or_create(user=self)
        order, created = Order.objects.get_or_create(user=self, product=product, ordered=False)

        if created :
            cart.orders.add(order)
            cart.save()

        else:
            order.quantity += 1
            order.save()