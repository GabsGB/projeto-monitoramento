import smtplib
import email.message
from datetime import datetime
from calendar import month_name

def enviar_email():
    data_atual = datetime.now()
    mes_atual = data_atual.month

    if mes_atual == 1:
        mes_anterior = 12
    else:
        mes_anterior = mes_atual - 1

    mes_atual = month_name[mes_atual]
    mes_anterior = month_name[mes_anterior]

    linhas = ""
    for imp in impressoras:
        linhas += f"""
        <tr>
            <td>{imp.posicao}</td>
            <td>{imp.num_serie}</td>
            <td>{imp.contador_mesAnterior}</td>
            <td>{imp.contador_mesAtual}</td>
        </tr>
        """





    server_smtp = "smtp-mail.outlook.com"
    port = 587
    sender_email = "" # meu email
    password = "" # senha

    reciver_email = ''
    subject = ''
    body = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Tabela no e-mail</title>
    </head>
    <body>
        <div>
            <table>
                <thead>
                    <tr>
                        <th>Impressora</th>
                        <th>Série</th>
                        <th> impressões {mes_anterior}</th>
                        <th> impressões {mes_atual}</th>
                    </tr>
                </thead>
                <tbody>
                    {linhas}
                </tbody>
            </table>
        </div>
    </body>
    </html>
    """