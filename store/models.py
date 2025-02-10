from django.db import models
from django.urls import reverse

from myshowcase.settings import AUTH_USER_MODEL



# Create your models here.
class Category (models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    thumbnail = models.ImageField( upload_to='category_images', null=True, blank=True)

    def __str__(self):
        return self.name


class Product (models.Model):

    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    price = models.FloatField(default=0.0)

    rating = models.IntegerField(
        default=0,                      
        choices=[
            (1, 'Rated 1'), 
            (2, 'Rated 2'), 
            (3, 'Rated 3'),
            (4, 'Rated 4'),
            (5, 'Rated 5'),
        ])

    stockQuantity = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    thumbnail = models.ImageField(upload_to='products_img', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date = models.DateTimeField()

    """
    La méthode spéciale __str__ permet d'indiquer la représentation en chaîne de caractères d'un objet. 
    Cette méthode doit obligatoirement retourner une chaîne de caractères.
    """
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('details', kwargs={
            'slug': self.slug,
            'categoryId': self.category.id,
            'productId': self.id
        })



# Model order

class Order(models.Model):

        #ForeignKey Cardinality : 1 - n [ 1 Shopper - n oder(s) ]
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
        #ForeignKey Cardinality : 1 - n [ 1 Proudct - n oder(s) ]
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)

    status = models.CharField(

        max_length=14,
        
        choices=[
        ('notYetAccepted', 'Not Yet accepted'),
        ('orderAborted', 'Order Aborted'),
        ('orderAccepted', 'Order Accepted'),
        ('orderPackaged', 'Order Packaged'), 
        ('orderDelivered', 'Order Delivered'),
    ],
        default='notYetAccepted',
    )


    """orderAccepted = models.BooleanField(default=False) # To check whether an order has been accepted by the seller.
    orderAborted = models.BooleanField(default=False)
    orderPackaged = models.BooleanField(default=False)
    orderDelivered = models.BooleanField(default=False) # To check whether an order has been delivered.
    orderDate = models.DateTimeField(auto_now=True, blank=True, null=True)"""

    def __str__(self):
        return self.product.name


# Cart Model

class Cart(models.Model):

        #OneToOne Cardinality : 1 - 1 ( 1 Shopper - 1 Cart )
    user = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE)
    orders = models.ManyToManyField(Order)
    #ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username