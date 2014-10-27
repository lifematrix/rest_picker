__author__ = 'steven'

from django.conf.urls import patterns, url
from django.views.generic import ListView
from .models import Food
from django.conf import settings

urlpatterns = patterns('restaurants.views',
    url(r'^$',
        ListView.as_view(
            model=Food,
            template_name='restaurants/index.html'),
        name='index'),
    url(r'^food/(?P<food_id>\d+)/$', 'choose_town', name='choose_town'),
    url(r'^food/(?P<food_id>\d+)/town/(?P<town_id>\d+)/$', 'choose_restaurant', name='choose_restaurant'),
    url(r'^rest/(?P<rest_id>\d+)/$', 'restaurant', name='restaurant'),
    url(r'^(?P<rest_id>\d+)/vote/$', 'vote', name='vote'),
    )

print('settings.DEBUG: %r' % settings.DEBUG)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))