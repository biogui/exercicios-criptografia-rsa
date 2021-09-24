'''
 Números Inteiros e Criptografia RSA - Capítulo 9.
 Exercício 10 - Método para Números de Fermat.
'''
F = lambda k: 2**(2**k) + 1

def metodo(k, n):
    q = k * 2**n + 1

    m      = 5
    modulo = 2**(2**m)
    while m < n:
        if modulo == q - 1: return m

        modulo = (modulo * modulo) % q
        m += 1

    return None

def main():
    print('Obtendo os números de Fermat divisíveis por 37 x 2^16 + 1 e 11131 x 2^12 + 1.')

    m_1 = metodo(37, 16)
    m_2 = metodo(11131, 12)

    print('\nApós cálculos, temos:')    
    print(f'\t37 x 2^16 + 1 | F({m_1}) .')
    print(f'\t11131 x 2^12 + 1 | F({m_2}) .')

if __name__ == "__main__":
    main()