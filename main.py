from services.scan_service import scan_filiais, scan_bd, attCont_mensais, scan_manual
from classes.ImpressoraController import ImpressoraController
from services.bd_service import read_impressoras
from util.snmp import snmp

if __name__ == "__main__":
    scan_filiais()
    impressoras = scan_bd()
    attCont_mensais(impressoras)
    