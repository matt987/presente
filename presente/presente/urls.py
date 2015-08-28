from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.http import HttpResponseRedirect
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'presente.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    (r'^$', lambda r: HttpResponseRedirect('admin/')),
)
