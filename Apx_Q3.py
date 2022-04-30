#Questão A
def ehFloat(var):
    if var.isnumeric():
        var += '.0'
        return True, var

    f = var.split('.')

    if len(f) == 2 and f[0].isnumeric() and f[1].isnumeric():
        # print('float')
        return True, var
    else:
        return False, var


numero = input('Digite um Numero: ')
numero = ehFloat(numero)
if numero[0]:
    print(f'{numero[1]} e  float')
else:
    print(f'{numero[1]} Há mais do que um ".".')

#Questão B
try:
    f = float(input('digite um numero : '))
except:
    print('Você digitou errado, não é do tipo float há um caractere!')
else:
    print(f'é Tipo um float: {f}')

#Questão C

precoDolar = 5

dolar = float(input('coloque  a quantia em dolar:'))
real = precoDolar*dolar

print(f'O valor de USD {dolar}  com a taxa ' )
print(f'vai para {real:.3f} BRL')


#Questão D

precoDolar = 4.75

dolar = int(input('Em quantas vezes você quer comprar o produto?:'))

real = precoDolar*dolar

print(f'Quantidade de dolar {dolar}')
print(f' é  {real:.3f} BRL')
desconto = real-(real*.15)
print(f'com desconto de 5% {desconto:.3f} BRL')

#Questão E

precoDolar = 4.75

dolar = float(input('coloque a quantidade de dolar:'))
# dolar = 2

real = precoDolar * dolar

parcelas = int(input('quantidade de parcelas: '))
# parcelas = 2

if parcelas == 1:
    desconto = real - (real * .15)
    print('Você ganhou 15% de desconto, portanto')
    print(f'de {real:.2f} BRL {desconto:.3f} BRL')

else:
    print(f'Pagando as  parcelas  {parcelas} ')
    juros = real + (real * .15)
    print(f' e com 5% de juros ao mês, você pagará o total de :{juros:.2f}BRL ')
    juros = juros / parcelas
    print(f' e com 5% de juros ao mês, você pagará {juros:.2f} BRL  por mês')