
from django.contrib import admin
from .models import myUser, Product,Category,Brand, Order

# Register your models here.
admin.site.register(myUser)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Order)
