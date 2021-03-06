"""urlconf for the base application"""

from django.conf.urls.defaults import url, patterns

urlpatterns = patterns('mycroft.base.views',
    url(r'^$', 'index', name='index'),
    url(r'^license/$', 'license', name='license'),
    url(r'^alacarte/$', 'alacarte', name='alacarte'),
    url(r'^store/$', 'store', name='store'),
    url(r'^lecture/(?P<poet_last_name>\w+)/(?P<poem_title>[\w\s\d\.\-]+)/?$', 'lecture', name='lecture'),
    url(r'^portal/(?P<institution>[\w\s\d\.\-]+)/(?P<lecture>[\w\s\d\.\-]+)/?$', 'portal_item', name='portal_item'),
    url(r'^portal/(?P<institution>[\w\s\d\.\-]+)/', 'portal', name='portal'),
    url(r'^get/(?P<username>[\w\d]+)/(?P<slug>[\w\s\d\.\-]+)/?$', 'stream', name='stream'),
    url(r'^api/client/(?P<method>\w+)/(?P<format>\w+)/$', 'client', name='clientAPI'),
    url(r'^api/login/', 'mylogin', name='mylogin'),
    url(r'^story/$', 'story', name='story'),
    url(r'^testimonials/$', 'testimonials', name='testimonials'),
    url(r'^about/$', 'about', name='about'),
    url(r'^thanks/$', 'thanks', name='thanks'),
    url(r'^subscription/done/$', 'done', name='done'),
    url(r'^subscription/cancel/$', 'cancel', name='cancel'),
)
