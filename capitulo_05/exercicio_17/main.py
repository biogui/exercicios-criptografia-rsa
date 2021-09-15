'''
 Números Inteiros e Criptografia RSA - Capítulo 5.
 Exercício 17 - Equação de congruência.
'''
def pot_mod(a, k, n):
    if k == 0: return 1

    modulo_da_raiz = pot_mod(a, k // 2, n)
    modulo         = (modulo_da_raiz * modulo_da_raiz) % n

    return (modulo * a) % n if k % 2 == 1 else modulo

def main():
    print('Digite um primo p da forma 4k + 3 e a separados por espaço para o cálculo da solução de x^2 == a (mod p)')
    p, a = map(int, input('> ').split())

    k = (p - 3) // 4
    b = pot_mod(a, k + 1, p)

    print('\nCalculando temos:')
    if b*b % p == a:
        print(f'x^2 == {a} (mod {p}) ==> S = {{{-b}, {b}}}')
    else:
        print(f'x^2 == {a} (mod {p}) ==> S = {{}}')

if __name__ == '__main__':
    main()