from django.db import models

class Cgrta004(models.Model):
    in_compania = models.CharField(primary_key=True, blank=True, null=False, max_length=60)
    in_cuenta = models.CharField(blank=True, null=True, max_length=60)
    in_descrip = models.CharField(blank=True, null=True, max_length=60)

    class Meta:
        managed = False
        db_table = 'cgrta004'
        unique_together = (('in_compania', 'in_cuenta'),)
