from django.db import models

# Create your models here.
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
class Team(models.Model):
    hoTen=models.CharField(max_length=100)
    gioiThieu=models.TextField()
    anhDaiDien=models.ImageField()
    twitter=models.TextField()
    instagram=models.TextField()
    facebook=models.TextField()
class About(models.Model):
    gioiThieu=models.TextField()
    address=models.TextField()
    phone=models.CharField(max_length=10)
    email=models.EmailField()
    facebook=models.TextField()
    twitter=models.TextField()
    instagram=models.TextField()
    linkedin=models.TextField()