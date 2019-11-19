lista = ('João', 'Ana', 'Paulo', 'Pedro', 'Aline', 'Helena', 'Kelly', 'Igor', 'Fernando', 'Isabel', 'Guilherme')
keyword = input('Qual inicial você gostaria de filtrar? ')

for word in lista:
    if word.startswith(keyword):
        print(word)
    else:
        print('Palavra não encontrada.')
        break
