from django.contrib import admin
from prizebond.models import LuckyDraw

# Register your models here.

class AdminLuckDraw(admin.ModelAdmin):
	pass

admin.site.register(LuckyDraw, AdminLuckDraw)
