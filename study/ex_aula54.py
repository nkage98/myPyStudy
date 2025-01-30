"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""


def ex1():
    try:
        numero = int(input('Digite um numero inteiro: '))

        if numero%2:
            return print('O numero que digitou é impar.')
        
        return print('O numero que digitou é par.')

    except:
        return print('O numero que digitou não é inteiro')
#ex1()

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

def saudacao():
    try: 
        hora = int(input('digite as horas: '))
        if hora < 24:    
            if hora < 12:
                return print('bom dia')
            elif hora < 17:
                return print ('boa tarde')
            return print('boa noite')        
        return print('A hora que digitou é invalido')
    except:
        print('A hora que digitou é invalido')

#saudacao()


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 

"está muito simples não farei kkk"

"""

