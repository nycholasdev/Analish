def analisar_sintomas(sintomas):

    if ('nadando de lado' in sintomas or 
        'barriga para cima' in sintomas or 
        'barriga pra cima' in sintomas or
        'cabeça para baixo' in sintomas):
        return ("\nProvavelmente se trata de doença da bexiga natatória - "
                "Recomenda-se buscar ajuda profissional")

    elif ('no fundo do aquário' in sintomas or 
          'barbatanas avermelhadas' in sintomas or 
          'falta de apetite' in sintomas):
        return ("\nProvavelmente se trata de Costiose - "
                "Tratamento: uso de parasiticidas aplicados no aquário a cada 48 horas."
                "É sempre recomendado buscar ajuda profissional e não medicar sem orientação")

    elif 'dificuldade respiratória' in sintomas:
        return ("\nProvavelmente se trata de Ictício - "
                "Tratamento: uso de parasiticidas aplicados no aquário a cada 48 horas."
                "É sempre recomendado buscar ajuda profissional e não medicar sem orientação")

    elif ('deslocamento da pele' in sintomas or 
          'muco' in sintomas or 
          'pele aveludada' in sintomas or 
          'pele com cor de ferrugem' in sintomas):
        return ("\nProvavelmente se trata de Oodiniose (doença do veludo)."
                "Recomenda-se uso de parasiticida e procurar um especialista.")

    elif 'apodrecimento dos tecidos' in sintomas:
        return ("\nProvavelmente se trata de degeneração das nadadeiras. "
                "Recomenda-se uso de bactericidas e procurar um especialista.")

    elif ('algodão' in sintomas or 
          'pelos' in sintomas):
        return ("\nProvavelmente se trata de doença do algodão - "
                "Recomenda-se buscar um especialista para tratamento adequado com base na espécie do "
                "peixe e na fase em que a doença se encontra.")
    
    elif ('esfregando' in sintomas or 'roçando' in sintomas):
        fundo = input("\nO peixe está no fundo do aquário, tem barbatanas avermelhadas" 
                      " ou falta de apetite? (sim/não): ").strip().lower()
        
        if fundo == 'sim':
            return ("\nProvavelmente se trata de Costiose. "
                    "Tratamento: uso de parasiticidas aplicados no aquário a cada 48 horas. "
                    "É sempre recomendado buscar ajuda profissional e não medicar sem orientação.")
        
        respirar = input("\nO peixe está com dificuldade para respirar? (sim/não): ").strip().lower()
        
        if respirar == 'sim':
            return ("\nProvavelmente se trata de Ictício. "
                    "Tratamento: uso de parasiticidas aplicados no aquário a cada 48 horas. "
                    "É sempre recomendado buscar ajuda profissional e não medicar sem orientação")
        
        else:
            return "\nNão conseguimos identificar o problema, forneça mais informações"

    elif ('manchas brancas' in sintomas or 
          'pontos brancos' in sintomas or 
          'sinais brancos' in sintomas):
        nadando_lado = input("\nO peixe está nadando de lado ou de barriga para cima? (sim/não): ").strip().lower()
        
        if nadando_lado == 'sim':
            return ("\nProvavelmente se trata de doença da bexiga natatória - "
                    "Recomenda-se buscar ajuda profissional")
        
        algodao = input("\nO peixe tem manchas que parecem algodão ou pelos brancos? (sim/não): ").strip().lower()
        
        if algodao == 'sim':
            return ("\nProvavelmente se trata da doença do algodão - "
                    "Recomenda-se buscar um especialista")
        
        pele = input("\nO peixe apresenta deslocamento da pele, muco, ou pele aveludada/cor de ferrugem? (sim/não): ").strip().lower()
        
        if pele == 'sim':
            return ("\nProvavelmente se trata de Oodiniose (doença do veludo) - "
                    "Recomenda-se uso de parasiticida e procurar um especialista")
        
        tecidos = input("\nO peixe apresenta apodrecimento dos tecidos? (sim/não): ").strip().lower()
        
        if tecidos == 'sim':
            return ("\nProvavelmente se trata de degeneração das nadadeiras - "
                    "Tratamento: uso de bactericidas")
        
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
        
        esfregando = input("\nO peixe está se esfregando nos objetos do aquário? (sim/não): ").strip().lower()

        if esfregando == 'sim':
            fundo = input("\nO peixe está no fundo do aquário, tem barbatanas avermelhadas ou falta de apetite? (sim/não): ").strip().lower()
            
            if fundo == 'sim':
                return ("\nProvavelmente se trata de Costiose - "
                        "Tratamento: uso de parasiticidas aplicados no aquário a cada 48 horas "
                        "É sempre recomendado buscar ajuda profissional e não medicar sem orientação.")
            
            respirar = input("\nO peixe está com dificuldade para respirar? (sim/não): ").strip().lower()
            
            if respirar == 'sim':
                return ("\nProvavelmente se trata de Ictício - "
                        "Tratamento: uso de parasiticidas aplicados no aquário a cada 48 horas. "
                        "É sempre recomendado buscar ajuda profissional e não medicar sem orientação.")
            
            else:
                return "\nNão conseguimos identificar o problema, forneça mais informações"
        
        else:
            return "\nNão conseguimos identificar o problema, forneça mais informações"