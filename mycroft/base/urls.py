"""urlconf for the base application"""

from django.conf.urls.defaults import url, patterns

urlpatterns = patterns('mycroft.base.views',
    url(r'^$', 'index', name='index'),
    url(r'^store/$', 'store', name='store'),
    url(r'^lecture/(?P<poet_last_name>\w+)/(?P<poem_title>[\w\s\d\.\-]+)/?$', 'lecture', name='lecture'),
    # url(r'^order/(?P<order_reference>[\w\d]+)/', 'order', name='order'),
    url(r'^story/$', 'story', name='story'),
    url(r'^testimonials/$', 'testimonials', name='testimonials'),
    url(r'^contact/$', 'contact', name='contact'),
    url(r'^thanks/$', 'thanks', name='thanks')
)
