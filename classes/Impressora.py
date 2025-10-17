class Impressora():
    def __init__(self, num_serie=None, modelo=None, tipo=None, ip=None, status=None, conexao=None):
        self.num_serie = num_serie
        self.modelo = modelo
        self.tipo = tipo
        self.ip = ip
        self.status = status
        self.conexao = conexao
        # atribustos definidos posteriormente
        self.filial_id = None
        self.contador = None
    
    def __str__(self):
        return f"""
            "num_serie": {self.num_serie},
            "modelo": {self.modelo},
            "tipo": {self.tipo},
            "ip": {self.ip},
            "filial_id": {self.filial_id},
            "status": {self.status},
            "conexao": {self.conexao},
            "contador": {self.contador}
            """