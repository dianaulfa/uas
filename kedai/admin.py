from django.contrib import admin
from .models import Member, Makanan

class MemberAnggota():
    list_display = ("Nama", "Alamat", "Tanggal",)

admin.site.register(Member)
admin.site.register(Makanan)
