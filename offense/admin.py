from django.contrib import admin

# Register your models here.
from .models import Student, Note, Offense

admin.site.register(Student)
admin.site.register(Note)
admin.site.register(Offense)
