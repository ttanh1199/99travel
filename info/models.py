from django.db import models

# Create your models here.
class Slide(models.Model):
    tieuDe=models.CharField(max_length=100)
    noiDung=models.TextField()
    anhNen=models.ImageField()
    def __str__(self):
        return self.tieuDe
class Review(models.Model):
    hoTen=models.CharField(max_length=100)
    noiDung=models.TextField()
    anhNen=models.ImageField()
    def __str__(self):
        return self.hoTen
class Discount(models.Model):
    tenDiaDiem=models.CharField(max_length=100)
    giaGoc=models.DecimalField(max_digits=20,decimal_places=2)
    giaGiam=models.DecimalField(max_digits=20,decimal_places=2)
    anhDiaDiem=models.ImageField()
    def __str__(self):
        return self.tenDiaDiem

