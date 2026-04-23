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

# Tipos de ordenes de compra según el tipo de división
class Ocxxt004(models.Model):
    to_cia = models.CharField(blank=True, null=True, max_length=60)
    to_division = models.CharField(blank=True, null=True, max_length=60)
    to_tipo = models.CharField(blank=True, null=True, max_length=60)
    to_descrip = models.CharField(primary_key=True, blank=True, null=False, max_length=60)

    class Meta:
        managed = False
        db_table = 'ocxxt004'

# Solicitantes de ordenes de compra
class Ocxxt006(models.Model):
    so_cia = models.CharField(blank=True, null=True, max_length=60)
    so_codigo = models.CharField(primary_key=True, blank=True, null=False, max_length=60)
    so_nombres = models.CharField(blank=True, null=True, max_length=60)
    so_fecalta = models.DateTimeField()
    so_estado = models.CharField(blank=True, null=True, max_length=60)

    class Meta:
        managed = False
        db_table = 'ocxxt006'
        unique_together = (('so_cia', 'so_codigo'),)

# Tipos de credito
class Coat007(models.Model):
    cre_codigo = models.CharField(primary_key=True, blank=True, null=False, max_length=60)
    cre_descrip = models.CharField(blank=True, null=True, max_length=60)
    cre_reg = models.CharField(blank=True, null=True, max_length=60)
    cre_estado = models.CharField(blank=True, null=True, max_length=60)

    class Meta:
        managed = False
        db_table = 'coat007'


class Ciatt011(models.Model):
    pv_cia = models.CharField(blank=True, null=True, max_length=60)
    pv_agencia = models.CharField(blank=True, null=True, max_length=60)
    pv_codigo = models.AutoField(primary_key=True, blank=True, null=False)
    pv_nombre = models.CharField(blank=True, null=True, max_length=60)
    pv_direcc = models.CharField(blank=True, null=True, max_length=60)
    pv_siglas = models.CharField(blank=True, null=True, max_length=60)
    pv_pais = models.CharField(blank=True, null=True, max_length=60)
    pv_prvcia = models.CharField(blank=True, null=True, max_length=60)
    pv_actpro = models.CharField(blank=True, null=True, max_length=60)
    pv_region = models.CharField(blank=True, null=True, max_length=60)
    pv_telef1 = models.CharField(blank=True, null=True, max_length=60)
    pv_telef2 = models.CharField(blank=True, null=True, max_length=60)
    pv_fax = models.CharField(blank=True, null=True, max_length=60)
    pv_telex = models.CharField(blank=True, null=True, max_length=60)
    pv_contacto = models.CharField(blank=True, null=True, max_length=60)
    pv_refere1 = models.CharField(blank=True, null=True, max_length=60)
    pv_refere2 = models.CharField(blank=True, null=True, max_length=60)
    pv_tipo = models.CharField(blank=True, null=True, max_length=60)
    pv_moneda = models.CharField(blank=True, null=True, max_length=60)
    pv_person = models.CharField(blank=True, null=True, max_length=60)
    pv_cedruc = models.CharField(blank=True, null=True, max_length=60)
    pv_estado = models.CharField(blank=True, null=True, max_length=60)
    pv_fechoa = models.DateTimeField()
    pv_usera = models.CharField(blank=True, null=True, max_length=60)
    pv_fechoe = models.DateTimeField(blank=True, null=True)
    pv_usere = models.CharField(blank=True, null=True, max_length=60)
    pv_cta_aux = models.CharField(blank=True, null=True, max_length=60)
    pv_cta_dol = models.CharField(blank=True, null=True, max_length=60)
    pv_cup_suc = models.DecimalField(max_digits=12, decimal_places=2)
    pv_cup_dol = models.DecimalField(max_digits=12, decimal_places=2)
    pv_cupsuc_u = models.DecimalField(max_digits=12, decimal_places=2)
    pv_cupdol_u = models.DecimalField(max_digits=12, decimal_places=2)
    pv_contesp = models.CharField(blank=True, null=True, max_length=60)
    pv_codcob = models.IntegerField(blank=True, null=True)
    pv_numcalle = models.CharField(blank=True, null=True, max_length=60)
    pv_autimp = models.CharField(blank=True, null=True, max_length=60)
    pv_serie = models.CharField(blank=True, null=True, max_length=60)
    pv_aut_sri = models.CharField(blank=True, null=True, max_length=60)
    pv_codbanco = models.CharField(blank=True, null=True, max_length=60)
    pv_tipcta = models.CharField(blank=True, null=True, max_length=60)
    pv_cta = models.CharField(blank=True, null=True, max_length=60)
    pv_pago_aut = models.CharField(blank=True, null=True, max_length=60)
    pv_fecnac = models.DateField(blank=True, null=True)
    pv_mail = models.CharField(blank=True, null=True, max_length=60)

    class Meta:
        managed = False
        db_table = 'ciatt011'
        unique_together = (('pv_cia', 'pv_agencia', 'pv_codigo'),)


class Cgrta001(models.Model):
    ct_compania = models.CharField(blank=True, null=True, max_length=60)
    ct_cuenta = models.CharField(primary_key=True, blank=True, null=False, max_length=60)
    ct_descripcion = models.CharField(blank=True, null=True, max_length=60)
    ct_estado = models.CharField(blank=True, null=True, max_length=60)
    ct_nivel = models.CharField(blank=True, null=True, max_length=60)
    ct_signo = models.CharField(blank=True, null=True, max_length=60)
    ct_tipo = models.CharField(blank=True, null=True, max_length=60)
    ct_dolar = models.CharField(blank=True, null=True, max_length=60)
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


# Cuentas por proveedor
class Ocxxt013(models.Model):
    mc_codgrp = models.SmallIntegerField(primary_key=True, blank=True, null=False, max_length=60)
    mc_secgrp = models.IntegerField(blank=True, null=True)
    mc_cuenta = models.ForeignKey('Cgrta001', on_delete = models.DO_NOTHING, db_column='mc_cuenta', blank=True, null=True, db_constraint=False)
    mc_codpro = models.ForeignKey('Ciatt011', on_delete = models.DO_NOTHING, db_column='mc_codpro', blank=True, null=True, db_constraint=False)

    class Meta:
        managed = False
        db_table = 'ocxxt013'



