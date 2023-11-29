from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm

# Register your models here.

admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(ProductInCart)
admin.site.register(Order)
admin.site.register(Deal)
# admin.site.register(CustomUser)
admin.site.register(Customer)
admin.site.register(Seller)

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email','is_staff','is_active')
    list_filter = ('email','is_staff','is_active')
    fieldsets = (
        (None,{'fields':('email','password')}),
        ('Permission',{'fields':('is_staff','is_active',"is_customer","is_seller")}),
    )
    add_fieldsets =(
        (None,{
            'classes':('wide',),
            'fields':('email','password','password2','is_staff','is_active')
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)

# admin.site.unregister(User)
admin.site.register(CustomUser, CustomUserAdmin)
# admin.site.register(User,UserAdmin)


class ProductInCartInline(admin.TabularInline):
    model = ProductInCart

class CartInline(admin.TabularInline):
    model = Cart

class DealInline(admin.TabularInline):
    model = Deal.user.through

# class UserAdmin(UserAdmin):
#     model = User
#     list_display=('username','get_cart','is_staff','is_active')
#     list_filter = ('username','is_staff','is_active')
#     fieldsets = (
#         (None,{'fields':('username','password')}),
#         ('Permissions',{'fields':('is_staff',('is_active','is_superuser'),)}),
#         ('Important dates',{'fields':('last_login','date_joined')}),
#         ('Advanced options',{
#             'classes':('collapse'),
#             'fields':('groups','user_permissions'),
#         })
#     )
#     add_fieldsets = (
#         (None,{
#             'classes':('wide'),
#             'fields':('username','password','password2','is_staff','is_superuser','groups')
#         })
#     )
#     inline= [
#         CartInline,DealInline
#     ]

#     def get_cart(self,obj):
#         return obj.cart
#     search_fields=('username',)
#     ordering= ('username',)


# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)