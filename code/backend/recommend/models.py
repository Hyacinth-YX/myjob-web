from django.db import models

# Create your models here.


class jobRecord(models.Model):
    jobId = models.IntegerField()
    uid = models.IntegerField()
    c_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "jobRecord"
        verbose_name = '访问记录'
        verbose_name_plural = '访问记录'
