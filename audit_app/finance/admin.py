from django.contrib import admin
from .models import Category, Costs, Profits


admin.site.register(Costs)
admin.site.register(Category)
admin.site.register(Profits)