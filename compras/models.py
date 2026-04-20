from django.db import models

#Tipos de division
class Ciatt003(models.Model):
    co_tipfila = models.CharField(blank=True, null=True, max_length=60)
    co_cia = models.CharField(blank=True, null=True, max_length=60)
    co_div = models.CharField(primary_key=True, blank=True, null=False, max_length=60)
    co_agencia = models.CharField(blank=True, null=True, max_length=60)
    co_ciudad = models.CharField(blank=True, null=True, max_length=60)
    co_nomext = models.CharField(max_length=60)
    co_nomcorto = models.CharField(blank=True, null=True, max_length=60)
    co_ruc = models.CharField(blank=True, null=True, max_length=60)
    co_patronal = models.CharField(blank=True, null=True, max_length=60)
    co_replegal = models.CharField(blank=True, null=True, max_length=60)
    co_cedrep = models.CharField(blank=True, null=True, max_length=60)
    co_direcc = models.CharField(blank=True, null=True, max_length=60)
    co_telef1 = models.CharField(blank=True, null=True, max_length=60)
    co_telef2 = models.CharField(blank=True, null=True, max_length=60)
    co_fax1 = models.CharField(blank=True, null=True, max_length=60)
    co_fax2 = models.CharField(blank=True, null=True, max_length=60)
    co_pobox = models.CharField(blank=True, null=True, max_length=60)
    co_contribuyente = models.CharField(blank=True, null=True, max_length=60)
    co_codcli = models.IntegerField(blank=True, null=True)
    co_resolucion = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ciatt003'


class Ocxxt004(models.Model):
    to_cia = models.CharField(blank=True, null=True, max_length=60)
    to_division = models.CharField(blank=True, null=True, max_length=60)
    to_tipo = models.CharField(blank=True, null=True, max_length=60)
    to_descrip = models.CharField(primary_key=True, blank=True, null=False, max_length=60)

    class Meta:
        managed = False
        db_table = 'ocxxt004'
