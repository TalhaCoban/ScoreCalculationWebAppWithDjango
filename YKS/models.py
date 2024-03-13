from django.db import models

# Create your models here.
class YKS(models.Model):
    ogrenci = models.ForeignKey("auth.User",on_delete = models.CASCADE, verbose_name = "ogrenci")
    tytham = models.FloatField(verbose_name="TYTham",max_length=3,default=500)
    tytyer = models.FloatField(verbose_name="TYTyer",max_length=3,default=500)
    sayisalham = models.FloatField(verbose_name="Sayisalham",max_length=3,default=500)
    sayisalyer = models.FloatField(verbose_name="Sayisalyer",max_length=3,default=500)
    eaham = models.FloatField(verbose_name="Eaham",max_length=3,default=500)
    eayer = models.FloatField(verbose_name="Eayer",max_length=3,default=500)
    sozelham = models.FloatField(verbose_name="Sozelham",max_length=3,default=500)
    sozelyer = models.FloatField(verbose_name="Sozelyer",max_length=3,default=500)
    ydtham = models.FloatField(verbose_name="Ydtham",max_length=3,default=500)
    ydtyer = models.FloatField(verbose_name="Ydtyer",max_length=3,default=500)
    tyt_sir_2018_ham = models.IntegerField(verbose_name="tyt_sir_2018_ham", default=1)
    tyt_sir_2019_ham = models.IntegerField(verbose_name="tyt_sir_2019_ham", default=1)
    tyt_sir_2018_yer = models.IntegerField(verbose_name="tyt_sir_2018_yer", default=1)
    tyt_sir_2019_yer = models.IntegerField(verbose_name="tyt_sir_2019_yer", default=1)
    ayt_sir_sayisal_2018_ham = models.IntegerField(verbose_name="ayt_sir_sayisal_2018_ham", default=1)
    ayt_sir_sayisal_2019_ham = models.IntegerField(verbose_name="ayt_sir_sayisal_2019_ham", default=1)
    ayt_sir_sayisal_2018_yer = models.IntegerField(verbose_name="ayt_sir_sayisal_2018_yer", default=1)
    ayt_sir_sayisal_2019_yer = models.IntegerField(verbose_name="ayt_sir_sayisal_2019_yer", default=1)
    ayt_sir_ea_2018_ham = models.IntegerField(verbose_name="ayt_sir_ea_2018_ham", default=1)
    ayt_sir_ea_2019_ham = models.IntegerField(verbose_name="ayt_sir_ea_2019_ham", default=1)
    ayt_sir_ea_2018_yer = models.IntegerField(verbose_name="ayt_sir_ea_2018_yer", default=1)
    ayt_sir_ea_2019_yer = models.IntegerField(verbose_name="ayt_sir_ea_2019_yer", default=1)
    ayt_sir_sozel_2018_ham = models.IntegerField(verbose_name="ayt_sir_sozel_2018_ham", default=1)
    ayt_sir_sozel_2019_ham = models.IntegerField(verbose_name="ayt_sir_sozel_2019_ham", default=1)
    ayt_sir_sozel_2018_yer = models.IntegerField(verbose_name="ayt_sir_sozel_2018_yer", default=1)
    ayt_sir_sozel_2019_yer = models.IntegerField(verbose_name="ayt_sir_sozel_2019_yer", default=1)
    ydt_sir_2018_ham = models.IntegerField(verbose_name="ydt_sir_2018_ham", default=1)
    ydt_sir_2019_ham = models.IntegerField(verbose_name="ydt_sir_2019_ham", default=1)
    ydt_sir_2018_yer = models.IntegerField(verbose_name="ydt_sir_2018_yer", default=1)
    ydt_sir_2019_yer = models.IntegerField(verbose_name="ydt_sir_2019_yer", default=1)
    created_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.ogrenci

    class Meta:
        ordering = ["-created_date"]