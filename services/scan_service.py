from classes.ImpressoraController import ImpressoraController
from classes.Impressora import Impressora
from .bd_service import read_impressoras, limpar_tbl, insert_tbl_relImpressora, insert_tbl_contMensais, read_filiais
from .sync_service import sincronizar_impressoras
from util.scan import scan
from util.snmp import snmp
from typing import Tuple
#import pandas as pd
#import numpy as np  

def coletar_statusImpressora() -> Tuple[list[Impressora], list[Impressora]]:
    impressoras_leitura: list[Impressora] = read_impressoras()
    impressoras_atualizadas = []
    
    for imp in impressoras_leitura:
        controler = ImpressoraController(imp)
        controler.atualizar_filialId()
        if imp.filial_id == "1" or "ZD230" in imp.modelo:
            continue
        controler.atualizar_dados_snmp()
        impressoras_atualizadas.append(imp)

    return impressoras_leitura, impressoras_atualizadas


def scan_filiais():
    print("Iniciando scan total das filiais...")
    filiais_bd = read_filiais()
    impressoras_bd = read_impressoras()
    
    faixaImpressoras = range(50, 56)
    bd_por_ip = {imp.ip: imp for imp in impressoras_bd}
    
    impressorasFiliais_atualizar = []

    for filial in filiais_bd:
        for impressora in faixaImpressoras:
            ip = f"10.0.{str(filial.id)}.{str(impressora)}"
            print(f"\nTestando IP {ip}\n")

            if scan(ip): # Ip online
                print("IP ONLINE \nRealizando teste SNMP")
                imp = Impressora(ip=ip,conexao="IP",status="Ativo")
                controler = ImpressoraController(imp)
                controler.atualizar_dados_snmp()

                if imp.status == "Erro no SNMP": # IP com erro não recebe SNMP
                    print("IP com erro no SNMP!")
                    
                    if ip in bd_por_ip:
                        imp_existente = bd_por_ip[ip]
                        controler = ImpressoraController(imp_existente)
                        controler.atualizar_status(imp.status)
                        print(f"IP cadastrado no BD... alterado status da impressora {imp_existente.num_serie} para Erro no SNMP")
                        impressorasFiliais_atualizar.append(imp_existente)

                    else:
                        print("IP não cadastrado no BD")
                '''
                    ANOTAÇÃO
                        Acredito que vale mais a pena ao invés desse if acima colocar um if imp.status = "erro no snmp" and ip not in ip_por_bd: continue
                        para ele ignorar esse IP, realizar testes posteriormente
                '''
                elif ip in bd_por_ip:
                    print("")
                #impressorasFiliais_atualizar

                if ip in bd_por_ip and imp.status == "Erro no SNMP": # IP cadastrado no BD                    
                    print("IP com erro no SNMP!")
                    imp_existente = bd_por_ip[ip]
                    controler = ImpressoraController(imp_existente)
                    controler.atualizar_status(imp.status)
                    print(f"IP cadastrado no BD... alterando status da impressora {imp_existente.num_serie} para Erro no SNMP")
                elif ip not in bd_por_ip and imp.status == "Erro no SNMP":
                     print("IP com erro no SNMP!")
                     print("IP não reconhecido no BD")
                    else: # Sem erro copiou o SNMP corretamente
                        print(f"Impressora:")
                        print(imp)
                        print(f"será adicionada/atualizada ao banco")
                        impressoras_filiais.append(imp)
            
            else: # Offline
                if ip in bd_por_ip: # IP cadastrado no bd
                    imp_existente = bd_por_ip[ip]
                    controler = ImpressoraController(imp_existente)
                    controler.atualizar_status("Offline")
                    print(f"Impressora:")
                    print(imp_existente)
                    print(f"Existe no banco, mas está offline")
                    impressoras_filiais.append(imp_existente)

    sincronizar_impressoras(impressoras_novas=impressoras_filiais, impressoras_bd=impressoras_bd)

def attImpressora_filial():
    impressoras_bd, impressoras_atualizadas = coletar_statusImpressora()
    sincronizar_impressoras(impressoras_novas=impressoras_atualizadas, impressoras_bd=impressoras_bd)

    print(len(impressoras_atualizadas))
    limpar_tbl("impressora_filial")
    for impressora in impressoras_atualizadas:
        if impressora.status == "Ativo":
            controler = ImpressoraController(impressora)
            insert_tbl_relImpressora(controler)

def attCont_mensais():
    impressoras_bd, impressoras_atualizadas = coletar_statusImpressora()
    sincronizar_impressoras(impressoras_novas=impressoras_atualizadas, impressoras_bd=impressoras_bd)

    for impressora in impressoras_atualizadas:
        if impressora.status == "Ativo":
            insert_tbl_contMensais(impressora)