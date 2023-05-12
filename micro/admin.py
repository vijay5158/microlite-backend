from django.contrib import admin
from .models import Category,SubCategory,Product,Solution
# Register your models here.


admin.site.register(SubCategory)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Solution)