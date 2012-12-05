""" Views for the base application """
from coffin.shortcuts import render, get_object_or_404
from paypal.standard.forms import PayPalPaymentsForm
from models import *
from django.conf import settings
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt

def index(request):
    lectures = Lecture.objects.all()
    for lecture in lectures:
        lecture.poem.poet.slug = lecture.poem.poet.last_name.lower()
    return render(request,'base/index.html', {'lectures': lectures})

def lecture(request, poet_last_name=None, poem_title=None):
    lecture = get_object_or_404(Lecture, slug=poem_title)
    if not lecture.poem.poet.year_of_death:
        lecture.poem.poet.year_of_death = 'Current'
    
    paypal_dict = {
        "business": settings.PAYPAL_RECEIVER_EMAIL,
        "amount": lecture.product.price_in_dollars,
        "item_name": 'Mycroft Lecture on \'' + lecture.title + '\'',
        "invoice": "unique-invoice-id",
        "notify_url": "%s%s" % (settings.SITE_NAME, reverse('paypal-ipn')),
        "return_url": "%s%s" % (settings.SITE_NAME, '/thanks/'),
        "cancel_return": "%s%s" % (settings.SITE_NAME, '/cancel/'),
    }

    form = PayPalPaymentsForm(initial=paypal_dict)
    context = {'lecture': lecture, "form": form.sandbox()}
    return render(request, 'base/lecture.html', context)

def store(request):
    lecture = Lecture.objects.get(pk=1)
    total_sold = 0

    student_dict = {
        "business": settings.PAYPAL_RECEIVER_EMAIL,
        "amount": lecture.product.price_in_dollars,
        "item_name": 'Mycroft Lecture on \'' + lecture.title + '\'',
        "invoice": "unique-invoice-id",
        "notify_url": "%s%s" % (settings.SITE_NAME, reverse('paypal-ipn')),
        "return_url": "%s%s" % (settings.SITE_NAME, '/thanks/'),
        "cancel_return": "%s%s" % (settings.SITE_NAME, '/cancel/'),
    }

    institutional_dict = {
        "cmd": "_xclick-subscriptions",
        "a3": "500",                      # monthly price 
        "p3": 12,                           # duration of each unit (depends on unit)
        "t3": "M",                         # duration unit ("M for Month")
        "src": "1",                        # make payments recur
        "sra": "1",                        # reattempt payment on payment error
        "no_note": "0",                    # remove extra notes (optional)
        "item_name": "Mycroft Lecture Intstitutional Subscription",
        "business": settings.PAYPAL_RECEIVER_EMAIL,
        "notify_url": "%s%s" % (settings.SITE_NAME, reverse('paypal-ipn')),
        "return_url": "%s%s" % (settings.SITE_NAME, '/thanks/'),
        "cancel_return": "%s%s" % (settings.SITE_NAME, '/cancel/'),
    }
    
    educator_dict = institutional_dict
    educator_dict.update({
        "a3": "100",                      # monthly price 
        "p3": 6,                           # duration of each unit (depends on unit)
        "item_name": "Mycroft Lecture Educator Subscription",
    })

    # Create the instance.
    student = PayPalPaymentsForm(initial=student_dict)
    educator = PayPalPaymentsForm(initial=educator_dict, button_type="subscribe")
    institutional = PayPalPaymentsForm(initial=institutional_dict, button_type="subscribe")

    context = {'lecture': lecture, "student": student.sandbox(), "educator": educator.sandbox(), "institutional": institutional.sandbox()}
    return render(request, 'base/store.html', context)

def order(request):
    return render(request, 'base/order.html')

def story(request):
    return render(request, 'base/story.html')

def testimonials(request):
    testimonials = Testimonial.objects.all()
    return render(request, 'base/testimonials.html', {"testimonials": testimonials})

def contact(request):
    return render(request, 'base/contact.html')

@csrf_exempt
def thanks(request):
    return render(request, 'base/thanks.html')
