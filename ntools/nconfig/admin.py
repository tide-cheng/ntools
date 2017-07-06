from django.contrib import admin

# Register your models here.
from .models import Configfile
from .models import Filename_to_hostname

class Configfile_admin(admin.ModelAdmin):
    list_display = ['filename_src_text','file_file','filename_dst_text','is_updated_to_hostname_db','fileadd_date']
    show_hidden = ['fileadd_date']
    readonly_fields = list_display
    list_display_links = None

    # def __init__(self,*args,**kwargs):
    #     super(Configfile_admin, self).__init__(*args, **kwargs)
    #     self.list_display_links = (None, )

class Host_admin(admin.ModelAdmin):
    list_display = ['filename', 'hostname']
    readonly_fields = list_display

admin.site.register(Configfile, Configfile_admin)
admin.site.register(Filename_to_hostname, Host_admin)