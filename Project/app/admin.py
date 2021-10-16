from django.contrib import admin
from .models import User, Product, Transaction

# Register your models here.
admin.site.register(User)
admin.site.register(Product)
admin.site.register(Transaction)
admin.site.site_header = 'Stadorm'