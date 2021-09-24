'''
 Números Inteiros e Criptografia RSA - Capítulo 8.
 Exercício 22 - Números totientes.
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


def existe_solucao_n_phi_n(k):
    if k != int(k): return False
    elif k == 1:    return True

    fatoracao_k = fatora(k)
    fator_max   = max(fatoracao_k.keys())

    k_ = k / (fator_max**(2 * fatoracao_k[fator_max] - 1) * (fator_max - 1))

    return existe_solucao_n_phi_n(k_)

def eh_totiente(k):
    return existe_solucao_n_phi_n(k)

def main():
    print('Obtendo todos k < 10^5 tais que existe solução para equação k = n x phi(n).')

    possiveis_ks = list(range(1, 100000))
    ks_validos   = list(
        filter( 
            lambda k: eh_totiente(k),
            possiveis_ks
        )
    )

    ks_validos_str = ", ".join(map(str, ks_validos))
    print('\nApós cálculos, temos:')
    print(f'\t{len(ks_validos)} valores que conferem a igualdade, esses são: {ks_validos_str}.')

if __name__ == "__main__":
    main()