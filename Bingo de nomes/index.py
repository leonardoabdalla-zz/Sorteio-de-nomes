import random
cadastro = input('Deseja cadastrar um nome ao sorteio?(S/N) ')
listaDeNomes = []
while cadastro == 'S':
    nome1 = input('Digite um nome: ')
    listaDeNomes.append(nome1)
    nome1 += 'a'
    cadastro = input('Deseja cadastrar outro nome?(S/N) ')
print(listaDeNomes)
sorteio = random.choice(listaDeNomes)
print('O nome sorteado foi {}'.format(sorteio))