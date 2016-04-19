from django.contrib import admin

from models import Guest,Enquiry


      

class GuestAdmin(admin.ModelAdmin):
	list_display = ('name', 'phone', 'email',)
	search_fields = ['name', 'address']
	exclude = ('travel_time', 'updated_time',)
	list_filter=('name',)


admin.site.register(Guest,GuestAdmin)  


class EnquiryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Enquiry,EnquiryAdmin)     
