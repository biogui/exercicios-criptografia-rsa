'''
 Números Inteiros e Criptografia RSA - Capítulo 5.
 Exercício 16.2 - Inverso modular .
'''
def pot_mod(a, k, n):
    if k == 0: return 1

    modulo_da_raiz = pot_mod(a, k // 2, n)
    modulo         = (modulo_da_raiz * modulo_da_raiz) % n

    return (modulo * a) % n if k % 2 == 1 else modulo

def inv_mod(a, p):
    return pot_mod(a, p - 2, p) if a % p else None

def main():
    print('Digite a, b e um primo p separados por espaço para o cálculo da solução de ax == b (mod p)')
    a, b, p = map(int, input('> ').split())

    inv_a_mod_p = inv_mod(a, p)

    print('\nCalculando temos:')
    if inv_a_mod_p:
        print(f'{a}x == {b} (mod {p}) ==> S = {{{b*inv_a_mod_p % p}}}')
    elif b % p == 0:
        print(f'{a}x == {b} (mod {p}) ==> S = {{x | x pertence a Z_{p}}}')
    else:
        print(f'{a}x == {b} (mod {p}) ==> S = {{}}')

if __name__ == '__main__':
    main()