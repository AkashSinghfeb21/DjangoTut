from django.db import models

class contact(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=300)
    phone = models.CharField(max_length=300)
    desc = models.CharField(max_length=3000)

    def __str__(self):
        return self.name