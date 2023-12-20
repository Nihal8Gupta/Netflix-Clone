from django.db import models

# Create your models here.
class demo(models.Model):
    dname = models.CharField(max_length=100)
    dno = models.IntegerField()
    def __str__(self) -> str:
        return self.dname