from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

from django.contrib.auth.models import AbstractUser,PermissionsMixin ,AbstractBaseUser
from .managers import CustomUserManager
from django.utils.translation import gettext_lazy as _

# Create your models here.

# class UserType(models.Model):
#     CUSTOMER = 1
#     SELLER = 2
#     TYPE_CHOICES = (
#         (SELLER,'SELLER'),
#         (CUSTOMER,'CUSTOMER')
#     )

#     id = models.PositiveSmallIntegerField(choices=TYPE_CHOICES,primary_key=True)

#     def __str__(self):
#         return self.get_id_display()

# class Customer(models.Model):
#     user = models.OneToOneField(User, on_delete= models.CASCADE)
#     address = models.CharField(max_length=1000)

# class Seller(models.Model):
#     user = models.OneToOneField(User, on_delete= models.CASCADE)
#     tax = models.CharField()
    

class CustomUser(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    # is_customer = models.BooleanField(default=True)
    # is_seller = models.BooleanField(default=False)


    # type = (
    #     (1,'Seller'),
    #     (2,'Customer')
    # )
    # user_type = models.IntegerField(choices = type, default=1)

    #user_type = models.ManyToManyField(UserType)

    class Types(models.TextChoices):
        SELLER= "Seller","SELLER"
        CUSTOMER = "Customer","CUSTOMER"

    default_type = Types.CUSTOMER
    type = models.CharField(_("Type"), max_length=255, choices=Types.choices, default=default_type)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.type = self.default_type
        return super().save(*args,**kwargs)

class CustomerAdditional(models.Model):
    user = models.OneToOneField(CustomUser, on_delete= models.CASCADE)
    address = models.CharField(max_length=10)


class SellerAdditional(models.Model):
    user = models.OneToOneField(CustomUser, on_delete= models.CASCADE)
    tax = models.CharField(max_length=10)
    warehouse_loc = models.CharField(max_length=100)

#model Mangers for proxy models
class SellerManager(models.Manager):
    def get_queryset(self,*args,**kwargs):
        return super().get_queryset(*args,**kwargs).filter(type=CustomUser.Types.SELLER)

class CustomerManager(models.Manager):
    def get_queryset(self,*args,**kwargs):
        return super().get_queryset(*args,**kwargs).filter(type=CustomUser.Types.CUSTOMER)
    
#proxy models.they do not create a seperate table
class Seller(CustomUser):
    default_type = CustomUser.Types.SELLER
    objects = SellerManager()
    class Meta:
        proxy:True

    def sell(self):
        print("I can sell")
    
    @property
    def showAdditional(self):
        return self.selleradditional

class Customer(CustomUser):
    default_type = CustomUser.Types.CUSTOMER
    objects = CustomerManager()
    class Meta:
        proxy:True

    def buy(self):
        print("I can buy")

    @property
    def showAdditional(self):
        return self.customeradditional



class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    prduct_name = models.CharField(max_length=255)
    price = models.FloatField()

    def __str__(self):
        return self.prduct_name
    
    
class Cart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    created_on = models.DateTimeField()

class ProductInCart(models.Model):
    class Meta:
        unique_together=(('cart','product'),)
    product_in_cart_id = models.AutoField(primary_key=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

class Order(models.Model):
    status_choices = (
        (1,"Not Packed"),
        (2,"Ready For Shipment"),
        (3,"Shipped"),
        (4,"Delivered")
    )
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    status = models.IntegerField(choices=status_choices,default=1)

class Deal(models.Model):
    user = models.ManyToManyField(CustomUser)
    deal_name = models.CharField(max_length=255)

class Contact(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=10)
    phone = models.IntegerField()
    query = models.TextField()