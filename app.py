from util.scan import scan
from util.snmp import snmp
import pandas as pd
import numpy as np
from util.bd import read_impressoras, insert_tbl_relImpressora, limpar_tbl, conectar_bd

# Recebe as impressoras em objeto ou somente os IPs
ips_impressoras = []

# Realiza o scan nos IPs

# - se retornar on: 
#       OIDs padrão ou manual?
#       envio do snmp
#       recebimento da resposta

# - se retornar off: 
#       adiciona ao um vetor de atualização de status

# Com a resposta acessa o BD e atualiza os contadores e os status das impressoras

def scan_total():
    ignorar = [14,16,17,18,31,32,33,40,43,44,46,47,48,49]

    inicio = "10.0."
    ips_off =[]
    ips_erro = []
    series = []
    modelos =[]
    ips = []
    oids = ['1.3.6.1.2.1.25.3.2.1.3.1', '1.3.6.1.2.1.43.5.1.1.17.1']
    for filial in range(2,54):
        if filial in ignorar:
            continue
        for impressora in range(50,56):
            ip = inicio + str(filial) + "." + str(impressora)
            resp = scan(ip)
            if resp is not None:
                resposta = snmp(resp, oids)
                if len(resposta) == 0:
                    modelos.append("Erro")
                    series.append("Erro")
                    ips_erro.append(ip)
                for resp in resposta:
                    print(resp)
                    print(resp["oid"])
                    print(resp["resposta"])
                    if resp['oid'] == '1.3.6.1.2.1.25.3.2.1.3.1':
                        modelos.append(resp['resposta'])
                    elif resp['oid'] == '1.3.6.1.2.1.43.5.1.1.17.1':
                        series.append(resp['resposta'])
                    if resp['resposta'] == "" or resp['resposta'] is None : resp['resposta'] = "Não encontrado!"
                ips.append(ip)
            else:
                ips_off.append(ip)

    dados = {
        'modelo': modelos,
        'series': series,
        'ips': ips
    }

    df = pd.DataFrame(dados)
    df.to_excel("planilha.xlsx")

def sincronizar_impressoras(impressoras_novas, impressoras_bd):
    bd_por_serie = {imp["num_serie"]: imp for imp in impressoras_bd}
    bd_por_ip = {imp["ip"]: imp for imp in impressoras_bd}

    ips_a_usar = set(nova["ip"] for nova in impressoras_novas if nova["ip"])
    for ip in ips_a_usar:
        if ip in bd_por_ip:
            impressora_conflitante = bd_por_ip[ip]
            print(f"[!] IP {ip} já está em uso por {impressora_conflitante['num_serie']}. Limpando antes de qualquer alteração...")
            conectar_bd(f'UPDATE impressoras SET ip=NULL WHERE num_serie="{impressora_conflitante["num_serie"]}"')
            bd_por_ip[ip]["ip"] = None

    for nova in impressoras_novas:
        
        nova_serie = nova["num_serie"]
        nova_ip = nova["ip"]

        if nova_serie not in bd_por_serie.keys(): # Verifica o número de série
            print("[X] Impressora não está no BD")
            print(f'Inserindo nova impressora: {nova}')

            if nova_ip in bd_por_ip.keys():
                print("[X] IP cadastrado com outra impressora... limpando ip da impressora antiga!")
                imp_antiga = bd_por_ip[nova_ip]
                comando = f'UPDATE impressoras SET ip=NULL where num_serie="{imp_antiga["num_serie"]}"'
                conectar_bd(comando)



            tipo = "Laser" if "ZD230" not in nova["modelo"] else "Térmica"
            ip_value = "NULL" if nova["ip"] is None else f'"{nova["ip"]}"'
            comando = f'INSERT INTO impressoras (num_serie, modelo, tipo, ip, status, conexao) VALUES ("{nova["num_serie"]}", "{nova["modelo"]}", "{tipo}", {ip_value}, "{"Ativo"}", "{"IP"}")'
            conectar_bd(comando)

        else: # num_serie está cadastrado ja
            print("[✓] Impressora está no BD")
            atual = bd_por_serie[nova_serie]

            # Preserva a conexão se a nova estiver vazia
            nova_conexao = nova["conexao"] if nova["conexao"] else atual["conexao"]

            # Monta o update apenas se houver alterações
            alterou = False
            updates = []

            if atual["ip"] != nova["ip"]:
                ip_value = "NULL" if nova["ip"] is None else f'"{nova["ip"]}"'
                updates.append(f'ip={ip_value}')
                alterou = True

            if atual["modelo"] != nova["modelo"]:
                updates.append(f'modelo="{nova["modelo"]}"')
                alterou = True

            if atual["tipo"] != nova["tipo"]:
                updates.append(f'tipo="{nova["tipo"]}"')
                alterou = True

            if atual["status"] != nova["status"]:
                updates.append(f'status="{nova["status"]}"')
                alterou = True

            if atual["conexao"] != nova_conexao:
                updates.append(f'conexao="{nova_conexao}"')
                alterou = True

            if alterou:
                update_query = f'UPDATE impressoras SET {", ".join(updates)} WHERE num_serie="{nova_serie}"'
                conectar_bd(update_query)
                print(f"[UPDATE] Impressora {nova_serie} atualizada.")
    print("\n[✓] Impressoras sincronizadas.")

