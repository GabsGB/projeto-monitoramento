from classes.ImpressoraController import ImpressoraController
import copy

def sincronizar_impressoras(impressoras_novas, impressoras_bd):
    # Índices rápidos por série e ip

    bd_por_serie = { imp.num_serie: imp for imp in impressoras_bd}
    #print(bd_por_serie.keys())    
    bd_por_ip = { imp.ip: imp for imp in impressoras_bd}
    #print(bd_por_ip.keys())

    for nova in impressoras_novas:
        print(f"\nN° de série: {nova.num_serie}")
        print(f"IP: {nova.ip}")
        
        if not nova.num_serie:
            print(f"Impressora sem N° de série \nIP: {nova.ip}\nSérie:{nova.num_serie}\nModelo:{nova.modelo}")
            continue

        if nova.num_serie not in bd_por_serie: # Verifica se a imrpessora não esta cadastrada pelo n° de série
            print(f"[X] Impressora não está no BD")
            #print(f'Inserindo nova impressora: {nova}')

            if nova.ip in bd_por_ip: # Verifica se o IP dela esta sendo usado por outra impressora
                imp_antiga = copy.deepcopy(bd_por_ip[nova.ip])
                controler = ImpressoraController(imp_antiga)
                print(f"[X] IP cadastrado com outra impressora {imp_antiga.num_serie} ... limpando ip da impressora antiga!")
                controler.limparIp()
                controler.salvar_bd(bd_por_ip[nova.ip])
                
            else:
                print("IP disponivel!")
            
            controler = ImpressoraController(nova)
            controler.salvar_bd()

        else: # num_serie está cadastrado ja
            print("[✓] Impressora está no BD")
            atual = bd_por_serie[nova.num_serie] # recebe os dados da impressora do BD (versão antiga)

            if nova.ip != atual.ip and nova.ip in bd_por_ip:
                imp_antiga = copy.deepcopy(bd_por_ip[nova.ip])
                controler = ImpressoraController(imp_antiga)
                print(f"[X] IP cadastrado com outra impressora {imp_antiga.num_serie} ... limpando ip da impressora antiga!")
                controler.limparIp()
                controler.salvar_bd(bd_por_ip[nova.ip])

            controler = ImpressoraController(nova) # recebe a impressora após o scan
            controler.salvar_bd(atual) # verifica se possui atualizações e se tiver salva
        
    print("\n[✓] Impressoras sincronizadas.")
