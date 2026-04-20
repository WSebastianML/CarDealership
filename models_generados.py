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
    ct_usuario = models.CharField(blank=True, null=True, max_length=60)
    ct_fhalta = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'cgrta001'
        unique_together = (('ct_compania', 'ct_cuenta'),)


class Ocxxt004(models.Model):
    to_cia = models.CharField(primary_key=True, blank=True, null=False, max_length=60)
    to_division = models.CharField(blank=True, null=True, max_length=60)
    to_tipo = models.CharField(blank=True, null=True, max_length=60)
    to_descrip = models.CharField(blank=True, null=True, max_length=60)

    class Meta:
        managed = False
        db_table = 'ocxxt004'


class Ciatt003(models.Model):
    co_tipfila = models.CharField(primary_key= True, blank=True, null=False, max_length=60)
    co_cia = models.CharField(blank=True, null=True, max_length=60)
    co_div = models.CharField(blank=True, null=True, max_length=60)
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