def attImpressora_filial():
    
    impressoras_leitura = read_impressoras()

    impressoras_bd = []
    impressoras_atualizadas = []
    
    '''
    impressora[0] = série
    impressora[1] = modelo
    impressora[2] = tipo (ignorar)
    impressora[3] = ip
    impressora[4] = status
    impressora[5] = tipo de conexão (ignorar)
    '''

    for leitura in impressoras_leitura:
        impressora_bd = {
            "num_serie": leitura[0],
            "modelo": leitura[1],
            "tipo": leitura[2],
            "ip": leitura[3],
            "filial_id": leitura[3],
            "status": leitura[4],
            "conexao": leitura[5]
        }

        impressoras_bd.append(impressora_bd)

        impressora = {
            "num_serie": leitura[0],
            "modelo": leitura[1],
            "tipo": leitura[2],
            "ip": leitura[3],
            "filial_id": leitura[3],
            "status": leitura[4],
            "conexao": leitura[5]
        }

        ip_segmentado = impressora["ip"].split(".")
        if ip_segmentado[0] == "192" or ip_segmentado[1] == "18":
            impressora["filial_id"] = "1"
        else:
            impressora["filial_id"] = impressora["ip"].split(".")[2]


        ''' ANOTAÇÃO PARA ADICIONAR AO CÓDIGO
            * Variavel de controle de mudança:
                inserir um váriavel alterado, e checar se os dados da impressora e os dados recebidos (exceto o contador) houveram mudanças.
        '''
        
        if impressora["filial_id"] == "1" or "ZD230" in impressora["modelo"]:
            continue

        if scan(impressora["ip"]):
            oids = snmp(impressora["ip"])
            if len(oids) > 0:
                for oid in oids:
                    impressora["status"] = "Ativo"
                    
                    # n° de série
                    if oid["oid"] == "1.3.6.1.2.1.43.5.1.1.17.1":
                        impressora["num_serie"] = oid["resposta"]
                    
                    # modelo
                    if oid["oid"] == "1.3.6.1.2.1.25.3.2.1.3.1":
                        impressora["modelo"] = oid["resposta"]
                    
                    # contador
                    #if oid["oid"] == "1.3.6.1.2.1.43.10.2.1.4.1.1":
                    #    impressora["contador"] = oid["resposta"]
            else:
                impressora["status"] = "Erro no SNMP"
        else:
            impressora["status"] = "Offline"

        
        #print(impressora)
        impressoras_atualizadas.append(impressora)   

    sincronizar_impressoras(impressoras_novas=impressoras_atualizadas, impressoras_bd=impressoras_bd)

    print(len(impressoras_atualizadas))
    limpar_tbl("impressora_filial")
    for impressora in impressoras_atualizadas:
        if impressora["status"] == "Ativo":
            print(impressora)
            insert_tbl_relImpressora(impressora)

def attCont_mensais():
    impressoras_leitura = read_impressoras()
    print(impressoras_leitura)

    impressoras_bd = []

    for leitura in impressoras_leitura:
        impressora_bd = {
            "num_serie": leitura[0],
            "modelo": leitura[1],
            "tipo": leitura[2],
            "ip": leitura[3],
            "filial_id": leitura[3],
            "status": leitura[4],
            "conexao": leitura[5],
            "contador": 0
        }

        impressoras_bd.append(impressora_bd)
    
        impressora = {
            "num_serie": leitura[0],
            "modelo": leitura[1],
            "tipo": leitura[2],
            "ip": leitura[3],
            "filial_id": leitura[3],
            "status": leitura[4],
            "conexao": leitura[5]
        }

        ip_segmentado = impressora["ip"].split(".")
        if ip_segmentado[0] == "192" or ip_segmentado[1] == "18":
            impressora["filial_id"] = "1"
        else:
            impressora["filial_id"] = impressora["ip"].split(".")[2]
        
        if impressora["filial_id"] == "1" or "ZD230" in impressora["modelo"]: # temporario
            continue

        if scan(impressora["ip"]):
            oids = snmp(impressora["ip"])
            if len(oids) > 0:
                for oid in oids:
                    impressora["status"] = "Ativo"
                    
                    # n° de série
                    if oid["oid"] == "1.3.6.1.2.1.43.5.1.1.17.1":
                        impressora["num_serie"] = oid["resposta"]
                    
                    # modelo
                    if oid["oid"] == "1.3.6.1.2.1.25.3.2.1.3.1":
                        impressora["modelo"] = oid["resposta"]
                    
                    # contador
                    if oid["oid"] == "1.3.6.1.2.1.43.10.2.1.4.1.1":
                        impressora["contador"] = oid["resposta"]
            else:
                impressora["status"] = "Erro no SNMP"
        else:
            impressora["status"] = "Offline"  

attImpressora_filial()