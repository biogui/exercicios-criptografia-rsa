'''
 Números Inteiros e Criptografia RSA - Capítulo 2.
 Exercício 12 - Fatoração por Algoritmo de Fermat.
'''
from math import sqrt

def fatores_por_fermat(n):
    if n % 2 == 0: return (2, n//2)

    x = int(sqrt(n))

    if x**2 == n: return (x, x)

    def nova_tentativa(x):
        x += 1
        if x == (n + 1) / 2: return (1, n)

        y = sqrt(x**2 - n)
        y_int = int(y)

        return (x + y_int, x - y_int) if y == y_int else nova_tentativa(x)

    return nova_tentativa(x)

def main():
    print('Digite um inteiro n menor que 2^32, para obter dois fatores pela fatoração de Fermat:')
    n = int(input('> '))

    fator_1, fator_2 = fatores_por_fermat(n)
    resultado = f'n = {n} é primo' if fator_1 == 1 else f'n = {n} = {fator_1} * {fator_2}'

    print(f'\nO resultado após a fatoração foi: {resultado}')

if __name__ == '__main__':
    main()