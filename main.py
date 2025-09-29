from services.scan_service import scan_filiais, scan_bd, attCont_mensais
from classes.ImpressoraController import ImpressoraController
from services.bd_service import read_impressoras
from util.snmp import snmp

if __name__ == "__main__":
    #impressoras = scan_bd()
    scan_filiais()
    #attCont_mensais(impressoras)
    