""" Views for the base application """
from coffin.shortcuts import render, get_object_or_404

from models import *


def index(request):
    lectures = Lecture.objects.all()
    for lecture in lectures:
        lecture.poem.poet.slug = lecture.poem.poet.last_name.lower()
    return render(request,'base/index.html', {'lectures': lectures})

def lecture(request, poet_last_name=None, poem_title=None):
    lecture = get_object_or_404(Lecture, slug=poem_title)
    if not lecture.poem.poet.year_of_death:
        lecture.poem.poet.year_of_death = 'Current'
    return render(request, 'base/lecture.html', {'lecture': lecture})

def store(request):
    return render(request, 'base/store.html')

def order(request):
    return render(request, 'base/order.html')

def story(request):
    return render(request, 'base/story.html')

def testimonials(request):
    testimonials = Testimonial.objects.all()
    return render(request, 'base/testimonials.html', {"testimonials": testimonials})

def contact(request):
    return render(request, 'base/contact.html')

