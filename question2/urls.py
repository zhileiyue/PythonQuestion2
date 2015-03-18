from django.conf.urls import patterns, include, url
from django.contrib import admin
from question2.view import fibo

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^fibo/(?P<fabnum>\d+\.\d)', fibo, name='fibo_decimal'),
    url(r'^fibo/(?P<fabnum>[^\.]+)', fibo, name='fibo')
)
