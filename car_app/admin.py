from django.contrib import admin
from car_app.models import TruckNumber, TruckModel, Post

# Register your models here.


class TruckModelAdmin(admin.ModelAdmin):
    fields = ['model_name', 'max_capacity', 'model_description']


class TruckNumberAdmin(admin.ModelAdmin):
    fields = ['bort_number',  'model_name', 'current_weight', 'truck_number_description', 'registration_date', 'current_work_start_date']


admin.site.register(Post)
admin.site.register(TruckModel)
admin.site.register(TruckNumber)

