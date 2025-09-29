from pysnmp.hlapi import *
from pysnmp.entity.engine import SnmpEngine

#mib = getMib()


# validação:
# entrada      ( )
# processo     (X)
# finalização  ( )

def snmp(ip, listaSnmp = ''):

    community = 'public'  # Comunidade SNMP configurada na impressora
    if listaSnmp != '':
        oids = listaSnmp
    else:
        oids = ['1.3.6.1.2.1.1.5.0', 'iso.3.6.1.2.1.43.5.1.1.17.1', 'iso.3.6.1.2.1.25.3.2.1.3.1', 'iso.3.6.1.2.1.43.10.2.1.4.1.1']

    #print(f"\n Ip da impressora {ip}")
    iterator = getCmd(
    SnmpEngine(),
    CommunityData(community),
    UdpTransportTarget((ip, 161), timeout=4, retries=1),
    ContextData(),
    *[ObjectType(ObjectIdentity(oid)) for oid in oids]
    )

    error_indication, error_status, error_index, var_binds = next(iterator)

    if error_indication:
        print(f"Erro SNMP: {error_indication}")
        return []
    elif error_status:
        print(f"Erro na resposta: {error_status.prettyPrint()}")
        return
    results = []
    for oid, val in var_binds:
        results.append({'oid': str(oid), 'resposta': str(val)})

    return results