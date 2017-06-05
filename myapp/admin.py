from django.contrib import admin

# Register your models here.
from .models import Student

class StudentAdmin(admin.ModelAdmin):
	list_display=[f.name for f in Student._meta.fields]

admin.site.register(Student,StudentAdmin)