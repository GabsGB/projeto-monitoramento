import pandas as pd
import smtplib
import email.message

# 1. Carregar planilha
#df = pd.read_excel("impressoras.xlsx", sheet_name="base_de_dados")
print(2,58)
print(df)
'''
# 2. Definir mês atual e anterior
mes_atual = "JUNHO"
mes_anterior = "MAIO"

# 3. Iterar pelas filiais
for filial, grupo in df.groupby("Filial"):
    gasto_atual = grupo[mes_atual].sum()
    gasto_anterior = grupo[mes_anterior].sum()
    
    # 4. Criar corpo do email
    corpo = f"""
    <h3>Relatório da Filial {filial}</h3>
    <p><b>Gasto em {mes_anterior}:</b> R$ {gasto_anterior:,.2f}</p>
    <p><b>Gasto em {mes_atual}:</b> R$ {gasto_atual:,.2f}</p>
    <br>
    <p>Segue lista de impressoras:</p>
    {grupo[['Modelo','Série Fabricante','IMPRESSORA',mes_anterior,mes_atual]].to_html(index=False)}
    """

    # 5. Montar email
    msg = email.message.Message()
    msg['Subject'] = f"Relatório Impressoras - {filial}"
    msg['From'] = "seuemail@dominio.com"
    msg['To'] = "email_filial@dominio.com"  # <- puxar da aba 'Email filiais'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo)

    # 6. Enviar (exemplo com Outlook SMTP)
    s = smtplib.SMTP('smtp-mail.outlook.com', 587)
    s.starttls()
    s.login("seuemail@dominio.com", "sua_senha")
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    s.quit()
'''