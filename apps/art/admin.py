from django.contrib import admin

# Register your models here.
from art.models import Class, Student, Art, Tag

admin.site.register(Class)
admin.site.register(Student)
admin.site.register(Art)
admin.site.register(Tag)
