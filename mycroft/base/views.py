""" Views for the base application """
import os
import pytz
import urllib
import decimal
from datetime import datetime, timedelta
import posixpath


from models import *

from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.models import check_password
from django.contrib.sites.models import Site
from django.core import serializers
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail, BadHeaderError, EmailMultiAlternatives
from django.core.urlresolvers import reverse
from django.dispatch import receiver
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext, Context
from django.template.loader import render_to_string, get_template
from django.utils import simplejson 
from django.utils.safestring import mark_safe
from django.views.static import serve


from paypal.standard.forms import PayPalPaymentsForm
from paypal.standard.conf import POSTBACK_ENDPOINT, SANDBOX_POSTBACK_ENDPOINT
from paypal.standard.ipn.signals import touch_user
from paypal.standard.ipn.signals import license_user
from paypal.standard.ipn.models import PayPalIPN

from registration.backends import get_backend
from registration.signals import user_registered
from registration.views import register as registerUser
from registration_email.forms import EmailRegistrationForm
from registration_touch.forms import TouchRegistrationForm

from subscription.models import Subscription, UserSubscription
from subscription.views import _paypal_form



USE_XSENDFILE = getattr(settings, 'USE_XSENDFILE', False)

PAYPAL_FORM = u"""
        <form id="subscriptionForm" action="%s" method="post" class="hidden">
            %s
            <input type="hidden" name="upload" value="1">
            <input id="checkoutSubscription" type="submit" class="btn pull-right btn-danger" value="Checkout with PayPal" alt="Checkout with PayPal" />
        </form>"""

def index(request):
    lectures = Lecture.objects.all().order_by('poem__poet__last_name')
    institutions = Institution.objects.all()
    for lecture in lectures:
        lecture.poem.poet.slug = lecture.poem.poet.last_name.lower()
    return render(request, 'base/index.html', {'lectures': lectures, 'institutions':institutions})

def license(request):
    subscriptions = Subscription.objects.get(id=1)
    form_class = EmailRegistrationForm
    form = form_class()

    genericUser = get_object_or_404(User, id=1)
    endpoint = (SANDBOX_POSTBACK_ENDPOINT if settings.PAYPAL_TEST else POSTBACK_ENDPOINT)

    # Create the instances.
    subscription = _paypal_form(get_object_or_404(Subscription, id=1), genericUser, upgrade_subscription=False, invoice=genInvoiceID('L'))
    subscriptionForm = mark_safe(PAYPAL_FORM % (endpoint, subscription.as_p()))

    lectures = Lecture.objects.all().order_by('poem__poet__last_name')
    for lecture in lectures:
        lecture.poem.poet.slug = lecture.poem.poet.last_name.lower()

    context = dict(
        lecture_list=lectures,
        subscription=subscriptions,
        form=form,
        subscription_form=subscriptionForm,
    )
    
    return render(request, 'base/license.html', context)

def alacarte(request):
    form_class = EmailRegistrationForm
    form = form_class()

    genericUser = get_object_or_404(User, id=1)
    endpoint = (SANDBOX_POSTBACK_ENDPOINT if settings.PAYPAL_TEST else POSTBACK_ENDPOINT)

    student_dict = {
        'cmd': '_cart',
        "business": settings.PAYPAL_RECEIVER_EMAIL,
        "discount_rate_cart": '0',
        "invoice": genInvoiceID('C'),
        "payer_email": '',
        "notify_url": "%s%s" % (settings.SITE_NAME, reverse('paypal-ipn')),
        "return_url": "%s%s" % (settings.SITE_NAME, '/thanks/'),
        "cancel_return": "%s%s" % (settings.SITE_NAME, '/cancel/'),
    }

    print 'STUDENT DICT:'
    print student_dict
    # Create the instances.
    student = PayPalPaymentsForm(initial=student_dict, button_class="pull-right btn-danger", button_text="Select your Lectures", button_type="bootstrap")
    

    lectures = Lecture.objects.all().order_by('poem__poet__last_name')
    for lecture in lectures:
        lecture.poem.poet.slug = lecture.poem.poet.last_name.lower()

    context = dict(
        lecture_list=lectures,
        student=student,
        form=form,
    )
    
    return render(request, 'base/alacarte.html', context)


