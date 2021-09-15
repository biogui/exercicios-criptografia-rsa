'''
 Números Inteiros e Criptografia RSA - Capítulo 5.
 Exercício 18 - Teorema de Fermat.
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

def main():
    print('Digite a e r para se obter todos primos p <= r | a^(p - 1) == 1 (mod p^2)')
    a, r = map(int, input('> ').split())

    crivo    = primos_ate_n_com_crivo_eratostenes(r)
    primos_p = filter(lambda p: pot_mod(a, p - 1, p*p) == 1, crivo)

    print('\nCalculando temos:')
    if primos_p:
        print(f'{a}^(p - 1) == 1 (mod p^2) ==> S = {{{", ".join(map(str, primos_p))}}}')
    else:
        print(f'{a}^(p - 1) == 1 (mod p^2) ==> S = {{}}')


if __name__ == "__main__":
    main()