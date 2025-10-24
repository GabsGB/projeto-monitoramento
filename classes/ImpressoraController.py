from util.scan import scan
from util.snmp import snmp
from services.bd_service import conectar_bd
from util.loggin import log_info, log_error

class ImpressoraController:
    def __init__(self, impressora=None):
        self.impressora = impressora
    

    def __str__(self):
        return (
            f'num_serie: {self.impressora.num_serie}, '
            f'modelo: {self.impressora.modelo}, '
            f'tipo: {self.impressora.tipo}, '
            f'ip: {self.impressora.ip}, '
            f'filial_id: {self.impressora.filial_id}, '
            f'status: {self.impressora.status}, '
            f'conexao: {self.impressora.conexao}, '
            f'contador: {self.impressora.contador}'
        )


    
    def set_impressora(self, nova_impressora):
        self.impressora = nova_impressora


    def set_filialId(self):
        if self.impressora.ip is None:
            self.impressora.filial_id = "-"
        else:
            ip_segmentado = self.impressora.ip.split(".")
            if ip_segmentado[0] == "192" or ip_segmentado[1] == "18":
                self.impressora.filial_id = "1"
            else:
                self.impressora.filial_id = ip_segmentado[2]


    def set_status(self, status):
        self.impressora.status = status


    def set_tipo(self, tipo=None):
        if tipo is None:
            self.impressora.tipo = "Térmica" if "ZD230" in self.impressora.modelo else "Laser"
        else:
            self.impressora.tipo = tipo


    def atualizar_dados_snmp(self):
        if scan(self.impressora.ip):
            oids = snmp(self.impressora.ip)
            if not oids:
                self.impressora.status = "Erro no SNMP"
                log_error(f"Erro ao obter dados SNMP para IP {self.impressora.ip}")
                return
        
            self.impressora.status = "Ativo"
            for oid in oids:
                if oid["oid"] == "1.3.6.1.2.1.43.5.1.1.17.1":
                    self.impressora.num_serie = oid["resposta"] or "Não encontrado!"
                if oid["oid"] == "1.3.6.1.2.1.25.3.2.1.3.1":
                    self.impressora.modelo = oid["resposta"] or "Não encontrado!"
                if oid["oid"] == "1.3.6.1.2.1.43.10.2.1.4.1.1":
                    self.impressora.contador = oid["resposta"] or "Não encontrado!"
            self.set_tipo()
            log_info(f"Dados SNMP atualizados para IP {self.impressora.ip}")
        else:
            self.impressora.status = "Offline"
            log_info(f"Impressora offline: IP {self.impressora.ip}")
        
        self.set_filialId()


    def limparIp(self):
        self.impressora.ip = None


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


    def salvar_bd(self, antigo=None):
        if antigo is None:
            ip_value = 'NULL' if self.impressora.ip is None else f'"{self.impressora.ip}"'
            if self.impressora.conexao != "USB":
                self.impressora.conexao = "IP"
            
            comando = f'''
                INSERT INTO impressoras (num_serie, modelo, tipo, ip, status, conexao)
                VALUES ("{self.impressora.num_serie}", "{self.impressora.modelo}", "{self.impressora.tipo}", {ip_value}, "{self.impressora.status}", "{self.impressora.conexao}")
            '''
            conectar_bd(comando)
            log_info(f"[INSERT] Impressora {self.impressora.num_serie} adicionada ao banco.")
        else:
            updates = []
            def add_update(campo, valor):
                if isinstance(valor, str): 
                    updates.append(f'{campo}="{valor}"')
                elif valor is None:
                    updates.append(f'{campo}=NULL')
                else:
                    updates.append(f'{campo}={valor}')
            
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
                log_info(f"[UPDATE] Impressora {self.impressora.num_serie} atualizada com alterações: {updates}")
            else:
                log_info(f"[✓] Impressora {self.impressora.num_serie} sem alterações.")

