from django.shortcuts import render
from mentor.models import Course,Trainers,Testimonials


# Create your views here.
def index(request):
    content={}
    content['data']=Course.objects.all()
    content['tdata']=Trainers.objects.all()
    content['rdata']=Testimonials.objects.all()
    #print(content['rdata'])
    return render(request,'index.html',content)


def about(request):
    return render(request,'about.html')

def courses(request):
    return render(request,'courses.html')

def trainers(request):
    return render(request,'trainers.html')

def events(request):
    return render(request,'events.html')

def pricing(request):
    return render(request,'pricing.html')

def contact(request):
    return render(request,'contact.html')


def course_details(request):
    return render(request,'course-details.html')