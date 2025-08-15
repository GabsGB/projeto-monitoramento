from services.scan_service import attCont_mensais, scan_filiais

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
if __name__ == "__main__":
    scan_filiais()
    pass


#attCont_mensais()