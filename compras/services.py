from .models import Ciatt003, Ocxxt004, Ocxxt006

def get_divisiones():
    return Ciatt003.objects.filter(co_tipfila = 'd')

def get_tipos_compra(division):
    queryset = Ocxxt004.objects.filter(to_cia='e')
    if division:
        queryset = queryset.filter(to_division=division)
    return queryset

def get_solicitantes():
    return Ocxxt006.objects.filter(so_estado='A')