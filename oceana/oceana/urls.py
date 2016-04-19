from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [


    url(r'^admin/', include(admin.site.urls)),
    url(r'^enquiry/$','travel.views.enquiry'),
    url(r'^$','travel.views.main'),
    url(r'^guest/$','travel.views.guest'),
    url(r'^travel/guests/$','travel.views.AllGuest'),
    url(r'^travel/enquiry/$','travel.views.AllEnquiry'),

]


