from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import get_user
from django.contrib.auth.decorators import login_required
from store.models import Cart, Order, Product
from django.shortcuts import get_object_or_404



# Create your views here.
class ProductHandler:

    @staticmethod
    def store_products(request):
        
        #return HttpResponse('<h1>Hello World</h1>')
        products = Product.objects.all()

        return render(request, 'store/products.html', context={'products' : products})


    @staticmethod
    def store_product_details(request, slug, categoryId, productId):
        """
        Pourquoi ne pas avoir récupérer les document et les filtrer en function de l'id pour affciher les le 
        detail d'un produit précis. Est ce que cette méthode est meilleur, plus performante ?
        """

        product = get_object_or_404(Product, slug=slug)
        relatedProducts = Product.objects.filter(category__exact = categoryId).exclude(id=productId)[:4]


        return render(request, 'store/productDetails.html', context={'product':product, 'relatedProducts':relatedProducts})
        #return HttpResponse('Product details')


class CartHandler:

    @staticmethod
    @login_required
    def manageCart(request, slug):

        product = get_object_or_404(Product, slug=slug)

        request.user.add_to_cart(product)

        return redirect( reverse('details', kwargs={"slug":slug, "categoryId":product.category.id, "productId":product.id}) )


    @staticmethod
    def cart(request):

        cart = get_object_or_404(Cart, user=request.user)

        orders = cart.orders.filter(ordered__exact=False)

        totalPrice = 0

        for order in orders :
            totalPrice += order.quantity * order.product.price

        return render(request, 'store/cart.html', context={'orders': orders, 'totalPrice': totalPrice})
    

    @staticmethod
    def remove_order_from_cart(request, orderId):
        
        order = get_object_or_404(Order, id=orderId)

        if order.status == 'notYetAccepted' :
            order.delete(keep_parents=True)

        return redirect('cart')
    

class OrderHandler:

    @staticmethod
    def show_order(request):

        cart = get_object_or_404(
            Cart,
            user=request.user,
        )

        orders = cart.orders.filter(ordered__exact=True)

        totalPrice = 0

        for order in orders :
            totalPrice += order.quantity * order.product.price

        return render(request, 'store/orders.html', context={'orders':orders, 'totalPrice':totalPrice})


    @staticmethod
    def order(request, orderId):
        
        order = get_object_or_404(Order, id=orderId)

        order.ordered = True
        order.save()

        return redirect('cart')
    
    @classmethod
    def remove_order(self, request, orderId):
        
        order = get_object_or_404(Order, id=orderId)

        if order.status == 'notYetAccepted' :
            order.delete(keep_parents=True)

        return redirect('orders')