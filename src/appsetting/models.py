from django.db import models

# Create your models here.
class AppSetting(models.Model):
    smtp_port = models.IntegerField()
    smtp_server = models.CharField(max_length=255)
    smtp_username = models.CharField(max_length=255)
    smtp_password = models.CharField(max_length=255)



    def __str__(self):
        return f"SMTP: {self.smtp_host}:{self.smtp_port}"
