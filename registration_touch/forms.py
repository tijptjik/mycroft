"""Custom registration forms that requires only an email address as a username."""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from registration_email.forms import get_md5_hexdigest

def generate_username(email):
    """
    Generates a unique username for the given email.

    The username will be an md5 hash of the given email. If the username exists
    we just append `a` to the email until we get a unique md5 hash.

    """
    try:
        User.objects.get(email=email)
        print 'Cannot generate new username. A user with this email already exists.'
        return User.objects.get(email=email).username

    except User.DoesNotExist:
        pass

    username = get_md5_hexdigest(email)
    found_unique_username = False
    while not found_unique_username:
        try:
            User.objects.get(username=username)
            email = '{0}a'.format(email)
            username = get_md5_hexdigest(email)
        except User.DoesNotExist:
            found_unique_username = True
            return username


class TouchAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(TouchAuthenticationForm, self).__init__(*args, **kwargs)
        self.fields['username'] = forms.CharField(
            label="Email", max_length=256)


class TouchRegistrationForm(forms.Form):
    
    email = forms.EmailField(
        widget=forms.TextInput(),
        label="Email"
    )
   
    def clean(self):
        """
        Verifiy that the values entered into the two password fields match.

        Note that an error here will end up in ``non_field_errors()`` because
        it doesn't apply to a single field.

        """
        data = self.cleaned_data
        if not 'email' in data:
            return data
        self.cleaned_data['password1'] = 'default'
        self.cleaned_data['username'] = generate_username(data['email'])
        return self.cleaned_data
