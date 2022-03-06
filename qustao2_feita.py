('====== QUESTÃO 2 -  #######Vinicius REis de SOuza)
qtdTestes = int(input('Informe a quantidade de testes:'))
qtdValoresTeste = int(input('Informe a quantidade de valores de cada teste:'))
valorMinino = float(input('Informe o valor mínimo do intervalo:'))
valorMaximo = float(input('informe o valor máximo do intervalo:'))

lista = []
con_Min = 0
con_Max = 0
con_intervalo = 0
soma = 0

for c in range(0, qtdTestes):
    print(f'Teste {c}')
    for p in range(qtdValoresTeste):
        valor = float(input(f'Digite um valor na posição {p}: '))
        lista.append(valor)
        if valor < valorMinino:
            con_Min += 1
        elif valor > valorMinino and valor < valorMaximo:
            con_intervalo += 1
            soma += valor
        elif valor > valorMaximo:
             con_Max += 1
    print(f'Você digitou os valores {lista}')
    print(f'Quantidade de valores mínimos : {cont_Min}')
    print(f'Quantidade de valores máximos:  {cont_Max}')
    print(f'Quantidade de valores dentro do intervalo:  {cont_intervalo}')
    print(f'A soma dos valores dentro do intervalo é: {soma}')
    con_Min = 0
    con_Max = 0
    con_intervalo = 0
    soma = 0
qtdTestes -= 1




