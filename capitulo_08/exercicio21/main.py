'''
 Números Inteiros e Criptografia RSA - Capítulo 8.
 Exercício 21 - Cálculo de Ordem.
'''
from sympy import prevprime, primerange, primepi

PRIMO_MAXIMO = prevprime(100000)
PRIMOS       = list(primerange(2, PRIMO_MAXIMO + 1))

def fatora(n):
    fatoracao = dict()
    for fator in PRIMOS[:primepi(n)]:
        if n % fator == 0:
            fatoracao[fator] = 0
            while n % fator == 0:
                fatoracao[fator] += 1
                n /= fator

    return fatoracao

def phi(n):
    fatoracao = fatora(n)

    phi_n = 1
    for p, k in fatoracao.items():
        phi_n *= p**(k - 1) * (p - 1)

    return phi_n

def main():
    print('Obtendo todos k < 10^5 tais que phi(k) = phi(k + 1).')

    possiveis_ks = list(range(1, 100001))
    phis         = {k: phi(k) for k in possiveis_ks}
    ks_validos   = list(
        filter( 
            lambda k: (phis[k] == phis[k + 1]),
            possiveis_ks[:-1]
        )
    )

    ks_validos_str = ", ".join(map(str, ks_validos))
    print('\nApós cálculos, temos:')
    print(f'\t{len(ks_validos)} valores que conferem a igualdade, esses são: {ks_validos_str}.')

if __name__ == "__main__":
    main()