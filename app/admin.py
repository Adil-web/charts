from django.contrib import admin
from .models import Data, ChartType, Name

# Register your models here.
admin.site.register(Name)
admin.site.register(ChartType)
admin.site.register(Data)