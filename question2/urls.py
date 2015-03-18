from django.conf.urls import patterns, include, url
from django.contrib import admin
from question2.view import fibo

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'question2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^fibo/(?P<fabnum>\d+\.\d)', fibo, name='fibo_decimal'),
    url(r'^fibo/(?P<fabnum>[^\.]+)', fibo, name='fibo')
)
