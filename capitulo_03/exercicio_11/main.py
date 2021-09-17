'''
 Números Inteiros e Criptografia RSA - Capítulo 3.
 Exercício 11 - Contagem de primos positivos.
'''
from math  import log

SEPARADOR = '-' * 57

A = [
    229168.50747390, -429449.7206839, 199330.41355048, 28226.22049280, 0, 0, -34712.81875914,
    0, 33820.10886195, -25379.82656589, 8386.14942934, -1360.44512548, 89.14545378
]

def S(x):
    sum_x = sum([a_x * (log(log(x)) ** k) for k, a_x in enumerate(A)])
    return (x / log(x)) * (1 + sum_x**(-1 / 4))

def primos_ate_n_com_crivo_eratostenes(n):
    if n < 3: return [2] if n == 2 else []

    crivo              = [i for i in range(3, n + 1, 2)]
    indice_primo_atual = 0
    while crivo[indice_primo_atual]**2 <= n:
        p     = crivo[indice_primo_atual]
        crivo = list(filter(lambda n: n == p or n % p != 0, crivo))
        indice_primo_atual += 1

    return [2] + crivo

def pi(x):
    return len(primos_ate_n_com_crivo_eratostenes(x))

def main():
    resultados = dict()
    for x in [11, 100, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]:
        pi_x = pi(x)
        S_t  = S(x)

        resultados[x] = [f'{abs(pi_x - S_t):.8f}', f'{abs(pi_x - (x / log(x))):.8f}']

    print('    x    |    pi(x) - S(x)    |   pi(x) - [x / log(x)]   ')
    for x, difs in resultados.items():
        print(f'{SEPARADOR}\n{x:^9}|{difs[0]:^20}|{difs[1]:^26}')

    print(
        '\nAssim, verificamos que A fórmula de aproximação obtida A partir do estudo\n' +
        'experimental é mais precisa que A aproximação dada por x / log(x).\n'
    )

if __name__ == '__main__':
    main()