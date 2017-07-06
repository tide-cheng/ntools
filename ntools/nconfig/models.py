from django.db import models

# Create your models here.

class Configfile(models.Model):
    filename_src_text=models.CharField('源文件名', max_length=256)
    fileadd_date = models.DateTimeField('文件加入数据库时间',auto_now_add=True)
    file_file=models.FileField('文件位置',upload_to='configfiles/')
    # filename_dst_text = str(file_file.name).rsplit('/',maxsplit=1)[0]
    filename_dst_text = models.CharField('目标文件名', max_length=256)
    is_updated_to_hostname_db = models.BooleanField('是否加入设备名数据库', default=False)

    def __str__(self):
        return self.filename_dst_text

    def save(self, *args, **kwargs):
        if not self.filename_dst_text:
            super().save(*args, **kwargs)
            self.filename_dst_text = self.get_filename_dst_text()
        super().save(*args, **kwargs)  # Call the "real" save() method.

    def get_filename_dst_text(self):
        # file_file.name = configfiles/A-HHA2D-BL1-DS01
        return str(self.file_file.name).split('/')[1]

class Filename_to_hostname(models.Model):
    filename = models.CharField('文件名', max_length=256)
    hostname = models.CharField('设备名', max_length=256)