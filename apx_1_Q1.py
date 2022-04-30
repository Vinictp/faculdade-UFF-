# Subprograma
def maior(numeros):
    valorMaior = max(numeros)
    return valorMaior

def menor(numeros):
    valorMenor = min(numeros)
    return valorMenor

def somatorio(numeros):
    soma = sum(numeros)
    return soma

def qtdNumeros(numeros):
    quantidade = len(numeros)
    return quantidade

# Programa Principal
soma = qtd = 0

entrada = input(f'Digite um número:')
while entrada != "":
    numeros = list(map(float, entrada.split()))
    maiorValor = maior(numeros)
    menorValor = menor(numeros)
    somaValor = somatorio(numeros)
    qtdValor = qtdNumeros(numeros)
    print("Menor:", menorValor, "Maior:", maiorValor)
    print("Quantidade de Números Lidos:", qtdValor)
    soma += somaValor
    qtd += qtdValor
    entrada = input()
print("Média dos Valores:", soma / qtd)