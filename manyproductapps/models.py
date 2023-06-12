from django.db import models

# Create your models here.
class product(models.Model):
    pid=models.IntegerField(primary_key=True)
    pname=models.CharField(max_length=10)
    pcost=models.FloatField(max_length=10)
    pmfdt=models.DateField()
    pexpdt=models.DateField()
