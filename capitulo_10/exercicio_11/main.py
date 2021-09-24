'''
 Números Inteiros e Criptografia RSA - Capítulo 10.
 Exercício 11 - Teste de Primalidade.
'''
from sympy import prevprime
import datetime

F = lambda k: 2**(2**k) + 1

def fatorial_mod(f, n):
    modulo = 1
    for fator_atual in range(2, f + 1):
        modulo = (modulo * fator_atual) % n

    return modulo

def teste_de_wilson(n):
    return (fatorial_mod(n - 1, n) == n - 1)

def main():
    print('Calculando o tempo de execução do teste de Wilson para o maiores primos menores que 10^k, com k <= 6.')

    print('Executando temos ...')
    for k in range(1, 6):
        primo  = prevprime(10**k)
        inicio = datetime.datetime.now()

        resultado = 'primo' if teste_de_wilson(primo) else 'composto'
        duracao   = datetime.datetime.now() - inicio

        print(f'\tn = {primo} < 10^{k} é {resultado}, e o teste é executado em {duracao.total_seconds() * 1000:.2f} ms.')

    print('Podemos aproximar o tempo de execução para T = 10^{k - 5} ms, portanto para um k = 100, o programa seria executado em um tempo próximo de 10^92 segundos.')

if __name__ == "__main__":
    main()