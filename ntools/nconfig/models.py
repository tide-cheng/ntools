from django.db import models

# Create your models here.

class Configfile(models.Model):
    filename_text=models.CharField('文件名',max_length=200,unique=True)
    fileadd_date = models.DateTimeField('文件加入数据库时间',auto_now_add=True)
    file_file=models.FileField('文件位置',upload_to='uploads/')

    def __str__(self):
        return self.filename_text