'''
 Números Inteiros e Criptografia RSA - Capítulo 7.
 Exercício 10 - Sistema de congruência.
'''

def mdc_extendido(a, b, u=1, v=0, u_=0, v_=1):
    if b == 0:
        return a, u, v
    else:
        q  = a // b
        ut = u - q * u_
        vt = v - q * v_
        return mdc_extendido(b, a % b, u_, v_, ut, vt)

def pot_mod(a, k, n):
    if k == 0: return 1

    modulo_da_raiz = pot_mod(a, k // 2, n)
    modulo         = (modulo_da_raiz * modulo_da_raiz) % n

    return (modulo * a) % n if k % 2 == 1 else modulo

def main():
    print('Digite dois primos p e q da forma 4k + 3 e a separados por espaço para o cálculo da solução de x^2 == a (mod p * q)')
    p, q, a = map(int, input('> ').split())

    k_p = (p - 3) // 4
    b_p = pot_mod(a, k_p + 1, p)
    s_p = b_p if b_p*b_p % p == a % p else None

    k_q = (q - 3) // 4
    b_q = pot_mod(a, k_q + 1, q)
    s_q = b_q if b_q*b_q % q == a % q else None

    if s_p and s_q:
        _, alpha, beta = mdc_extendido(p, q)

        s = (s_p * beta * q + s_q * alpha * p) % (p * q)
        print(f'\nx^2 == {a} (mod {p*q}) ==> S = {{{s}}}')
    else:
        print(f'\nx^2 == {a} (mod {p*q}) ==> S = {{}}')

if __name__ == '__main__':
    main()