# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

def questionario():

    count = 0

    for questoes in perguntas:
        print(questoes['Pergunta'])

        for opcoes in range(len(questoes['Opções'])):
            print(f'{opcoes}) {questoes['Opções'][opcoes]}')
        
        resposta = input('Digite a alternativa correta: ')

        if questoes['Opções'][int(resposta)] != questoes['Resposta']:
            print('Alternativa INCORRETA')
            continue
        
        count += 1
        print('Alternativa CORRETA')
    
    return print(f'voce acertou {count} questoes')
 

questionario()