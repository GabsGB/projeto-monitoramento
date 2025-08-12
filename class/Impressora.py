class Impressora():
    def __init__(self, num_serie, modelo, tipo, ip, filial_id, status, conexao, contador):
        self.num_serie = num_serie
        self.modelo = modelo
        self.tipo = tipo
        self.ip = ip
        self.filial_id = filial_id
        self.status = status
        self.conexao = conexao
        self.contador = contador      
        pass

    def atualizar_filialId(self):
        ip_segmentado = self.ip.split(".")
        if ip_segmentado[0] == "192" or ip_segmentado[1] == "18":
            self.filial_id = "1"
        else:
            self.filial_id = self.ip.split(".")[2]

    def atualizar_dados_snmp(self, oids):
        if not oids:
            self.status = "Erro no SNMP"
            return

        self.status = "Ativo"
        for oid in oids:
            # n° de série
            if oid["oid"] == "1.3.6.1.2.1.43.5.1.1.17.1": # N° de série
                self.num_serie = oid["resposta"] or "Não encontrado!"
            
            # modelo
            if oid["oid"] == "1.3.6.1.2.1.25.3.2.1.3.1": # Modelo
                self.num_serie = oid["resposta"] or "Não encontrado!"
            
            # contador
            if oid["oid"] == "1.3.6.1.2.1.43.10.2.1.4.1.1": # Contador
                self.num_serie = oid["resposta"] or "Não encontrado!"