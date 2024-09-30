from diagnosis import analisar_sintomas
from questions import analisar_questões

def diagnosticar_peixe():
    resposta = input("\n Você consegue descrever os sintomas do peixe? (sim/não): ").lower()

    if resposta == 'sim':
        sintomas = input("\nDescreva os sintomas observados no peixe: ").lower()

        resultado = analisar_sintomas(sintomas)
        return resultado
    
    else:
        resultado = analisar_questões()
        return resultado

diagnostico = diagnosticar_peixe()
print(diagnostico)
