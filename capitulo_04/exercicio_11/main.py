'''
 Números Inteiros e Criptografia RSA - Capítulo 4.
 Exercício 11 - Exponenciação rápida.
'''
def pot_mod(a, k, n):
    if k == 0: return 1

    modulo_da_raiz = pot_mod(a, k // 2, n)
    modulo         = (modulo_da_raiz * modulo_da_raiz) % n

    return (modulo * a) % n if k % 2 == 1 else modulo

def main():
    print('Digite a, k e n separados por espaço para o cálculo de a^k (mod n)')
    a, k, n = map(int, input('> ').split())

    print(f'\nCalculando temos:\n {a}^{k} == {pot_mod(a, k, n)} (mod {n})')

if __name__ == '__main__':
    main()