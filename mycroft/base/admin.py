from django.contrib import admin

from models import *

for model in [Product, Video, Lecturer, Series, Poet, Poem, Lecture, Testimonial]:
     admin.site.register(model)
