from django.conf.urls import include, url
from django.conf.urls.static import static
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf import settings
from  . import views

admin.autodiscover()
media_url = settings.MEDIA_URL.lstrip('/').rstrip('/')

urlpatterns = [
    # Examples:
    url(r'^$', views.Index, name='home'),
    url(r'^survey/(?P<id>\d+)/$', views.SurveyDetail, name='survey_detail'),
    url(r'^confirm/(?P<uuid>\w+)/$', views.Confirm, name='confirmation'),
    url(r'^privacy/$', views.privacy, name='privacy_statement'),


    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# # media url hackery. le sigh.
# urlpatterns += [
#     (r'^%s(?P<path>.*)$' % media_url, 'django.views.static.serve',
#      {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
# ]
