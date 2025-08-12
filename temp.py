import pandas as pd
import numpy as np
from util.bd import insert_impressora

df = pd.read_excel("impressorasbd.xlsx")

'''
{
coluna: [{n_linha: valor,
    n_linha: valor,
    n_linha: valor,
    ...}]
}

Para acessar o valor da linha:
    df[coluna][n° da linha]

'''

ignorar = ["OFF","CONFIRMAR","MANU"]

for index in range(0, len(df["Modelo"])):
    # Se o IP ou o Modelo estiver na lista de ignorar, continue
    if df["IP"][index] in ignorar or df["Modelo"][index] in ignorar:
        continue
    
    impressora = {
        "num_serie": df["Série Fabricante"][index],
        "modelo": df["Modelo"][index],  
        "tipo": df["Laser/Térmica"][index],
        "ip": df["IP"][index] if df["IP"][index] != "USB" else None,
        "conexao": "USB" if df["IP"][index] == "USB" else "IP"
    }

    print(impressora)  # Verificar os dados
    insert_impressora(impressora)