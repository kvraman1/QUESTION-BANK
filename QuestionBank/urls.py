"""QuestionBank URL Configuration

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
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^Qbank/', include('Qbank.urls')),
    url(r'^admin/', include(admin.site.urls)),
]

admin.site.site_header = ('DEPARTMENT OF COMPUTER SCIENCE QUESTION BANK SITE ADMIN')
admin.site.site_title = ('COMPUTER SCIENCE SITE ADMIN')

#checks if the project is run in DEBUG mood
#setting url for serving media fille, media uploads
if settings.DEBUG:
    urlpatterns += patterns('',(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root': settings.MEDIA_ROOT}), 
    )