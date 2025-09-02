from services.scan_service import scan
from classes.ImpressoraController import ImpressoraController
from classes.Impressora import Impressora
from .bd_service import read_impressoras
import ipaddress

def validar_ipv4(ip):
    try:
        ip = ipaddress.IPv4Address(ip)
        if ip.is_private:
            print(f"Ip {ip} permitido!")
            return True
        else:
            print(f"Ip {ip} não permitido!")
            return False
    except ipaddress.AddressValueError:
        print(f"IP {ip} inválido")
        return False
    


def validar_ip(ip):

    if "." not in ip:
        return False
    if not len(ip.split(".")) <= 4:
        return False
    
    

def validar_impressora(ip):
    impressoras_leituras = read_impressoras()
    bd_por_ip = {imp.ip: imp for imp in impressoras_leituras}
    
    if scan(ip):
        print("Ip Ativo!")
        imp = Impressora(ip=ip, conexao="IP", status="Ativo")
        controler = ImpressoraController(imp)
        controler.atualizar_dados_snmp()
        if imp.num_serie != None:
            print(f"N° de série {imp.num_serie}")
            if imp.filial_id == "1" or "ZD230" in imp.modelo:
                print("Impressora bloqueada! Matriz ou Zebra")
                return None
            print(f"Impressora inserida na lista de atualzação.")
            return imp
        else: return None
    else:
        print("Ip offline!")
        if ip in bd_por_ip:
            print("IP cadastrado no banco... alterando status da impressora...")
            imp_existente = bd_por_ip[ip]
            controler = ImpressoraController(imp_existente)
            controler.set_status("Offline")
            print(f"Impressora inserida na lista de atualzação.")
            return imp_existente
        else: return None

