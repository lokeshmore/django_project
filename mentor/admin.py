from django.contrib import admin 
from mentor.models import Course,Trainers,Testimonials

# Register your models here.
admin.site.register(Course)

admin.site.register(Trainers)
admin.site.register(Testimonials)
