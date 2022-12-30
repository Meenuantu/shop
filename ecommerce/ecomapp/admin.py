from django.contrib import admin

# Register your models here.
from .models import Product,Category

class categoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category,categoryAdmin)

class productAdmin(admin.ModelAdmin):
    list_display = ['name','price','stock','category','available_yes_no','created_on','updated_on']
    list_editable = ['price','stock','available_yes_no']
    prepopulated_fields = {'slug':('name',)}
    list_per_page = 20

admin.site.register(Product,productAdmin)



