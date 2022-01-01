from django.db import models

# Create your models here.


class BigJob(models.Model):
    jobName = models.CharField(verbose_name="工作名称", max_length=64)
    jobSalary = models.CharField(max_length=64)
    jobLimitExperience = models.CharField(max_length=64)
    jobLimitStudy = models.CharField(max_length=64)
    jobArea = models.CharField(max_length=64)
    companyName = models.CharField(max_length=64)
    financialStatus = models.CharField(max_length=64)
    scale = models.CharField(max_length=64)
    companyLogo = models.CharField(max_length=256)
    bonus = models.CharField(max_length=64)

    def __str__(self) -> str:
        return self.jobName

    class Meta:
        db_table = "bigJob"
        verbose_name_plural = "职业大类"
        verbose_name = "职业大类"
