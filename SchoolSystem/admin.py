from django.contrib import admin
from .models import (
    Trade, Student, Graduate_year, Fixed_Fee, Fixed_Fee_Day
)
# Register your models here.
admin.site.register(Trade)
admin.site.register(Student)
admin.site.register(Graduate_year)
admin.site.register(Fixed_Fee)
admin.site.register(Fixed_Fee_Day)