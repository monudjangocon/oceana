from django.contrib import admin

from django.conf.urls import include, url,patterns
from models import Guest,Enquiry
from views import *

from django.contrib.admin import views


class GuestAdmin(admin.ModelAdmin):


    
    exclude = ('user',)
    list_display = ('image','name', 'phone', 'email',)
    search_fields = ['name', 'address']
    exclude = ('travel_time', 'updated_time',)
    list_filter=('name',)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.user = request.user
        obj.save()    
    
    def queryset(self, request):
        qs = super(GuestAdmin, self).queryset(request)

        if not request.user.is_superuser:
            qs = qs.filter(user=request.user)
        return qs


    def change_view(self, request, temp):
        # View for a change request
        return views.admin_change_view(request, self, temp)
        

    
    def get_urls(self):
        # Set up the URLS dynamically
        urls = super(GuestAdmin, self).get_urls()
        my_urls =patterns('',
                           ('^(?P<temp>d+)/$', self.change_view),
                            ('^add/$', self.add_view),
                        )
        
        return my_urls + urls 


      

'''class GuestAdmin(admin.ModelAdmin):
	list_display = ('image','name', 'phone', 'email',)
	search_fields = ['name', 'address']
	exclude = ('travel_time', 'updated_time',)
	list_filter=('name',)'''


admin.site.register(Guest,GuestAdmin)  


class EnquiryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Enquiry,EnquiryAdmin)     
