'''
Created on 2015-04-29

@author: admin
'''
from django.conf.urls import patterns, url

urlpatterns = patterns(
    'api.views',
    url(r'cars/$', 'car_list', name='car_list'),
    url(r'cars/(?P<pk>[0-9]+)$', 'car_detail', name='car_detail'),

)