from classes.ImpressoraController import ImpressoraController
from classes.Impressora import Impressora
from .bd_service import read_impressoras, limpar_tbl, insert_tbl_relImpressora, insert_tbl_contMensais, read_tbl_filiais
from .sync_service import sincronizar_impressoras
from typing import Tuple
from .validacao import validar_impressora, validar_ipv4
from util.loggin import log_info, log_error
import copy

def scan_bd() -> Tuple[list[Impressora]]:
    impressoras_bd: list[Impressora] = read_impressoras()
    impressoras_leitura = copy.deepcopy(impressoras_bd)

    impressoras_atualizadas: list = []
    
    for imp in impressoras_leitura:
        if imp.ip is not None:
            log_info(f"Processando impressora: IP {imp.ip}, Série {imp.num_serie}")
            controler = ImpressoraController(imp)
            controler.set_filialId()
            if "ZD230" in imp.modelo or imp.filial_id == "1":
                continue
            controler.atualizar_dados_snmp()
            log_info(f"Dados SNMP atualizados para IP {imp.ip}")
            impressoras_atualizadas.append(imp)
        else:
            log_info(f"Impressora ignorada: sem IP definido (Série {imp.num_serie})")
    
    sincronizar_impressoras(impressoras_atualizadas, impressoras_bd)
    return impressoras_atualizadas


def scan_filiais():
    log_info("Iniciando scan total das filiais...")
    filiais_bd = read_tbl_filiais()
    impressoras_bd = read_impressoras()
    
    faixa_filial = range(50, 56)
    impressoras_filiais = []

    for filial in filiais_bd:
        log_info(f"Rodando na filial {filial.id}")
        for impressora in faixa_filial:
            ip = f"10.0.{str(filial.id)}.{str(impressora)}"
            log_info(f"Testando IP {ip}")
            imp = validar_impressora(ip, impressoras_bd)
            if imp is not None:
                log_info(f"Impressora encontrada no IP {ip}: Série {imp.num_serie}")
                impressoras_filiais.append(imp)
    log_info("Finalizado scan das filiais.")

    sincronizar_impressoras(impressoras_novas=impressoras_filiais, impressoras_bd=impressoras_bd)
    return impressoras_filiais


def scan_manual():
    impressora_atulizar = []
    impressoras_bd = read_impressoras()

    ip = input("digite o IP (ex: 255.255.255.255, 10.0.0.1...): ").strip()
    if ip is not None:
        if "-" not in ip:  # IP único
            if validar_ipv4(ip):
                log_info(f"IP digitado: {ip}")
                imp = validar_impressora(ip, impressoras_bd)
                if imp:
                    log_info(f"Impressora validada manualmente: Série {imp.num_serie}, IP {imp.ip}")
                    impressora_atulizar.append(imp)
            else:
                log_error(f"IP inválido digitado: {ip}")
        else:
            log_info(f"Faixa de IPs detectada: {ip} (ainda não implementado)")

    sincronizar_impressoras(impressoras_novas=impressora_atulizar, impressoras_bd=impressoras_bd)


def attImpressora_filial(impressoras_atualizadas):
    log_info(f"Atualizando impressoras-filiais: {len(impressoras_atualizadas)} impressoras")
    limpar_tbl("impressora_filial")
    for impressora in impressoras_atualizadas:
        if impressora.status == "Ativo":
            insert_tbl_relImpressora(impressora)
            log_info(f"Relacionamento inserido: Série {impressora.num_serie}, Filial {impressora.filial_id}")


def attCont_mensais(impressoras_atualizadas):
    atualizadas_por_serie = [imp.num_serie for imp in impressoras_atualizadas]
    for impressora in impressoras_atualizadas:
        if impressora.status == "Ativo":
            insert_tbl_contMensais(impressora)
            log_info(f"Contador mensal inserido: Série {impressora.num_serie}, Contador {impressora.contador}")
    log_info(f"Total de impressoras atualizadas: {len(atualizadas_por_serie)}")
    log_info(f"Séries atualizadas: {atualizadas_por_serie}")
