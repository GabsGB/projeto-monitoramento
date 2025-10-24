import mariadb
import sys
from classes.Impressora import Impressora
from classes.Filial import Filial
from util.loggin import log_info, log_error

def conectar_bd(comando, method='insert'):
    try:
        conector = mariadb.connect(
            host="192.168.0.197",
            port=3306,
            user='root@localhost',
            password="-admin123",
            database="solupress_coplacana")
        log_info("Conexão ao Banco de Dados realizada com sucesso.")
    except mariadb.Error as e:
        log_error(f"Erro ao se conectar à plataforma do MariaDB: {e}")
        sys.exit(1)
    except Exception as e:
        log_error(f"[ERRO BANCO] Comando: {comando}")
        log_error(f"[ERRO BANCO] Erro: {e}")
    
    cursor = conector.cursor()
    log_info(f"Executando comando SQL: {comando}")
    cursor.execute(comando)
    conector.commit()

    if method == "read":
        resposta = cursor.fetchall()
        return resposta
    cursor.close()


def insert_tbl_filiais(filial):
    comando = f'INSERT INTO filiais VALUES ({int(filial.num)}, "{filial.nome}")'
    conectar_bd(comando)


def read_tbl_filiais():
    comando = 'SELECT * FROM filiais'
    filiais_leitura = conectar_bd(comando, method='read')
    filiais_bd = []
    for leitura in filiais_leitura:
        filial = Filial(leitura[0], leitura[1])
        filiais_bd.append(filial)
    return filiais_bd


def update_tbl_filiais():
    return


def delete_tbl_filiais():
    return


def insert_tbl_impressoras(impressora):
    ip_value = "NULL" if impressora.ip is None else f'"{impressora.ip}"'
    comando = f'INSERT INTO impressoras(num_serie, modelo, tipo, ip, conexao) VALUES ("{impressora.num_serie}", "{impressora.modelo}", "{impressora.tipo}", {ip_value}, "{impressora["conexao"]}")'
    log_info(f"Comando SQL gerado para impressora: {comando}")
    conectar_bd(comando)


def insert_tbl_relImpressora(impressora):
    comando = f'INSERT INTO impressora_filial(num_serie, filial_id, status) VALUES ("{impressora.num_serie}", "{impressora.filial_id}", "{impressora.status}")'
    conectar_bd(comando)


def limpar_tbl(tabela):
    comando = f'truncate {tabela.lower()}'
    conectar_bd(comando)


def read_impressoras():
    comando = 'SELECT * FROM impressoras'
    impressoras = conectar_bd(comando, method='read')
    impressoras_bd = []
    for leitura in impressoras:
        imp = Impressora(leitura[0], leitura[1], leitura[2], leitura[3], leitura[4], leitura[5])
        log_info(f"Impressora carregada: n° de série: {imp.num_serie}, IP: {imp.ip} status: {imp.status}",)
        impressoras_bd.append(imp)
    return impressoras_bd


def insert_tbl_contMensais(impressora):
    log_info(f'Impressora a ser inserida: \nN{impressora}')
    comando = f'''
    INSERT INTO contadores_mensais (num_serie, filial_id, contador, estado)
    VALUES (
    '{impressora.num_serie}', 
    '{impressora.filial_id}', 
    {float(impressora.contador) if impressora.contador is not None else float(0)},
    '{"Ok" if impressora.contador is not None else 'Verificar'}')
    '''
    conectar_bd(comando)
    return

