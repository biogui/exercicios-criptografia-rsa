'''
 Números Inteiros e Criptografia RSA - Capítulo 5.
 Exercício 16.1 - Inverso modular .
'''
def pot_mod(a, k, n):
    if k == 0: return 1

    modulo_da_raiz = pot_mod(a, k // 2, n)
    modulo         = (modulo_da_raiz * modulo_da_raiz) % n

    return (modulo * a) % n if k % 2 == 1 else modulo

def inv_mod(a, p):
    return pot_mod(a, p - 2, p) if a % p else None

def main():
    print('Digite a e um primo p separados por espaço para o cálculo do inverso de p em Z_a')
    a, p = map(int, input('> ').split())

    inv_a_mod_p = inv_mod(a, p)

    if inv_a_mod_p:
        print(f'\nCalculando temos:\n {inv_a_mod_p} x {a} == 1 (mod {p})')
    else:
        print(f'\n{a} não tem inverso em Z_{p}')

if __name__ == '__main__':
    main()