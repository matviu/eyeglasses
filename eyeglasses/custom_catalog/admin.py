# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Eyeglasses, Section

# Register your models here.

class EyeglassesAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('name',)}


class SectionAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('name',)}

admin.site.register(Eyeglasses, EyeglassesAdmin)
admin.site.register(Section, SectionAdmin)
