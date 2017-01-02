from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Configfile
from .form import Uploadfileform
# Create your views here.

def dashboard(request):
    all_entries = Configfile.objects.all()
    if request.method == "POST":
        form = Uploadfileform(request.POST, request.FILES)
        index = 0
        if form.is_valid():
            files = request.FILES.getlist('file')
            for file in files:
                instance = Configfile(filename_text=file.name,file_file=file)
                instance.save()
            return HttpResponse('Upload OK!')
    else:
        form = Uploadfileform()
        index = 0
    return render(request,'nconfig/dashboard.html',{'all_entries': all_entries,'form': form,'index':index})

def detail(request,filename):
    entry = get_object_or_404(Configfile, filename_text=filename)
    return render(request, 'nconfig/dashboard.html', {'entry':entry})