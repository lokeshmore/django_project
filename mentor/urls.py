from django.urls import path,include
from .  import views

urlpatterns = [
    path('index',views.index,name="index"),
    path('about',views.about,name="index"),
    path('courses',views.courses,name="index"),
    path('trainers',views.trainers,name="index"),
    path('events',views.events,name="events"),
    path('pricing',views.pricing,name="index"),
    path('contact',views.contact,name="index"),
    path('course-details',views.course_details,name="index"),
    
]