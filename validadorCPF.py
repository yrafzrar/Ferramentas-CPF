import string
remocao_de_simbolos = str.maketrans("", "", string.punctuation)
cpf = input("Insira o CPF a ser válidado: \n>").translate(remocao_de_simbolos)
def invalido(x):
    print(f"CPF inválido, {x} digito não corresponde")

nove_digitos = cpf[:9]
if nove_digitos.isnumeric() and len(cpf) == 11:
    contagem10dig = 10
    contagem11dig = 11
    resultado_10digito = 0
    resultado_11digito = 0

    for dig in nove_digitos:
        resultado_10digito += contagem10dig *int(dig)
        contagem10dig -= 1

    resultado_10digito = (resultado_10digito*10)%11
    digito10 = 0 if resultado_10digito >= 9 else resultado_10digito
    dez_digitos = nove_digitos + str(digito10)
    
    if digito10 == int(cpf[9]):
        for dig in dez_digitos:
            resultado_11digito += contagem11dig*int(dig)
            contagem11dig -= 1

        resultado_11digito = (resultado_11digito*10)%11
        digito11 = 0 if resultado_11digito >= 9 else resultado_11digito
        if digito11 == int(cpf[10]):
            print("CPF válido")
        else:
            invalido(11)
    else:
        invalido(10)
else:
    print("Caracteres inválidos")