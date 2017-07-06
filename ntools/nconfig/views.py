from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Configfile, Filename_to_hostname
from .form import Uploadfileform, update_request_form
from django.conf import settings
import os
import re
base_dir = settings.BASE_DIR



def dashboard(request):
    all_entries = Configfile.objects.all()
    return render(request,'nconfig/dashboard.html',{'all_entries': all_entries})

def detail(request,filename):
    entry = get_object_or_404(Configfile, filename_dst_text=filename)
    file = open(os.path.join(base_dir, "uploads/configfiles",filename))
    content = file.read()
    return render(request, 'nconfig/filedetail.html', {'entry':entry, 'content':content})

def text(request, filename):
    return  HttpResponse('/uploads/'+ filename)

def configdb(request):
    all_entries = Configfile.objects.all()
    if request.method == "POST":
        form = Uploadfileform(request.POST, request.FILES)
        if form.is_valid():
            files = request.FILES.getlist('file')
            for file in files:
                if not str(file.name).startswith('.'):
                    instance = Configfile(filename_src_text=file.name,file_file=file)
                    instance.save()
            all_entries = Configfile.objects.all()
            return render(request,'nconfig/configdb_uploadOK.html',{'all_entries': all_entries})
    else:
        pass
    return render(request,'nconfig/configdb.html',{'all_entries': all_entries})

def update_hostname(request):
    data = ''
    if request.method == "POST":
        data = request.POST.get('update')
        if data == 'on':
            update_hostname_db()
        else:
            pass
    all_entries = Filename_to_hostname.objects.all()
    return render(request,'nconfig/update_hostname.html',{'all_entries': all_entries, 'update_request_form':update_request_form, 'data':data})

def detail_hostname(request,filename):
    entry = get_object_or_404(Filename_to_hostname, filename=filename)
    file = open(os.path.join(base_dir, "uploads/configfiles", filename))
    content = file.read()
    return render(request, 'nconfig/filedetail_hostname.html', {'entry':entry, 'content':content})

def update_hostname_db():
    need_update = Configfile.objects.filter(is_updated_to_hostname_db=False)
    for e in need_update:
        file = open(os.path.join(base_dir, "uploads/configfiles", e.filename_dst_text))
        content = file.read()
        regex = re.compile(r'^hostname (.*)$',re.M)
        hostname = regex.search(content).group(1).strip()
        i = Filename_to_hostname(filename=e.filename_dst_text, hostname=hostname)
        i.save()
        e.is_updated_to_hostname_db = True
        e.save()
