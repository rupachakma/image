from django.db import models

# Create your models here.
class Office(models.Model):
    name=models.CharField(max_length=20)
    department=models.CharField(max_length=20)
    profileImg=models.ImageField(upload_to="image",blank=True,null=True)

    def __str__(self):
        return self.name
        