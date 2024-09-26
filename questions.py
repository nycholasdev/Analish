def analisar_questões():

    print("\nTudo bem. Vamos fazer algumas perguntas para identificar qual pode ser o problema do peixe.")

    # Perguntas interativas com "sim" ou "não"

    esfregando = input("\nO peixe está se esfregando nos objetos do aquário? (sim/não): ").strip().lower()
            
    if esfregando == 'sim':
        fundo = input("\nO peixe está no fundo do aquário, tem barbatanas avermelhadas ou falta de apetite? (sim/não): ").strip().lower()
        
        if fundo == 'sim':
            return ("\nProvavelmente se trata de Costiose - "
                    "Tratamento: uso de parasiticidas aplicados no aquário a cada 48 horas. "
                    "É sempre recomendado buscar ajuda profissional e não medicar sem orientação.")
        
        respirar = input("\nO peixe está com dificuldade para respirar? (sim/não): ").strip().lower()
        
        if respirar == 'sim':
            return ("\nProvavelmente se trata de Ictício - "
                    "Tratamento: uso de parasiticidas aplicados no aquário a cada 48 horas. "
                    "É sempre recomendado buscar ajuda profissional e não medicar sem orientação")
        
        else:
            return "\nNão conseguimos identificar o problema, forneça mais informações"

    manchas_brancas = input("\nO peixe tem manchas brancas, "
                            "pontos brancos ou sinais brancos? (sim/não): ").strip().lower()

    if manchas_brancas == 'sim':
        nadando_lado = input("\nO peixe está nadando de lado ou de barriga para cima? (sim/não): ").strip().lower()
        
        if nadando_lado == 'sim':
            return ("\nProvavelmente se trata de doença da bexiga natatória - "
                    "Recomenda-se buscar ajuda profissional")
        
        algodao = input("\nO peixe tem manchas que parecem algodão ou pelos brancos? (sim/não): ").strip().lower()
        
        if algodao == 'sim':
            return ("\nProvavelmente se trata da doença do algodão - "
                    "Recomenda-se buscar um especialista para tratar com base na espécie do peixe "
                    "e fase da doença.")
        
        pele = input("\nO peixe apresenta deslocamento da pele, muco, ou pele aveludada/cor de ferrugem? (sim/não): ").strip().lower()
        
        if pele == 'sim':
            return ("\nProvavelmente se trata de Oodiniose (doença do veludo) - "
                    "Recomenda-se uso de parasiticida e procurar um especialista.")
        
        tecidos = input("\nO peixe apresenta apodrecimento dos tecidos? (sim/não): ").strip().lower()
        
        if tecidos == 'sim':
            return ("\nProvavelmente se trata de degeneração das nadadeiras. "
                    "Tratamento: uso de bactericidas. "
                    "É sempre recomendado buscar ajuda profissional e não medicar sem orientação.")
        
        fundo = input("\nO peixe está no fundo do aquário, tem barbatanas avermelhadas ou falta de apetite? (sim/não): ").strip().lower()
        
        if fundo == 'sim':
            return ("\nProvavelmente se trata de Costiose - "
                    "Tratamento: uso de parasiticidas aplicados no aquário a cada 48 horas. "
                    "É sempre recomendado buscar ajuda profissional e não medicar sem orientação.")
        
        respirar = input("\nO peixe está com dificuldade respiratória? (sim/não): ").strip().lower()
        
        if respirar == 'sim':
            return ("\nProvavelmente se trata de Ictício - "
                    "Tratamento: uso de parasiticidas aplicados no aquário a cada 48 horas. "
                    "É sempre recomendado buscar ajuda profissional e não medicar sem orientação")
        
        esfregando = input("\nO peixe está se esfregando nos objetos do aquário? (sim/não): ").strip().lower()
        
        if esfregando == 'sim':
            fundo = input("\nO peixe está no fundo do aquário, tem barbatanas avermelhadas ou falta de apetite? (sim/não): ").strip().lower()
            
            if fundo == 'sim':
                return ("\nProvavelmente se trata de Costiose - "
                        "Tratamento: uso de parasiticidas aplicados no aquário a cada 48 horas. "
                        "É sempre recomendado buscar ajuda profissional e não medicar sem orientação.")
            
            respirar = input("\nO peixe está com dificuldade respiratória? (sim/não): ").strip().lower()
            
            if respirar == 'sim':
                return ("\nProvavelmente se trata de Ictício - "
                        "Tratamento: uso de parasiticidas aplicados no aquário a cada 48 horas. "
                        "É sempre recomendado buscar ajuda profissional e não medicar sem orientação.")
            
            else:
                return "\nNão conseguimos identificar o problema, forneça mais informações"
        
        else:
            return "\nNão conseguimos identificar o problema, forneça mais informações"

    else:
        return "\nSem sintomas identificados."