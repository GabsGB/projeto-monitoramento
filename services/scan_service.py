from classes.ImpressoraController import ImpressoraController
from classes.Impressora import Impressora
from .bd_service import read_impressoras, limpar_tbl, insert_tbl_relImpressora, insert_tbl_contMensais, read_filiais
from .sync_service import sincronizar_impressoras
from util.scan import scan
from util.snmp import snmp
from typing import Tuple
from .validacao import validar_impressora, validar_ip
#import pandas as pd
#import numpy as np  

'''
scan_bd() -> Baixa as impressoras do BD
'''

def scan_bd() -> Tuple[list[Impressora], list[Impressora]]:
    impressoras_leitura: list[Impressora] = read_impressoras()
    impressoras_atualizadas: list = []
    
    
    for imp in impressoras_leitura:
        if imp.ip is not None:
            controler = ImpressoraController(imp)
            controler.set_filialId()
            if imp.filial_id == "1" or "ZD230" in imp.modelo:
                continue
            controler.atualizar_dados_snmp()
            impressoras_atualizadas.append(imp)
        else: continue

    sincronizar_impressoras(impressoras_novas=impressoras_atualizadas, impressoras_bd=impressoras_leitura)
    return impressoras_atualizadas


def scan_filiais():
    print("Iniciando scan total das filiais...")
    filiais_bd = read_filiais()
    impressoras_bd = read_impressoras()
    bd_por_ip = {imp.ip: imp for imp in impressoras_bd}
    
    faixaImpressoras = range(50, 56)
    
    impressoras_filiais = []

    for filial in filiais_bd:
        print(f"Rodando na filial {filial.id}")
        for impressora in faixaImpressoras:
            ip = f"10.0.{str(filial.id)}.{str(impressora)}"
            print(f"\n==========================================\nTestando IP {ip}")
            imp = validar_impressora(ip)
            if imp is not None:
                impressoras_filiais.append(imp)
                
    sincronizar_impressoras(impressoras_novas=impressoras_filiais, impressoras_bd=impressoras_bd)
    return  impressoras_filiais


def scan_manual():
    impressora_atulizar = []
    impressoras_bd = read_impressoras()

    tipo_scan = int(input("""
        1 - IP único
        2 - Faixa de IP
        : """))
    
    if tipo_scan == 1:
        ip = input("digite o IP (ex: 255.255.255.255, 10.0.0.1...): ")
        if ip is not None:
            if validar_ip(ip):
                imp = validar_impressora(ip)
                if imp:
                    impressora_atulizar.append(imp)
        
    elif tipo_scan == 2:
        
        pass

    sincronizar_impressoras(impressoras_novas=impressora_atulizar, impressoras_bd=impressoras_bd)


def attImpressora_filial(impressoras_atualizadas):
    #impressoras_bd, impressoras_atualizadas = scan_bd()

    print(len(impressoras_atualizadas))
    limpar_tbl("impressora_filial")
    for impressora in impressoras_atualizadas:
        if impressora.status == "Ativo":
            controler = ImpressoraController(impressora)
            insert_tbl_relImpressora(controler)


def attCont_mensais(impressoras_atualizadas):
    #impressoras_bd, impressoras_atualizadas = scan_bd()
    #sincronizar_impressoras(impressoras_novas=impressoras_atualizadas, impressoras_bd=impressoras_bd)

    for impressora in impressoras_atualizadas:
        if impressora.status == "Ativo":
            insert_tbl_contMensais(impressora)

