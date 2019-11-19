#lista_nomes = ['James', 'Ana', 'Dauto', 'Felipe']

#for nome in lista_nomes:
#    print(nome)

#print("Todos os nomes foram impressos!")

# i = 0

# while i < len(lista_nomes):
#    print(lista_nomes[i])
#    i += 1


########################################################

#lista_escadinha = ['#', '##', '###', '####', '#####']

#for item in lista_escadinha:
#    print(item)

########################################################
escadinha = ''
caractere = input('Digite um caractere: ')
numeroEscadas = int(input('Digite o número de escadinhas desejadas: '))

for item in range(0, numeroEscadas):
    escadinha += caractere
    print(escadinha)