def lecture(request, poet_last_name=None, poem_title=None):
    lecture = get_object_or_404(Lecture, slug=poem_title)
    if not lecture.poem.poet.year_of_death:
        lecture.poem.poet.year_of_death = 'Current'

    duration = lecture.video.duration / 60

    paypal_dict = {
        "business": settings.PAYPAL_RECEIVER_EMAIL,
        "amount": lecture.product.price_in_dollars,
        "item_name": lecture.title,
        "item_number": lecture.id,
        "invoice": genInvoiceID('S'),
        "notify_url": "%s%s" % (settings.SITE_NAME, reverse('paypal-ipn')),
        "return_url": "%s%s" % (settings.SITE_NAME, '/thanks/'),
        "cancel_return": "%s%s" % (settings.SITE_NAME, '/cancel/'),
    }

    form = PayPalPaymentsForm(initial=paypal_dict, button_class="btn-primary", button_text="BUY", button_type="bootstrap")
    context = {'lecture': lecture, "form": form, "duration": duration}
    return render(request, 'base/lecture.html', context)

def store(request, extra_context=None):
    subscriptions = Subscription.objects.get(id=1)
    form_class = EmailRegistrationForm
    form = form_class()

    genericUser = get_object_or_404(User, id=1)
    endpoint = (SANDBOX_POSTBACK_ENDPOINT if settings.PAYPAL_TEST else POSTBACK_ENDPOINT)

    student_dict = {
        'cmd': '_cart',
        "business": settings.PAYPAL_RECEIVER_EMAIL,
        "discount_rate_cart": '0',
        "invoice": genInvoiceID('C'),
        "payer_email": '',
        "notify_url": "%s%s" % (settings.SITE_NAME, reverse('paypal-ipn')),
        "return_url": "%s%s" % (settings.SITE_NAME, '/thanks/'),
        "cancel_return": "%s%s" % (settings.SITE_NAME, '/cancel/'),
    }

    # Create the instances.
    student = PayPalPaymentsForm(initial=student_dict, button_class="pull-right btn-danger", button_text="Select your Lectures", button_type="bootstrap")
    subscription = _paypal_form(get_object_or_404(Subscription, id=1), genericUser, upgrade_subscription=False, invoice=genInvoiceID('L'))
    subscriptionForm = mark_safe(PAYPAL_FORM % (endpoint, subscription.as_p()))

    context = dict(
        lecture_list=Lecture.objects.all(),
        subscription=subscriptions,
        student=student,
        form=form,
        subscription_form=subscriptionForm,
    )
    
    if extra_context is None:
        extra_context = {}
    for key, value in extra_context.items():
        context[key] = callable(value) and value() or value
    
    return render(request, 'base/store.html', context)
    
def story(request):
    return render(request, 'base/story.html')

def testimonials(request):
    testimonials = Testimonial.objects.all()
    return render(request, 'base/testimonials.html', {"testimonials": testimonials})

def contact(request):
    return render(request, 'base/contact.html')

def about(request):
    return render(request, 'base/about.html')

def thanks(request):
    return render(request, 'base/thanks.html')

def done(request):
    return render(request, 'base/congratulations.html')

def cancel(request):
    return render(request, 'base/cancel.html')

def mylogin(request):
    print 'received'
    if request.is_ajax():
        if request.method == 'GET':
            return HttpResponse('GET not supported')
        elif request.method == 'POST': 
            userpass = request.POST['password']
            print userpass
            userid = int(request.POST['userid'])
            print userid
            user = User.objects.get(id=userid)
            print user
            result = check_password(userpass,user.password)
            print result

            data = {'match':result}
            return HttpResponse(simplejson.dumps(data), content_type='application/javascript; charset=utf8')

    else:
        return HttpResponse('ERROR')

