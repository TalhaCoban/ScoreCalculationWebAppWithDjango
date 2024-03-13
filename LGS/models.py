from django.db import models

# Create your models here.
class LGS(models.Model):
    ogrenci = models.ForeignKey("auth.User",on_delete = models.CASCADE, verbose_name = "ogrenci")
    lgspuan = models.FloatField(verbose_name="LGSpuan",max_length=7,default=500)
    created_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.ogrenci

    class Meta:
        ordering = ["-created_date"]