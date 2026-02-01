import random
import time
import os
while True:
    quantidade = input("Quantos CPF's gerar?\n>")
    if quantidade.isdigit():
        for _ in range(int(quantidade)):
            cpf = ''
            for i in range(9):
                cpf += str(random.randint(0,9))

            contagem10dig = 10
            contagem11dig = 11
            resultado_10digito = 0
            resultado_11digito = 0

            for dig in cpf:
                resultado_10digito += contagem10dig *int(dig)
                contagem10dig -= 1

            resultado_10digito = (resultado_10digito*10)%11
            digito10 = 0 if resultado_10digito >= 9 else resultado_10digito
            cpf += str(digito10)
            
            
            for dig in cpf:
                resultado_11digito += contagem11dig*int(dig)
                contagem11dig -= 1

            resultado_11digito = (resultado_11digito*10)%11
            digito11 = 0 if resultado_11digito >= 9 else resultado_11digito
            cpf += str(digito11)
                
        print("Caracter inválido")
    escolha = input("Deseja gerar novamente?\n[s]im [n]ão\n>")
    if escolha.lower() == 's':
        os.system('cls' if os.name == 'nt' else 'clear')
        continue
    else:
        print("Encerrando",end="", flush=True)
        for _ in range(3):
            time.sleep(0.5)
            print(".",end="", flush=True)
        exit()