from django.contrib import admin

from models import *

for model in [Product, Video, Lecturer, Series, Poet, Poem, Testimonial, Preview]:
     admin.site.register(model)


class LectureAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Lecture, LectureAdmin)
