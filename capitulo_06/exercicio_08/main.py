'''
 Números Inteiros e Criptografia RSA - Capítulo 6.
 Exercício 8 - Teste de Fermat.
'''
from sympy import primerange

def fatora(n):
    possiveis_fatores = primerange(2, n + 1)

    fatoracao = dict()
    for fator in possiveis_fatores:
        if n % fator == 0:
            fatoracao[fator] = 0
            while n % fator == 0:
                fatoracao[fator] += 1
                n /= fator

    return fatoracao

def impares_compostos_ate_n_com_crivo_eratostenes(n):
    if n < 3: return [2] if n == 2 else []

    crivo              = [i for i in range(3, n + 1, 2)]
    indice_primo_atual = 0
    while crivo[indice_primo_atual]**2 <= n:
        p     = crivo[indice_primo_atual]
        crivo = list(filter(lambda n: n == p or n % p != 0, crivo))
        indice_primo_atual += 1

    impares = [i for i in range(3, n + 1, 2)]

    return list(filter(lambda i: i not in crivo, impares))

def pot_mod(a, k, n):
    if k == 0: return 1

    modulo_da_raiz = pot_mod(a, k // 2, n)
    modulo         = (modulo_da_raiz * modulo_da_raiz) % n

    return (modulo * a) % n if k % 2 == 1 else modulo

def teste_fermat(n, b):
    return (pot_mod(b, n - 1, n) == 1)

def teste_korselt(n):
    fatoracao = fatora(n)

    for p in fatoracao.keys():
        if n % (p*p) == 0:         return False
        if (n - 1) % (p - 1) != 0: return False

    return True

def main():
    print('Digite r para se obter todos pseudoprimos p < r para as base 2 e 3.')
    r = int(input('> '))

    impares_compostos            = impares_compostos_ate_n_com_crivo_eratostenes(r)
    pseudoprimos_para_base_2_e_3 = list(
        filter(
            lambda i: teste_fermat(i, 2) and teste_fermat(i, 3),
            impares_compostos
        )
    )
    nums_de_carmichael           = list(
        filter(
            lambda p: teste_korselt(p),
            pseudoprimos_para_base_2_e_3
        )
    )

    pseudoprimos_str    = ", ".join(map(str, pseudoprimos_para_base_2_e_3))
    nums_carmichael_str = ", ".join(map(str, nums_de_carmichael))
    print('\nApós cálculos, temos:')
    print(f'\t{len(pseudoprimos_para_base_2_e_3)} pseudoprimos < r para base 2 e 3: {pseudoprimos_str}.')
    print(f'\tDesses, temos {len(nums_de_carmichael)} números de carmichael, esses são: {nums_carmichael_str}.')

if __name__ == "__main__":
    main()