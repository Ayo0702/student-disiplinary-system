from django.contrib import admin

# Register your models here.
from .models import Student, Note, Offense
class NoteInline(admin.TabularInline):
    model = Note
    extra = 1

class OffenseAdmin(admin.ModelAdmin):
    inlines = [NoteInline]

admin.site.register(Student)
admin.site.register(Note)
admin.site.register(Offense, OffenseAdmin)
