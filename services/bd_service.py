import mariadb
import sys
from classes.Impressora import Impressora
from classes.Filial import Filial

def conectar_bd(comando, method='insert'):
    
    try:
        conector = mariadb.connect(
            user='root@localhost',
            password="-admin123",
            host="127.0.0.1",
            port=3306,
            database="teste")
        print("\nConexão ao Banco de Dados realizada com sucesso!\n")
    except mariadb.Error as e:
        print(f"Erro ao se conectar a plataforma do MariaDB: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"[ERRO BANCO] Comando: {comando}")
        print(f"[ERRO BANCO] Erro: {e}")
    
    cursor = conector.cursor()
    print(comando)
    cursor.execute(comando)
    conector.commit()

    if method=="read":
        resposta = cursor.fetchall()
        return resposta
    cursor.close()

#  FUNÇÕES CRUD FILIAIS

def insert_tbl_filiais(filial):
    comando = f'INSERT INTO filiais VALUES ({int(filial.num)}, "{filial.nome}")'
    conectar_bd(comando)


def read_filiais():
    comando = 'SELECT * FROM teste.filiais'
    filiais_leitura = conectar_bd(comando, method='read')
    filiais_bd = []
    for leitura in filiais_leitura:
        filial = Filial(leitura[0], leitura[1])
        filiais_bd.append(filial)
    return filiais_bd


def alter_filiais():
    return


def delete_filiais():
    return

#  FUNÇÕES CRUD IMPRESSORAS
def insert_tbl_impressoras(impressora): # alterar o código para POO
    # Preparar a consulta SQL, tratando NULL para o campo ip
    ip_value = "NULL" if impressora.ip is None else f'"{impressora.ip}"'
    comando = f'INSERT INTO impressoras(num_serie, modelo, tipo, ip, conexao) VALUES ("{impressora.num_serie}", "{impressora.modelo}", "{impressora.tipo}", {ip_value}, "{impressora["conexao"]}")'
    
    print(comando)  # Verificar a consulta SQL gerada
    conectar_bd(comando)


def insert_tbl_relImpressora(impressora): # alterar o código para POO
    # Preparar a consulta SQL, tratando NULL para o campo ip
    comando = f'INSERT INTO impressora_filial(num_serie, filial_id, status) VALUES ("{impressora.num_serie}", "{impressora.filial_id}", "{impressora.status}")' 
    conectar_bd(comando)


def limpar_tbl(tabela):
    #Inserir uma verificação da entrada
    comando = f'truncate {tabela.lower()}'
    conectar_bd(comando)


def read_impressoras():
    comando = 'SELECT * FROM teste.impressoras'
    impressoras = conectar_bd(comando, method='read')
    impressoras_bd = []
    for leitura in impressoras:
        #print(leitura)
        imp = Impressora(leitura[0], leitura[1], leitura[2], leitura[3], leitura[4], leitura[5])
        print(imp.num_serie)
        #print(imp.ip)
        impressoras_bd.append(imp)
    bd_por_serie = {imp.num_serie: imp for imp in impressoras_bd}
    print(bd_por_serie.keys())
    return impressoras_bd


def insert_tbl_contMensais(impressora):
    
    #print(f'''
    #    "num_serie": {impressora.num_serie},
    #        "modelo": {impressora.modelo},
    #        "tipo": self.{impressora.tipo},
    #        "ip": self.{impressora.ip},
    #        "filial_id": self.{impressora.filial_id},
    #        "status": self.{impressora.status},
    #        "conexao": self.{impressora.conexao},
    #        "contador": self.{impressora.contador}
    #''')

    comando = f'''
    INSERT INTO contadores_mensais (num_serie, filial_id, contador)
    VALUES ("{impressora.num_serie}", {int(impressora.filial_id)}, {float(impressora.contador)})
    '''
    conectar_bd(comando)
    return

