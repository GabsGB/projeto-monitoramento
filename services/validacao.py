from util.scan import scan
from classes.ImpressoraController import ImpressoraController
from classes.Impressora import Impressora
from .bd_service import read_impressoras
from util.loggin import log_info, log_error
import ipaddress

def validar_ipv4(ip):
    try:
        ip = ipaddress.IPv4Address(ip)
        if ip.is_multicast or ip.is_loopback or ip.is_unspecified or not ip.is_private:
            log_error(f"IP {ip} não permitido!")
            return False
        elif ip.is_private:
            log_info(f"IP {ip} permitido!")
            return True
    except ipaddress.AddressValueError:
        log_error(f"IP {ip} inválido")
        return False
    

def validar_impressora(ip, impressoras_bd=None):
    if impressoras_bd is None:
        impressoras_bd = read_impressoras()
    bd_por_ip = {imp.ip: imp for imp in impressoras_bd}
    
    if scan(ip):
        log_info(f"IP ativo: {ip}")
        imp = Impressora(ip=ip, conexao="IP", status="Ativo")
        controler = ImpressoraController(imp)
        controler.atualizar_dados_snmp()
        if imp.num_serie is not None:
            log_info(f"N° de série detectado: {imp.num_serie}")
            if imp.filial_id == "1" or "ZD230" in imp.modelo:
                log_info("Impressora bloqueada: Matriz ou Zebra")
                return None
            log_info("Impressora inserida na lista de atualização.")
            return imp
        else:
            log_error("Impressora sem número de série após SNMP.")
            return None
    else:
        log_info(f"IP offline: {ip}")
        if ip in bd_por_ip:
            log_info("IP cadastrado no banco... alterando status da impressora.")
            imp_existente = bd_por_ip[ip]
            controler = ImpressoraController(imp_existente)
            controler.set_status("Offline")
            log_info("Impressora inserida na lista de atualização.")
            return imp_existente
        else:
            log_error("IP não encontrado no banco e está offline.")
            return None

