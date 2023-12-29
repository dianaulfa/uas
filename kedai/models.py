from django.db import models

class Member(models.Model):
    Nama = models.CharField(max_length=200)
    Alamat = models.TextField()
    Tanggal_Lahir = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.Nama}"

class Makanan(models.Model):
    Nama = models.CharField(max_length=200)
    Harga = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.Nama}"