def client(request, method, format):

    if format == 'xml':
        mimetype = 'application/xml'
    if format == 'json':
        mimetype = 'application/javascript; charset=utf8'

    if request.is_ajax():
        if request.method == 'GET':
            return HttpResponse('GET not supported')
        elif request.method == 'POST':
            if method == 'student':
                backend = 'registration.backends.default.DefaultBackend'
                print request.POST
                form_class = TouchRegistrationForm
                try:
                    email = request.POST['email']
                    User.objects.get(email=email)
                    print 'Cannot generate new username. A user with this email already exists.'
                    touch_user = User.objects.get(email=email)
                except User.DoesNotExist:
                    touch_user = registerUser(request=request, backend=backend, form_class=form_class, deferred=True)
                    print 'NEW USER CREATED:'
                    print touch_user
                data = serializers.serialize(format, [touch_user, ])
                print data
            elif method == 'educator':
                print 'REGISTERED USER MAIL'
                backend = 'registration.backends.institutional.InstitutionalBackend'
                print backend
                print
                form_class = EmailRegistrationForm
                print form_class
                print
                
                new_user = registerUser(request=request, backend=backend, form_class=form_class, deferred=True)
                print new_user
                print
                text_template = 'base/mail-newuser.txt'
                print text_template
                print
                html_template = 'base/mail-newuser.html'
                print html_template
                print
                sendMail(to=request.POST['email'],
                    subject="Welcome to Mycroft Lectures",
                    payload=Context({'user':new_user, 'email': settings.EMAIL_HOST_USER, 'password': request.POST['password1']}),
                    text_template=text_template,
                    html_template=html_template)
                print sendMail
                print 
                data = serializers.serialize(format, [new_user, ])
                print data
                print
            return HttpResponse(data, content_type=mimetype)
    else:
        return HttpResponse('ERROR')

def portal(request, institution):
    institution = get_object_or_404(Institution, slug=institution)
    lectures = Lecture.objects.all()
    if not "institution has valid account":
        expired = True
    else:
        expired = False

    context = {
        'lectures': lectures,
        'institution' : institution,
        'expired': expired
        }
    return render(request, 'base/portal.html', context)

def portal_item(request, institution, lecture):
    institution = get_object_or_404(Institution, slug=institution)
    if not "institution has valid account":
        expired = True
    else:
        expired = False
        lecture = get_object_or_404(Lecture, slug=lecture)
        if not lecture.poem.poet.year_of_death:
            lecture.poem.poet.year_of_death = 'Current'

    context = {
        'lecture': lecture,
        'institution' : institution,
        'expired': expired}
    return render(request, 'base/portal_item.html', context)

def stream(request, username, slug):
    try:
        user = User.objects.get(username=username)
    except:
        return HttpResponse('ERROR')

    lecture = get_object_or_404(Lecture, slug=slug)
    access = Access.objects.get(lecture=lecture, user=user)
    if access.active:
        return HttpResponse(lecture.video.video)
    else:
        return HttpResponse('LINK EXPIRED')

