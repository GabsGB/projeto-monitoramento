from classes.ImpressoraController import ImpressoraController
from classes.Impressora import Impressora
from .bd_service import read_impressoras, limpar_tbl, insert_tbl_relImpressora, insert_tbl_contMensais, read_tbl_filiais
from .sync_service import sincronizar_impressoras
from util.scan import scan
from util.snmp import snmp
from typing import Tuple
from .validacao import validar_impressora, validar_ipv4
import copy
#import pandas as pd
#import numpy as np  

def scan_bd() -> Tuple[list[Impressora], list[Impressora]]:
    impressoras_bd: list[Impressora] = read_impressoras()
    impressoras_leitura = copy.deepcopy(impressoras_bd)

    impressoras_atualizadas: list = []
    
    for imp in impressoras_leitura:
        if imp.ip is not None:
            #print(f"\nIP: {imp.ip}")
            #print(f"N° de série: {imp.num_serie}\n")
            controler = ImpressoraController(imp)
            controler.set_filialId()
            if "ZD230" in imp.modelo or imp.filial_id == "1":
                continue
            controler.atualizar_dados_snmp()
            #print(f"IP: {imp.ip}")
            impressoras_atualizadas.append(imp)
        else: continue
    
    sincronizar_impressoras(impressoras_atualizadas, impressoras_bd)
    return impressoras_atualizadas


def scan_filiais():
    print("Iniciando scan total das filiais...")
    filiais_bd = read_tbl_filiais()
    impressoras_bd = read_impressoras()
    
    faixa_filial = range(50, 56)
    impressoras_filiais = []

    for filial in filiais_bd:
        print(f"Rodando na filial {filial.id}")
        for impressora in faixa_filial:
            ip = f"10.0.{str(filial.id)}.{str(impressora)}"
            print(f"\n==========================================\nTestando IP {ip}")
            imp = validar_impressora(ip, impressoras_bd)
            if imp is not None:
                impressoras_filiais.append(imp)
    print(f"\nFinalizado scan das filiais.\n")

    sincronizar_impressoras(impressoras_novas=impressoras_filiais, impressoras_bd=impressoras_bd)
    return  impressoras_filiais

''' # Adicionar posteriormente
def scan_manual():
    impressora_atulizar = []
    impressoras_bd = read_impressoras()

    ip = input("digite o IP (ex: 255.255.255.255, 10.0.0.1...): ").strip()
    if ip is not None:
        if not "-" in ip: # IP único
            if validar_ipv4(ip):
                imp = validar_impressora(ip)
                if imp:
                    impressora_atulizar.append(imp)
        else:

            
            pass


    sincronizar_impressoras(impressoras_novas=impressora_atulizar, impressoras_bd=impressoras_bd)
'''

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

    atualizadas_por_serie = [imp.num_serie for imp in impressoras_atualizadas]
    for impressora in impressoras_atualizadas:
        if impressora.status == "Ativo":
            insert_tbl_contMensais(impressora)
    print(len(atualizadas_por_serie))
    print(atualizadas_por_serie)
    
