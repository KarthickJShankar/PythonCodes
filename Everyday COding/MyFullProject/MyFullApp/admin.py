from django.contrib import admin
from .models import MyModel

# Register your models here.
class MyAdminClass(admin.ModelAdmin):
    List_Fields = ['id','name','age']
admin.site.register(MyModel)