def xsendfileserve(request, path, document_root=None):
    """
    Serve static files using X-Sendfile below a given point 
    in the directory structure.

    This is a thin wrapper around Django's built-in django.views.static,
    which optionally uses USE_XSENDFILE to tell webservers to send the
    file to the client. This can, for example, be used to enable Django's
    authentication for static files.

    To use, put a URL pattern such as::

        (r'^(?P<path>.*)$', login_required(xsendfileserve), 
                            {'document_root' : '/path/to/my/files/'})

    in your URLconf. You must provide the ``document_root`` param. You may
    also set ``show_indexes`` to ``True`` if you'd like to serve a basic index
    of the directory.  This index view will use the template hardcoded below,
    but if you'd like to override it, you can create a template called
    ``static/directory_index.html``.
    """

    if USE_XSENDFILE:
        # This code comes straight from the static file serve
        # code in Django 1.2.

        # Clean up given path to only allow serving files below document_root.
        path = posixpath.normpath(urllib.unquote(path))
        path = path.lstrip('/')
        newpath = ''
        for part in path.split('/'):
            if not part:
                # Strip empty path components.
                continue
            drive, part = os.path.splitdrive(part)
            head, part = os.path.split(part)
            if part in (os.curdir, os.pardir):
                # Strip '.' and '..' in path.
                continue
            newpath = os.path.join(newpath, part).replace('\\', '/')
        if newpath and path != newpath:
            return HttpResponseRedirect(newpath)
        fullpath = os.path.join(document_root, newpath)

        # This is where the magic takes place.
        response = HttpResponse()
        response['X-Sendfile'] = fullpath
        # Unset the Content-Type as to allow for the webserver
        # to determine it.
        response['Content-Type'] = ''

        return response

    return serve(request, path, document_root)

@receiver(license_user)
@receiver(touch_user)
def mailUser(sender, **kwargs):
    print 'SIGNAL RECEIVED'
    print 'Active User:', sender.get('txn_type')
    
    pid = sender['payer_id']
    
    if type(pid) == list:
        pid = pid[0]
    
    user = User.objects.get(id=pid)
    to = User.objects.get(id=pid).email
    print 'To:', to
    
    if sender.get('txn_type') in ['subscr_signup']:
        print 'SUBCRIBER SIGNUP'
        itemid = sender['item_number']
        if type(itemid) == list:
            itemid = itemid[0]
        
        institution = Institution.objects.get(contact=user)
        license = Subscription.objects.get(id=int(itemid))
        subject = 'Mycroft Lectures License'
        period = int(license.recurrence_period)
        if license.recurrence_unit == 'Y':
            period = period * 12;
        times = datetime.now(pytz.utc) + timedelta(days=period*30)
        payload = Context({
            'site': Site.objects.get_current(),
            'email': settings.EMAIL_HOST_USER,
            'institution':institution,
            'user': user,
            'expiry': times.strftime("%A, %d %B %Y"),
            'license': license,
            'lectures' : Lecture.objects.all()
            })
        print 'Payload: '
        print payload
        text_template = 'base/mail-educator.txt'
        html_template = 'base/mail-educator.html'
    elif sender.get('txn_type') in ['subscr_payment']:
        pass
    else:
        print 'INDIVIDUAL PURCHASE'
        subject = 'Mycroft Lectures purchase'
        times = datetime.now(pytz.utc) + timedelta(days=settings.DOWNLOAD_EXPIRATION_DAYS)
        payload = Context({
            'site': Site.objects.get_current(),
            'email': settings.EMAIL_HOST_USER,
            'user': user,
            'expiry': times.strftime("%A, %d %B %Y"),
            'lectures' : Lecture.objects.filter(access__user=user).all()
            })
        text_template = 'base/mail-student.txt'
        html_template = 'base/mail-student.html'

    sendMail(to, subject, payload, text_template, html_template, )


def sendMail(to, subject, payload={}, text_template=None, html_template=None):
    from_email = settings.DEFAULT_FROM_EMAIL
    plaintext = get_template(text_template)
    htmly     = get_template(html_template)
   
    text_content = plaintext.render(payload)
    html_content = htmly.render(payload)
    
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to,])
    if html_content:
        msg.attach_alternative(html_content, "text/html")
    
    msg.send()
    
def genInvoiceID(typer):
    invoices = len(PayPalIPN.objects.filter(payment_type__startswith="instant"))
    no = "%04d" % (invoices + 1)
    return "MYCORFT"+ str(no) + typer + datetime.now().strftime("%d%H%M%S")
