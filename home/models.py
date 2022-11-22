from django.db import models

class Emp(models.Model):
    name=models.CharField(max_length=60)
    email=models.CharField(max_length=60)
    subject=models.CharField(max_length=50)
    message=models.CharField(max_length=400)
    def __str__(self):
        return self.name+" "+self.email
