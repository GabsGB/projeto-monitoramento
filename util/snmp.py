from pysnmp.hlapi import *
from pysnmp.entity.engine import SnmpEngine
from util.loggin import log_info, log_error

def snmp(ip, listaSnmp=''):
    community = 'public'  # Comunidade SNMP configurada na impressora

    oids = listaSnmp if listaSnmp else [
        '1.3.6.1.2.1.1.5.0',
        'iso.3.6.1.2.1.43.5.1.1.17.1',
        'iso.3.6.1.2.1.25.3.2.1.3.1',
        'iso.3.6.1.2.1.43.10.2.1.4.1.1'
    ]

    log_info(f"Iniciando consulta SNMP para IP {ip}")

    iterator = getCmd(
        SnmpEngine(),
        CommunityData(community),
        UdpTransportTarget((ip, 161), timeout=4, retries=1),
        ContextData(),
        *[ObjectType(ObjectIdentity(oid)) for oid in oids]
    )

    error_indication, error_status, error_index, var_binds = next(iterator)

    if error_indication:
        log_error(f"Erro SNMP em {ip}: {error_indication}")
        return []
    elif error_status:
        log_error(f"Erro na resposta SNMP em {ip}: {error_status.prettyPrint()}")
        return

    results = []
    for oid, val in var_binds:
        results.append({'oid': str(oid), 'resposta': str(val)})
        log_info(f"OID {oid} → Resposta: {val}")

    return results
