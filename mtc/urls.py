from django.conf.urls.defaults import patterns, include, url
from django.views.generic import DetailView
from mtc.membership.models import Member, Parish, FamilyMember

#from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#from mtc.settings import DEBUG

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mtc.views.home', name='home'),
    # url(r'^mtc/', include('mtc.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    (r'^tiny_mce/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/home/sa-user/workspace/mtc/staticfiles/jscripts/tiny_mce'}),
    (r'^css/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/home/sa-user/workspace/mtc/staticfiles/css'}),
    (r'^search/$', 'mtc.search.views.search'),
    (r'^members/directory/$', 'mtc.membership.views.directoryview'),
    (r'^members/directory/dirpdf/$', 'mtc.membership.views.render_to_pdf2'),
 #(r'^members/(?P<pk>\d+)/directory/$', DetailView.as_view(model=Members, context_object_name="members_list")),
    (r'', include('django.contrib.flatpages.urls')),
)



#urlpatterns += staticfiles_urlpatterns()