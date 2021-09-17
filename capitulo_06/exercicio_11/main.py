'''
 Números Inteiros e Criptografia RSA - Capítulo 6.
 Exercício 11 - Pseudoprimos p^2 para base 2.
'''
def primos_ate_n_com_crivo_eratostenes(n):
    if n < 3: return [2] if n == 2 else []

    crivo              = [i for i in range(3, n + 1, 2)]
    indice_primo_atual = 0
    while crivo[indice_primo_atual]**2 <= n:
        p     = crivo[indice_primo_atual]
        crivo = list(filter(lambda n: n == p or n % p != 0, crivo))
        indice_primo_atual += 1

    return [2] + crivo

def pot_mod(a, k, n):
    if k == 0: return 1

    modulo_da_raiz = pot_mod(a, k // 2, n)
    modulo         = (modulo_da_raiz * modulo_da_raiz) % n

    return (modulo * a) % n if k % 2 == 1 else modulo

def teste_fermat(n, b):
    return (pot_mod(b, n - 1, n) == 1)

def main():
    print('Digite r para se obter todos os pseudoprimos para base 2 do tipo p^2, onde p é um primo <= r.')
    r = int(input('> '))

    primos                   = primos_ate_n_com_crivo_eratostenes(r)
    possiveis_pseudoprimos   = list(map(lambda p: p * p, primos))
    pseudoprimos_para_base_2 = list(
        filter(
            lambda i: teste_fermat(i, 2),
            possiveis_pseudoprimos
        )
    )

    pseudoprimos_str    = ", ".join(map(str, pseudoprimos_para_base_2))
    print('\nApós cálculos, temos:')
    print(f'\t{len(pseudoprimos_para_base_2)} pseudoprimos obtidos para base 2: {pseudoprimos_str}.')

if __name__ == "__main__":
    main()