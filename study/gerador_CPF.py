
import random

def gerador_de_CPF():

    
    nove_digito_cpf = ''
    for i in range(9):
        nove_digito_cpf += str(random.randint(0,9))

    digt_verf = 0
    multiplicador = 10

    for number in nove_digito_cpf:
        digt_verf += int(number)*multiplicador 
        multiplicador -= 1
    
    digt_verf = (digt_verf*10)%11

    if digt_verf > 9:
        digt_verf = 0
     
    nove_digito_cpf += str(digt_verf)

    multiplicador = 11
    digt_verf = 0
    
    for number in nove_digito_cpf:
        digt_verf += int(number)*multiplicador 
        multiplicador -= 1

    digt_verf = (digt_verf*10)%11

    if digt_verf > 9:
        digt_verf = 0
    
    nove_digito_cpf += str(digt_verf)

    print(nove_digito_cpf)

gerador_de_CPF()