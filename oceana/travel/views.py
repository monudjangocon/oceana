from django.shortcuts import render_to_response

from django.template import RequestContext
from models import Guest,Enquiry
from django.http import HttpResponse,HttpResponseRedirect 
from forms import GuestForm,EnquiryForm

def main(request):
  return render_to_response('base.html',{})







def guest(request):
  if request.method=="POST":
    form=GuestForm(request.POST)
    if form.is_valid():
      form.save()
      return HttpResponse('guest added')
  else:
    form=GuestForm()
  return render_to_response('guest2.html',{'form':form},context_instance=RequestContext(request))






def enquiry(request):
  if request.method=="POST":
    form=EnquiryForm(request.POST)
    if form.is_valid():
      form.save()
      return HttpResponse('eaquiry added')
  else:
    form=EnquiryForm()
  return render_to_response('enquiry.html',{'form':form},context_instance=RequestContext(request))    


def AllGuest(request):

  guests=Guest.objects.all()
  return render_to_response('allguest.html',{'guests':guests},  context_instance=RequestContext(request))

def AllEnquiry(request):
  
  enquiry=Enquiry.objects.all()
  return render_to_response('allenquiry.html',{'enquiry':enquiry},  context_instance=RequestContext(request))




      
  

  
