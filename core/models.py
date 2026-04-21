from django.db import models

class Company(models.Model):
    key      = models.CharField(max_length=50, unique=True)
    name     = models.CharField(max_length=100)
    db_alias = models.CharField(max_length=50)

    db_dsn    = models.CharField(max_length=100)   # 'DNSdesarrollo'
    db_name   = models.CharField(max_length=100)   # 'ecuawagen'
    db_server = models.CharField(max_length=100)   # 'ol_desarrollo'
    db_host   = models.CharField(max_length=200)   # '192.168.1.9'
    logo      = models.CharField(max_length=200, blank=True)
    activa    = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'core'