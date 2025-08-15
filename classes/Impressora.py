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