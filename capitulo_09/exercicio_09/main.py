'''
 Números Inteiros e Criptografia RSA - Capítulo 9.
 Exercício 9 - Método de Fermat para Números de Mersenne.
'''
from sympy import primerange, isprime
from tqdm  import tqdm

MODO = 1

PRIMO_MINIMO = 2
PRIMO_MAXIMO = 257
PRIMOS       = list(primerange(PRIMO_MINIMO, PRIMO_MAXIMO + 1))

M = lambda p: 2**p - 1

def pot_mod(a, k, n):
    if k == 0: return 1

    modulo_da_raiz = pot_mod(a, k // 2, n)
    modulo         = (modulo_da_raiz * modulo_da_raiz) % n

    return (modulo * a) % n if k % 2 == 1 else modulo

def metodo_de_fermat(p):
    numero_de_mersenne = M(p)
    descricao  = f'p = {p:3d}'

    limite_r = (2**(p // 2) - 1) // (2 * p)

    q = 2 * p + 1
    for r in tqdm(range(limite_r), ncols=90, desc=descricao):
        if pot_mod(2, p, q) == 1: return q

        q += p

    return numero_de_mersenne

def main():
    print('Obtendo os todos os valores para os quais 2 <= p <= 257 primo culmina em um número de Mersenne M(p), também primo.')

    primos_que_geram_Mp_primo = list(
        filter(
            lambda p: metodo_de_fermat(p) == M(p) if MODO == 0 else lambda p: isprime(M(p)), # *(1)
            PRIMOS
        )
    )

    primos_que_geram_Mp_primo_str = ", ".join(map(str, primos_que_geram_Mp_primo))
    print('\nApós cálculos, temos:')
    print(f'\t{len(primos_que_geram_Mp_primo)} primos que geram M(p) primo obtidos, esses são: {primos_que_geram_Mp_primo_str}.')

if __name__ == "__main__":
    main()

# *(1)
#  O método é muito lento para números de Mersenne gerados por primos p >= 89,
# devido a quantidade gigantesca de r's para se testar, trocando a constante
# MODO para 0 é possível ver o quão demorado é o processo.