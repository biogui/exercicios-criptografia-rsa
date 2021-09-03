'''
 Números Inteiros e Criptografia RSA - Capítulo 2.
 Exercício 12 - Frequência de tipos de primo.
'''
from tqdm import tqdm

SEPARADOR = '-' * 65

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
    qtd_primos_3 = len(crivo) - qtd_primos_1

    return qtd_primos_1, qtd_primos_3

def main():
    print('Calculando as razões pi_1(x) / pi_3(x) para diversos x variando em N\n')
    resultados = dict()
    for x in tqdm(range(100, 100000, 100), ncols=90, desc=''):
        resultados[x] = pi_1_e_pi_3(x)

    print('    x    |    pi_1(x)    |    pi_3(x)    |    pi_1(x)/pi_3(x)    ')
    for x, pis in resultados.items():
        pi_1_x, pi_3_x = pis
        print(f'{SEPARADOR}\n{x:^9}|{pi_1_x:^15}|{pi_3_x:^15}|{pi_1_x/pi_3_x:^23}')

    print('\nAssim, vemos que a razão tende a 1 quando x tende ao infinito.\n')

if __name__ == '__main__':
    main()