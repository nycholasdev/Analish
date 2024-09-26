from diagnosis import analisar_sintomas
from questions import analisar_questões

def diagnosticar_peixe():
    resposta = input("\n Você consegue descrever os sintomas do peixe? (sim/não): ").lower()

    if resposta == 'sim':
        sintomas = input("\nDescreva os sintomas observados no peixe: ").lower()

        # Fluxograma 1

        resultado = analisar_sintomas(sintomas)
        return resultado
    
    else:
        # Fluxograma 2 - Perguntas interativas com "sim" ou "não"
        resultado = analisar_questões()
        return resultado

# Executar o diagnóstico
diagnostico = diagnosticar_peixe()
print(diagnostico)
