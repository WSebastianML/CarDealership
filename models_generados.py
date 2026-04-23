# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Cgrta001(models.Model):
    ct_compania = models.CharField(blank=True, null=True)
    ct_cuenta = models.CharField(blank=True, null=True)
    ct_descripcion = models.CharField(blank=True, null=True)
    ct_estado = models.CharField(blank=True, null=True)
    ct_nivel = models.CharField(blank=True, null=True)
    ct_signo = models.CharField(blank=True, null=True)
    ct_tipo = models.CharField(blank=True, null=True)
    ct_dolar = models.CharField(blank=True, null=True)
    ct_db_ano_ant = models.DecimalField(max_digits=14, decimal_places=2)
    ct_cr_ano_ant = models.DecimalField(max_digits=14, decimal_places=2)
    ct_db_mes01 = models.DecimalField(max_digits=14, decimal_places=2)
    ct_db_mes02 = models.DecimalField(max_digits=14, decimal_places=2)
    ct_db_mes03 = models.DecimalField(max_digits=14, decimal_places=2)
    ct_db_mes04 = models.DecimalField(max_digits=14, decimal_places=2)
    ct_db_mes05 = models.DecimalField(max_digits=14, decimal_places=2)
    ct_db_mes06 = models.DecimalField(max_digits=14, decimal_places=2)
    ct_db_mes07 = models.DecimalField(max_digits=14, decimal_places=2)
    ct_db_mes08 = models.DecimalField(max_digits=14, decimal_places=2)
    ct_db_mes09 = models.DecimalField(max_digits=14, decimal_places=2)
    ct_db_mes10 = models.DecimalField(max_digits=14, decimal_places=2)
    ct_db_mes11 = models.DecimalField(max_digits=14, decimal_places=2)
    ct_db_mes12 = models.DecimalField(max_digits=14, decimal_places=2)
    ct_cr_mes01 = models.DecimalField(max_digits=14, decimal_places=2)
    ct_cr_mes02 = models.DecimalField(max_digits=14, decimal_places=2)
    ct_cr_mes03 = models.DecimalField(max_digits=14, decimal_places=2)
    ct_cr_mes04 = models.DecimalField(max_digits=14, decimal_places=2)
    ct_cr_mes05 = models.DecimalField(max_digits=14, decimal_places=2)
    ct_cr_mes06 = models.DecimalField(max_digits=14, decimal_places=2)
    ct_cr_mes07 = models.DecimalField(max_digits=14, decimal_places=2)
    ct_cr_mes08 = models.DecimalField(max_digits=14, decimal_places=2)
    ct_cr_mes09 = models.DecimalField(max_digits=14, decimal_places=2)
    ct_cr_mes10 = models.DecimalField(max_digits=14, decimal_places=2)
    ct_cr_mes11 = models.DecimalField(max_digits=14, decimal_places=2)
    ct_cr_mes12 = models.DecimalField(max_digits=14, decimal_places=2)
    ct_db_mes01s = models.DecimalField(max_digits=14, decimal_places=2)
    ct_db_mes02s = models.DecimalField(max_digits=14, decimal_places=2)
    ct_db_mes03s = models.DecimalField(max_digits=14, decimal_places=2)
    ct_db_mes04s = models.DecimalField(max_digits=14, decimal_places=2)
    ct_cr_mes01s = models.DecimalField(max_digits=14, decimal_places=2)
    ct_cr_mes02s = models.DecimalField(max_digits=14, decimal_places=2)
    ct_cr_mes03s = models.DecimalField(max_digits=14, decimal_places=2)
    ct_cr_mes04s = models.DecimalField(max_digits=14, decimal_places=2)
    ct_usuario = models.CharField(blank=True, null=True)
    ct_fhalta = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'cgrta001'
        unique_together = (('ct_compania', 'ct_cuenta'),)
