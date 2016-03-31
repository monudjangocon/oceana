from django.shortcuts import render_to_response

from django.template import RequestContext
from models import Guest

def home(request):
	return render_to_response('base.html',{})




def admin_change_view(request, model_admin, temp=None):
    
    opts = model_admin.model._meta
    admin_site = model_admin.admin_site
    has_perm = request.user.has_perm(opts.app_label + '.' + opts.get_change_permission())
    
    obj = None
    if temp:
        obj = Guest.objects.get(id=temp)
    
    guest_2 = Guest.objects.all()
    
    context = { 'admin_site': admin_site.name,
               'title': 'Add/Edit Story',
               'opts':opts,
               'editions': ed,          #New
               'guest_2':guest_2,   #New
               'obj':obj,               #New
               'root_path': '/%s' % admin_site.root_path,
               'app_label' : opts.app_label,
               'has_change_permission':has_perm}
    template = 'admin/change_form.html' 
    return render_to_response(template, context,
                              context_instance=RequestContext(request))  