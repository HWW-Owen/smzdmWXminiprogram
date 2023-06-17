from django.contrib import admin

# Register your models here.
from .models import Category,Product,UserProduct,AppUser,Comment,Subscribe

admin.site.register(AppUser)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(UserProduct)
admin.site.register(Comment)
admin.site.register(Subscribe)



