"""urlconf for the base application"""

from django.conf.urls.defaults import url, patterns


urlpatterns = patterns('mycroft.base.views',
    url(r'^$', 'home', name='home'),
)
