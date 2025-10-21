from classes.ImpressoraController import ImpressoraController
from util.loggin import log_info, log_error
import copy

def sincronizar_impressoras(impressoras_novas, impressoras_bd):
    bd_por_serie = {imp.num_serie: imp for imp in impressoras_bd}
    #for imp in bd_por_serie:
    #    print(imp)

    bd_por_ip = {imp.ip: imp for imp in impressoras_bd}

    for nova in impressoras_novas:
        log_info(f"Sincronizando impressora: Série {nova.num_serie}, IP {nova.ip}")
        
        if not nova.num_serie:
            log_error(f"Impressora sem número de série. IP: {nova.ip}, Modelo: {nova.modelo}")
            continue

        if nova.num_serie not in bd_por_serie:
            log_info(f"[X] Impressora não está no BD: Série {nova.num_serie}")

            if nova.ip in bd_por_ip:
                imp_antiga = copy.deepcopy(bd_por_ip[nova.ip])
                controler = ImpressoraController(imp_antiga)
                log_info(f"[X] IP {nova.ip} já cadastrado com outra impressora ({imp_antiga.num_serie}). Limpando IP da impressora antiga.")
                controler.limparIp()
                controler.salvar_bd(bd_por_ip[nova.ip])
            else:
                log_info(f"IP {nova.ip} disponível para uso.")

            controler = ImpressoraController(nova)
            controler.salvar_bd()

        else:
            log_info(f"[✓] Impressora já está no BD: Série {nova.num_serie}, Ip: {nova.ip}, Status: {nova.status}")
            atual = bd_por_serie[nova.num_serie]
            #print()
            #print(nova)
            #print()
            #print(atual)

            if nova.ip != atual.ip and nova.ip in bd_por_ip:
                imp_antiga = copy.deepcopy(bd_por_ip[nova.ip])
                controler = ImpressoraController(imp_antiga)
                
                log_info(f"[X] IP {nova.ip} já cadastrado com outra impressora ({imp_antiga.num_serie}). Limpando IP da impressora antiga.")
                controler.limparIp()
                controler.salvar_bd(bd_por_ip[nova.ip])

            controler = ImpressoraController(nova)
            controler.salvar_bd(atual)

    log_info("[✓] Impressoras sincronizadas com sucesso.")

