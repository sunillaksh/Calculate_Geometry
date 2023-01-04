from django.contrib import admin
from note_geometry.models import Student_note

# Register your models here.

class usernote(admin.ModelAdmin):
    list_display = ('user','note_sub', 'note_title','note_para')

admin.site.register(Student_note,usernote)