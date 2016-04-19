from django import forms

from models import Guest,Enquiry

class GuestForm(forms.ModelForm):
	class Meta:
		model=Guest
		fields=['name','phone','email']

class EnquiryForm(forms.ModelForm):
	class Meta:
		model=Enquiry
		fields=['guest','address']
