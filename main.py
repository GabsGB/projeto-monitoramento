from services.scan_service import scan_filiais, scan_bd, attCont_mensais, scan_manual, attImpressora_filial
from classes.ImpressoraController import ImpressoraController
from services.bd_service import read_impressoras
from util.snmp import snmp

if __name__ == "__main__":
    
    resp = input("Realizar somente o scan, atualizar contadores?  \n1 - Scan \n2-Scan + Contadores")

    scan_filiais()
    impressoras = scan_bd()
    attImpressora_filial(impressoras)
    if resp == '2':
        attCont_mensais(impressoras)
    