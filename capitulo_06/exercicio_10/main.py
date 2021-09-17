'''
 Números Inteiros e Criptografia RSA - Capítulo 6.
 Exercício 10 - Teste de Miller.
'''
from sympy import primerange

def gera_impares_compostos(inicio, fim):
    impares = filter(lambda n: n % 2 == 1, range(inicio, fim + 1))
    primos  = list(primerange(inicio, fim + 1))

    return list(filter(lambda i: i not in primos, impares))

def pot_mod(a, k, n):
    if k == 0: return 1

    modulo_da_raiz = pot_mod(a, k // 2, n)
    modulo         = (modulo_da_raiz * modulo_da_raiz) % n

    return (modulo * a) % n if k % 2 == 1 else modulo

def teste_miller(n, b):
    k = 1
    q = (n - 1) / 2
    while q % 2 != 1:
        k += 1
        q /= 2

    r = pot_mod(b, q, n)
    if r == 1: return True

    i = 1
    r = r*r % n
    while i < k:
        if r == n - 1: return True
        r = r*r % n
        i += 1

    return False

def main():
    print('Digite b para se obter o menor pseudoprimo forte possível para a base b.')
    b = int(input('> '))

    impares_compostos = gera_impares_compostos(b, 10000)
    for i in impares_compostos:
        if teste_miller(i, b):
            print(f'\nO menor pseudoprimo forte para a base {b} é {i}.')
            break

if __name__ == "__main__":
    main()