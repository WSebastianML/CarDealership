from . import models

def get_divisiones():
    return models.Ciatt003.objects.filter(co_tipfila = 'd')

def get_tipos_compra(division):
    queryset = models.Ocxxt004.objects.filter(to_cia='e')
    if division:
        queryset = queryset.filter(to_division=division)
    return queryset

def get_solicitantes():
    return models.Ocxxt006.objects.filter(so_estado='A')

def get_tipos_credito():
    return models.Coat007.objects.exclude(cre_codigo='00')

def get_cuentas_por_ruc(ruc):
    # mc_codpro__pv_cedruc navega de Ocxxt013 a Ciatt011 y busca por pv_cedruc
    # mc_cuenta__ct_compania navega de Ocxxt013 a Cgrta001 y filtra por compañía
    return models.Ocxxt013.objects.filter(
        mc_codpro__pv_cedruc=ruc,
        mc_cuenta__ct_compania='e'
    ).select_related('mc_codpro', 'mc_cuenta')