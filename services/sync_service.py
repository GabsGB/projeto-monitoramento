from classes.ImpressoraController import ImpressoraController

def sincronizar_impressoras(impressoras_novas, impressoras_bd):
    # Índices rápidos por série e ip
    bd_por_serie = { imp.num_serie: imp for imp in impressoras_bd}
    bd_por_ip = { imp.ip: imp for imp in impressoras_bd}

    ips_a_usar = set(nova.ip for nova in impressoras_novas if nova.ip)

    for ip in ips_a_usar:
        if ip in bd_por_ip:
            impressora_conflitante = bd_por_ip[ip]
            controler = ImpressoraController(impressora_conflitante)
            print(f"[!] IP {ip} já está em uso por {impressora_conflitante.num_serie}. Limpando antes de qualquer alteração...")
            controler.limparIp()
            controler.salvar_bd(impressora_conflitante)
            bd_por_ip[ip].ip = None

    for nova in impressoras_novas:
        if nova.num_serie not in bd_por_serie: # Verifica se a imrpessora não esta cadastrada pelo n° de série
            print("[X] Impressora não está no BD")
            print(f'Inserindo nova impressora: {nova}')

            if nova.ip in bd_por_ip: # Verifica se o IP dela esta sendo usado por outra impressora
                print("[X] IP cadastrado com outra impressora... limpando ip da impressora antiga!")
                imp_antiga = bd_por_ip[nova.ip]
                controler = ImpressoraController(imp_antiga)
                controler.limparIp()
                controler.salvar_bd(imp_antiga)
            
            controler = ImpressoraController(nova)
            controler.salvar_bd()

        else: # num_serie está cadastrado ja
            print("[✓] Impressora está no BD")
            atual = bd_por_serie[nova.num_serie]
            controler = ImpressoraController(nova)
            controler.salvar_bd(atual)
    print("\n[✓] Impressoras sincronizadas.")
