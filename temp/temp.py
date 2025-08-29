import pandas as pd
from email.message import EmailMessage
import smtplib

# Carregar dados
df_data_base = pd.read_excel("impressoras.xlsx", sheet_name='base_de_dados')
df_filiais = pd.read_excel("impressoras.xlsx", sheet_name='filiais')

# Configurações
EMAIL_REMETENTE = "solupress@coplacana.com.br"
EMAIL_SENHA = "coplacana@1"
EMAIL_COPIA = "matheus.tano@coplacana.com.br;fabio.christofoletti@coplacana.com.br"
SMTP_SERVIDOR = "smtp-mail.outlook.com"
SMTP_PORTA = 587

# Preparar estrutura de filiais
filial_por_nome = {}
filiais_semEmail = []

for fil in df_filiais.to_dict(orient="records"):
    nome = fil['nome_filial'].lower()
    filial_por_nome[nome] = {
        "nome": nome,
        "id": fil['id_filial'],
        "email": fil['email_filial'],
        "impressoras": []
    }

# Associar impressoras às filiais
for imp in df_data_base.to_dict(orient="records"):
    nome_filial = str(imp['filial']).lower()
    ip = str(imp['ip'])
    if nome_filial in filial_por_nome and ip:
        impressora = {
            "num_serie": imp['num_serie'],
            "ip": imp['ip'],
            "nome": imp['impressora'],
            "leituraJunho": imp['junho'],
            "leituraJulho": imp['julho']
        }
        filial_por_nome[nome_filial]["impressoras"].append(impressora)

# Loop por filial
for chave, filial in filial_por_nome.items():
    filial_nome = filial['nome']
    filial_id = filial['id']
    impressoras = filial['impressoras']

    # Separar e-mails
    to_emails = [e.strip() for e in filial['email'].split(";") if e.strip()]
    cc_emails = [e.strip() for e in EMAIL_COPIA.split(";") if e.strip()]
    bcc_emails = []  # Adicione se quiser cópias ocultas
    
    # Criar tabela HTML
    df_impressoras = pd.DataFrame(impressoras)
    print("📊 Colunas originais:", df_impressoras.columns.tolist())
    print("📊 DataFrame vazio?", df_impressoras.empty)
    if df_impressoras.empty:
        print(f"⚠️ Filial '{filial_nome}' não possui impressoras. Pulando...\n")
        filiais_semEmail.append(filial_nome)
        continue
    

    df_impressoras = df_impressoras.rename(columns={
        'num_serie': 'Nº Série',
        'ip': 'IP',
        'nome': 'Modelo',
        'leituraJunho': 'Junho',
        'leituraJulho': 'Julho'
    })

    tabela_html = df_impressoras[['Modelo', 'Nº Série', 'IP', 'Junho', 'Julho']].to_html(index=False, border=1)

    corpo_html = f"""
    <style>
    table {{
        border-collapse: separate;
        border-spacing: 5px 5px;
        margin: 20px auto;
    }}
    th, td {{
        padding: 8px 12px;
        text-align: center;
    }}
    </style>
    <h3>Relatório da Filial {filial_nome.capitalize()}</h3>
    <p>Segue relatório de gastos das impressoras deste mês em comparação ao anterior!</p>
    {tabela_html}
    <p><strong>OBS:</strong> Diferenças grandes podem indicar troca ou manutenção das impressoras.</p>
    """

    # Criar mensagem
    msg = EmailMessage()
    msg['Subject'] = f"Relatório Impressoras - Filial {filial_nome.capitalize()}"
    msg['From'] = EMAIL_REMETENTE
    msg['To'] = ", ".join(to_emails)
    msg['Cc'] = ", ".join(cc_emails)
    msg.set_content(corpo_html, subtype='html')

    # Exibir preview
    print(f"📄 Conteúdo:\n{corpo_html}")
    print("="*60)
    print(f"📍 Filial: {filial_nome.capitalize()}")
    print(f"📧 Para: {', '.join(to_emails)}")
    print(f"📧 Cópia: {', '.join(cc_emails)}")
    print("="*60)

    # Decisão do usuário
    resposta = input("\nO que deseja fazer? \nEnviar - (1) \nPular - (2) \nSair - (0): ").strip()

    if resposta == '1':
        try:
            with smtplib.SMTP(SMTP_SERVIDOR, SMTP_PORTA) as smtp:
                smtp.starttls()
                smtp.login(EMAIL_REMETENTE, EMAIL_SENHA)
                all_recipients = to_emails + cc_emails + bcc_emails
                smtp.send_message(msg, to_addrs=all_recipients)
            print("✅ E-mail enviado com sucesso!\n")
        except Exception as e:
            print(f"❌ Erro ao enviar e-mail: {e}\n")
    elif resposta == '2':
        print("⏭️ E-mail ignorado. Pulando para a próxima filial...\n")
        filiais_semEmail.append(filial_nome)
        continue
    elif resposta == '0':
        print("🛑 Operação cancelada pelo usuário.\n")
        break
print("Filiais que não foram enviados o e-mail: ")
for filial in filiais_semEmail:
    print(f"* {filial}")