multi = int( input('Informe a quantidade de nomes completos a serem inseridos :'))
def nome (nome1):
    nome = nome1.split()
    return nome
while multi != 0:
    nome2 = str(input('Digite seu nome Aqui:'))
    listanome = nome (nome2)
    print(f'{listanome[0]} {listanome[-1]}')
    multi -= 1