"""ludissuetracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
#from django.contrib import admin

#admin.autodiscover()

urlpatterns = patterns['',
   (r'^',include('ludissues.urls')), (r'^admin/', include(admin.site.urls)), (r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT})
]

#use ludissues model
from models import ludissues

#dictionary with all the objects in ludissues
info = {
	'queryset':ludissues.objects.all(),
}

#To save us writing lots of python code we are using the list_detail generic view lits detail is the name of the view we are using
urlpatterns = patterns('django.views.generic.list_detail', #issue-list and issue-detail are the template names which will be looked in the default template directories#
	url(r'^$','object_list',info,name='issue-list'), url(r'^(?P<object_id>\d+)/$','object_detail',info,name='issue-detail'),

)


