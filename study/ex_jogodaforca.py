"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""

def findWord(palavra_secreta):
    acertos = ''
    count = 0
    while 1:
    
        novatentativa = input('Digite uma letra: ')
        palavra = ''

        if len(novatentativa) < 2:
            count += 1
            if novatentativa in palavra_secreta:
                acertos += novatentativa
            
            for letra in palavra_secreta:
            
                if letra in acertos:
                    palavra += letra
                else:
                    palavra += '*'
            
            if palavra == palavra_secreta:
                return print(f'parabens voce dercobriu a palavra: {palavra_secreta} em {count} tentativas')
                

            print(palavra)
            print('tentativas: ', count)

        else: 
            print('Digite apenas uma letra')

findWord('banana')