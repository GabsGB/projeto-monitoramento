import mariadb
import sys

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


#def show_tables():


#  FUNÇÕES CRUD FILIAIS

def insert_filial():
    while True:
        filial_num = input("Digite o número da filial: ")
        if filial_num == "0":break
        filial_nome = input("Digite o nome da filial: ")
        confirmacao = input(f"Deseja adicionar a filial {filial_num} - {filial_nome}  S/N: ")
        if confirmacao.lower() == "s":
            comando = f'INSERT INTO filiais VALUES ({int(filial_num)}, "{filial_nome}")'
            conectar_bd(comando)
        filial_num = filial_nome = ""

def read_filiais():
    comando = 'SELECT * FROM teste.filiais'
    filiais = conectar_bd(comando, method='read')
    return filiais

def alter_filiais():
    return

def delete_filiais():
    return

#  FUNÇÕES CRUD IMPRESSORAS
def insert_tbl_impressora(impressora):
    # Preparar a consulta SQL, tratando NULL para o campo ip
    ip_value = "NULL" if impressora["ip"] is None else f'"{impressora["ip"]}"'
    comando = f'INSERT INTO impressoras(num_serie, modelo, tipo, ip, conexao) VALUES ("{impressora["num_serie"]}", "{impressora["modelo"]}", "{impressora["tipo"]}", {ip_value}, "{impressora["conexao"]}")'
    
    print(comando)  # Verificar a consulta SQL gerada
    conectar_bd(comando)

def insert_tbl_relImpressora(impressora):
    # Preparar a consulta SQL, tratando NULL para o campo ip
    comando = f'INSERT INTO impressora_filial(num_serie, filial_id, status) VALUES ("{impressora["num_serie"]}", "{impressora["filial_id"]}", "{impressora["status"]}")' 
    conectar_bd(comando)

def limpar_tbl(tabela):
    #Inserir uma verificação da entrada
    comando = f'truncate {tabela.lower()}'
    conectar_bd(comando)

def read_impressoras():
    comando = 'SELECT * FROM teste.impressoras WHERE ip != ""'
    impressoras = conectar_bd(comando, method='read')

    return impressoras
    
#