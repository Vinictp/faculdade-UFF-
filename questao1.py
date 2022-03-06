#questão 1 de Python Vinicius Reis de Souza  221071023##


while True:
    print('\n')
    valor = int(input("Digite o Valor a ser Trocado : "))
    cedulas= 0 
    notadecem = 100
    valorentregue = valor
    moeda = 1
   
    while True:
 
        if notadecem <= valorentregue:
            cedulas += 1
            valorentregue -=notadecem
                 
        else:
            if cedulas >1:
                print (f'{cedulas} notas de {notadecem} reais')
            if cedulas ==1:
                print (f'{cedulas} nota de {notadecem} reais')
            if   notadecem ==100:
                 notadecem = 50
            elif notadecem == 50:
                 notadecem = 20
            elif notadecem == 20:
                 notadecem = 10
            elif notadecem == 10:
                 notadecem = 5     
            elif notadecem == 5:
                 notadecem = 2
            elif notadecem == 2:
                 moeda = 1 
                 print (f'{moeda} moeda de  um real')
                 break
            cedulas =0
            if valorentregue==0:
                break 
            
