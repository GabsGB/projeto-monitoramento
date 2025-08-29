from classes.ImpressoraController import ImpressoraController
from classes.Impressora import Impressora
from .bd_service import read_impressoras, limpar_tbl, insert_tbl_relImpressora, insert_tbl_contMensais, read_filiais
from .sync_service import sincronizar_impressoras
from util.scan import scan
from util.snmp import snmp
from typing import Tuple
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
            if scan(ip):
                print("Ip ativo!")
                imp = Impressora(ip=ip,conexao="IP",status="Ativo")
                controler = ImpressoraController(imp)
                controler.atualizar_dados_snmp()
                if imp.num_serie != None:
                    print(f"N° de série {imp.num_serie}")
                    if imp.filial_id == "1" or "ZD230" in imp.modelo:
                        print("Impressora bloqueada! Matriz ou Zebra")
                        continue
                    print(f"Impressora inserida na lista de atualzação.")
                    impressoras_filiais.append(imp)
            else:
                print("Ip offline!")
                if ip in bd_por_ip:
                    print("IP cadastrado no banco... alterando status da impressora...")
                    imp_existente = bd_por_ip[ip]
                    controler = ImpressoraController(imp_existente)
                    controler.set_status("Offline")
                    print(f"Impressora inserida na lista de atualzação.")
                    impressoras_filiais.append(imp_existente)
    sincronizar_impressoras(impressoras_novas=impressoras_filiais, impressoras_bd=impressoras_bd)
    return  impressoras_filiais


def scan_manual():
    ips = input("Digite a faixa de Ip que deseja buscar: ")
    print(ips)
    pass


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

