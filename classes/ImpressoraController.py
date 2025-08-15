from util.scan import scan
from util.snmp import snmp
from services.bd_service import conectar_bd

class ImpressoraController:
    def __init__(self, impressora):
        self.impressora = impressora
    
    def atualizar_filialId(self):
        ip_segmentado = self.impressora.ip.split(".")
        if ip_segmentado[0] == "192" or ip_segmentado[1] == "18":
            self.impressora.filial_id = "1"
        else:
            self.impressora.filial_id = ip_segmentado[2]

    def atualizar_dados_snmp(self):
        
        if scan(self.impressora.ip):
            oids = snmp(self.impressora.ip)
            if not oids:
                self.impressora.status = "Erro no SNMP"
                return
        
            self.impressora.status = "Ativo"
            for oid in oids:
                # n° de série
                if oid["oid"] == "1.3.6.1.2.1.43.5.1.1.17.1": # N° de série
                    self.impressora.num_serie = oid["resposta"] or "Não encontrado!"
                
                # modelo
                if oid["oid"] == "1.3.6.1.2.1.25.3.2.1.3.1": # Modelo
                    self.impressora.modelo = oid["resposta"] or "Não encontrado!"
                
                # contador
                if oid["oid"] == "1.3.6.1.2.1.43.10.2.1.4.1.1": # Contador
                    self.impressora.contador = oid["resposta"] or "Não encontrado!"
            self.atualizar_tipo()

        else:
            self.atualizar_status("Offline")


    def atualizar_status(self, status):
        self.impressora.status = status


    def atualizar_tipo(self, tipo=None):
        if tipo is None:
            self.impressora = "Laser" if "ZD230" in self.impressora.modelo else "Térmica"
        else:
            self.impressora.tipo = tipo


    def to_dict(self):
        return {
            "num_serie": self.impressora.num_serie,
            "modelo": self.impressora.modelo,
            "tipo": self.impressora.tipo,
            "ip": self.impressora.ip,
            "filial_id": self.impressora.filial_id,
            "status": self.impressora.status,
            "conexao": self.impressora.conexao,
            "contador": self.impressora.contador
        }   

    def salvar_bd(self, antigo=None): # Se for realizar insert somente chamar a função, para update mandar o objeto antigo
        if antigo is None: 
            # 🔹 INSERT - impressora nova
            ip_value = 'NUll' if self.impressora.ip is None else '"'+self.impressora.ip+'"'
            self.impressora.tipo = 'Laser' if "ZD230" in self.impressora.modelo else 'Térmica'
            if self.impressora.conexao != "USB": self.impressora.conexao = "IP"
            
            comando = F'''
                INSERT INTO impressoras (num_serie, modelo, tipo, ip, status, conexao)
                VALUES ("{self.impressora.num_serie}", "{self.impressora.modelo}", "{self.impressora.tipo}", {ip_value}, "{self.impressora.status}", "{self.impressora.conexao}")
            '''
            conectar_bd(comando)

        updates = []

        def add_update(campo, valor):
            if isinstance(valor, str): 
                updates.append(f'{campo}="{valor}"') # Se o valor for uma string
            elif valor is None:
                updates.append(f'{campo}=NULL') # Se o valor for vazio
            else:
                updates.append(f'{campo}={valor}') # Se o valor for númerico
        
        if self.impressora.modelo != antigo.modelo:
            add_update("modelo", self.impressora.modelo)
        if self.impressora.tipo != antigo.tipo:
            add_update("tipo", self.impressora.tipo)
        if self.impressora.ip != antigo.ip:
            add_update("ip", self.impressora.ip)
        if self.impressora.status != antigo.status:
            add_update("status", self.impressora.status)
        if self.impressora.conexao != antigo.conexao:
            add_update("conexao", self.impressora.conexao)
        
        if updates:
            comando = f'UPDATE impressoras SET {", ".join(updates)} WHERE num_serie="{self.impressora.num_serie}"'
            conectar_bd(comando)
            print(f"[UPDATE] Impressora {self.impressora.num_serie} atualizada.")
        else:
            print(f"[✓] Impressora {self.impressora.num_serie} sem alterações.")
        
    def limparIp(self):
        self.impressora.ip = None
