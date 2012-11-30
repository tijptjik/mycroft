""" Default urlconf for mycroft """

from django.conf import settings
from django.conf.urls.defaults import url, patterns, include
from session_csrf import anonymous_csrf
from django.contrib import admin
admin.autodiscover()

# django-session-csrf monkeypatcher
import session_csrf
session_csrf.monkeypatch()


def bad(request):
    """ Simulates a server error """
    1 / 0

urlpatterns = patterns('',
    (r'', include('mycroft.base.urls')),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/$', anonymous_csrf(admin.site.admin_view(admin.site.index))),
    (r'^admin/', include(admin.site.urls)),
    #url(r'^', include('debug_toolbar_user_panel.urls')),
    (r'^bad/$', bad),
)

urlpatterns += patterns('',
    (r'^mamona/', include('mamona.urls')),
    url(r'^single/$', 'sales.views.order_singleitem', name='sales-order-singleitem'),
    url(r'^multiitem/$', 'sales.views.order_multiitem', name='sales-order-multiitem'),
    url(r'^singlescreen/$', 'sales.views.order_singlescreen', name='sales-order-singlescreen'),
    url(r'^details/(?P<order_id>[0-9]+)/$', 'order.views.show_order', name='show-order'),
)

## In DEBUG mode, serve media files through Django.
if settings.DEBUG:
    # Remove leading and trailing slashes so the regex matches.
    media_url = settings.MEDIA_URL.lstrip('/').rstrip('/')
    urlpatterns += patterns('',
        (r'^%s/(?P<path>.*)$' % media_url, 'django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT}),
    )
