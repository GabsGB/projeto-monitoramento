from services.scan_service import scan_filiais, scan_bd, attCont_mensais, scan_manual, attImpressora_filial

if __name__ == "__main__":
    
    #resp = input("Realizar somente o scan, atualizar contadores?  \n1 - Scan \n2 - Scan + Contadores \n:")

    #scan_filiais()
    impressoras = scan_bd()
    
    attCont_mensais(impressoras)
    
