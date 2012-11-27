""" Views for the base application """

from coffin.shortcuts import render

from models import *


def index(request):
    return render(request,'base/index.html')

def lecture(request, poet_last_name=None, poem_title=None):
    return render(request, 'base/lecture.html')

def order(request):
    return render(request, 'base/order.html')

def contact(request):
    return render(request, 'base/contact.html')

def about(request):
    return render(request, 'base/about.html')
