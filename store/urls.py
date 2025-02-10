from .views import ProductHandler, CartHandler, OrderHandler
from django.urls import path
 
urlpatterns = [
    path('products/', ProductHandler.store_products, name='products'),
    path('products/<str:slug>/<int:categoryId>/<int:productId>/', ProductHandler.store_product_details, name='details'),
    path('products/<str:slug>/add_to_cart/', CartHandler.manageCart, name='add_to_cart'),
    path('cart/', CartHandler.cart, name='cart'),
    path('cart/remove_order_from_cart/<int:orderId>/', CartHandler.remove_order_from_cart, name='remove_order_from_cart'),
    path('orders/', OrderHandler.show_order, name='orders'),
    path('cart/order/<int:orderId>/', OrderHandler.order, name='order'),
    path('order/remove_order/<int:orderId>/', OrderHandler.remove_order, name='remove_order'),
] 