#def imprimir_dados(nome, idade=24):
#    print('nome: {}, idade: {}' .format(nome, idade))

# imprimir_dados('James', 24)

#def somar_numeros(n1, n2):
 #   return n1 + n2

#resultado = somar_numeros(10, 20)

# print(resultado)

# def titulos_copa_mundo(pais, *args):
#    print('O país {}' .format(pais))
#    print('ganhou a copa do mundo nos seguintes anos:')
#    for titulo in args:
#        print(titulo)

# titulos_copa_mundo('Brasil', '1994', '2002', '2006')

salario = int(input('Qual o seu salário? '))
plano = int(input('Qual o valor do seu plano de saúde? '))

def inss(salario):
    inss = salario*0.09
    return inss

def vale_transporte(salario):
    vale_transporte = salario*0.03
    return vale_transporte

def plano_de_saude(salario):
    plano_de_saude = plano*0.15
    return plano_de_saude

def liquido(salario):
    liquido = salario - inss(salario) - vale_transporte(salario) - plano_de_saude(salario)
    return liquido

print('O seu salário líquido é:')
print(liquido(salario))





