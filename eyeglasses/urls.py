# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

admin.site.site_header = u'Eyeglasses'

urlpatterns = patterns('',
    url(r'^', include('attachment.urls')),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^feedback/', include('eyeglasses.custom_feedback.urls')),
    url(r'^catalog/', include('catalog.urls')),
    url(r'^', include('eyeglasses.custom_catalog.urls')),
    url(r'^(?P<path>.*)$', 'pages.views.details', name='pages-details-by-path'),
    url(r'^$', 'pages.views.details', name='pages-root', kwargs={'path': u''}),
)
