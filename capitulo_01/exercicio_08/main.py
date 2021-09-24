'''
 Números Inteiros e Criptografia RSA - Capítulo 1.
 Exercício 8 - Algoritmo de Euclides Estendido.
'''

BARRA_GRAFICA = '-' * 50

def mdc(a, b):
    return a if b == 0 else mdc(b, a % b)

def mdc_extendido(a, b, u=1, v=0, u_=0, v_=1):
    if b == 0:
        return a, u, v
    else:
        q  = a // b
        ut = u - q * u_
        vt = v - q * v_
        return mdc_extendido(b, a % b, u_, v_, ut, vt)

def main():
    print('Digite a, b e c separados por espaço para a equação ax + by = c\n> ')
    a, b, c = map(int, input().split())

    d = mdc(a, b)

    if c % d != 0:
        print(f'\n{BARRA_GRAFICA}\n{a}x + {b}y = {c} => S = {{}}\n')
        exit()

    a_, b_, c_ = a / d, b / d, c / d
    _, alpha, beta = mdc_extendido(a_, b_)
    x, y = c_ * alpha, c_ * beta
    print(f'\n{BARRA_GRAFICA}\n{a}x + {b}y = {c} => S = {{{x:.0f}, {y:.0f}}}\n')

if __name__ == '__main__':
    main()