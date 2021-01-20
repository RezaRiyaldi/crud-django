from django.db import models

# Create your models here.
class Data_mhs(models.Model):
    id_mhs = models.AutoField(primary_key = True)
    nim = models.CharField(max_length = 15, blank = True, null = True)
    nama = models.CharField(max_length = 100, blank = True, null = True)
    tgl_lahir = models.DateField(blank = True, null = True)
    alamat = models.TextField()

    class Meta:
        db_table = 'tb_mahasiswa'