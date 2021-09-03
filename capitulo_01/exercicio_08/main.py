'''
 Números Inteiros e Criptografia RSA - Capítulo 1.
 Exercício 8 - Algoritmo de Euclides Estendido.
'''

BARRA_GRAFICA = '-' * 50

# Realiza o algoritmo de euclides
def mdc(a, b):
    return a if b == 0 else mdc(b, a % b)

# Realiza algoritmo de euclides estendido
def mdc_extendido(a, b, u, v, u_, v_): 
    if b == 0:
        return a, u, v
    else:
        q  = a // b
        ut = u - q * u_
        vt = v - q * v_
        return mdc_extendido(b, a % b, u_, v_, ut, vt)

def main():
    # Recebe como entrada a e b, da equação ax + by = mdc(a, b)
    print('Digite a, b e c separados por espaço para a equação ax + by = c\n> ')
    a, b, c = map(int, input().split())

    d = mdc(a, b)

    # Confere se d divide c e printa a solução caso essa seja vazia
    if c % d != 0:
        print(f'\n{BARRA_GRAFICA}\n{a}x + {b}y = {c} => S = {{}}\n')
        exit()

    # Seta as variáveis de a', b' e c' para o cálculo final com mdc estendido
    a_, b_, c_ = a / d, b / d, c / d

    # Calcula alpha e beta por euclides estendido
    _, alpha, beta = mdc_extendido(a_, b_)

    # Seta a solução e printa o resultado
    x, y = c_ * alpha, c_ * beta
    print(f'\n{BARRA_GRAFICA}\n{a}x + {b}y = {c} => S = {{{x:.0f}, {y:.0f}}}\n')

if __name__ == '__main__':
    main()