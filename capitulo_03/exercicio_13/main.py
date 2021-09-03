'''
 Números Inteiros e Criptografia RSA - Capítulo 2.
 Exercício 12 - Frequência de tipos de primo.
'''
from sys   import stderr
from sympy import nextprime

SEPARADOR  = '-' * 65

VERDADEIRO = 'SIM'
FALSO      = 'NAO'
LIMITE     = 1e5

def primos_ate_n_com_crivo_eratostenes(n):
    if n < 3: return [2] if n == 2 else []

    crivo              = [i for i in range(3, n + 1, 2)]
    indice_primo_atual = 0
    while crivo[indice_primo_atual]**2 <= n:
        p     = crivo[indice_primo_atual]
        crivo = list(filter(lambda n: n == p or n % p != 0, crivo))
        indice_primo_atual += 1

    return [2] + crivo

def pi_1_e_pi_3(x):
    crivo = primos_ate_n_com_crivo_eratostenes(x)

    qtd_primos_1 = len(list(filter(lambda p: p % 4 == 1, crivo)))
    qtd_primos_3 = len(list(filter(lambda p: p % 4 == 3, crivo)))

    return qtd_primos_1, qtd_primos_3

def main():
    print('Buscando menor valor de x para o qual pi_1(x) > pi_3(x) ...\n')
    print('    x    |    pi_1(x)    |    pi_3(x)    |   pi_1(x) > pi_3(x)   ')

    x = 3
    pi_1_x, pi_3_x = pi_1_e_pi_3(x)
    while pi_1_x <= pi_3_x and x < LIMITE:
        print(f'{SEPARADOR}\n{x:^9}|{pi_1_x:^15}|{pi_3_x:^15}|{FALSO:^23}')
        x = nextprime(x)
        pi_1_x, pi_3_x = pi_1_e_pi_3(x)

    if x >= LIMITE:
        print('\nAssim, não existe x pertencente a [1, 10^5] tal que pi_1(x) > pi_3(x).\n')
    else:
        print(f'{SEPARADOR}\n{x:^9}|{pi_1_x:^15}|{pi_3_x:^15}|{VERDADEIRO:^23}')
        print(f'\nAssim, vemos que o menor valor de x para pi_1(x) > pi_3(x) é igual a {x}.\n')


if __name__ == '__main__':
    main()