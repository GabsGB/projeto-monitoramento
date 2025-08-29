from services.scan_service import scan_filiais, scan_impressorasBd, attCont_mensais
from services.bd_service import read_impressoras, read_filiais
from util.snmp import snmp

if __name__ == "__main__":
    scan_impressorasBd()
    attCont_mensais()