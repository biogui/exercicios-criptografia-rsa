'''
 Números Inteiros e Criptografia RSA - Capítulo 11.
 Exercício 8 - Criptografia de Rabin.
'''
from math import sqrt

STR_NULA = 'BLOCO INVÁLIDO'

N = 20490901
A = [18504501, 18109884]

pre_codificacao = {
    10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F', 16: 'G', 17: 'H', 18: 'I',
    19: 'J', 20: 'K', 21: 'L', 22: 'M', 23: 'N', 24: 'O', 25: 'P', 26: 'Q', 27: 'R',
    28: 'S', 29: 'T', 30: 'U', 31: 'V', 32: 'W', 33: 'X', 34: 'Y', 35: 'Z', 99: ' '
}

def fatores_por_fermat(n):
    if n % 2 == 0: return (2, n//2)

    x = int(sqrt(n))

    if x**2 == n: return (x, x)

    def nova_tentativa(x):
        x += 1
        if x == (n + 1) / 2: return (1, n)

        y = sqrt(x**2 - n)
        y_int = int(y)

        return (x + y_int, x - y_int) if y == y_int else nova_tentativa(x)

    return nova_tentativa(x)

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

def pos_decodificacao(b):
    bloco_str = str(b)
    numeros   = [int(bloco_str[i: i + 2]) for i in range(0, len(bloco_str), 2)]

    try:
        texto = ''.join(map(lambda n: pre_codificacao[n], numeros))
    except KeyError:
        return STR_NULA

    return texto

def main():
    print('Decodificando a mensagem 18504501 - 18109888 para a Criptografia de Rabin com n = 20490901.')

    print('Executando temos ...')
    p, q = fatores_por_fermat(N)
    print(f'(1) Fatorando, obtemos n = {p} x {q}.')

    print(f'(2) Decodificando, via soluções de x^2 = a (mod n).')
    decodificao = list()
    for bloco in A:
        k_p = (p - 3) // 4
        s_p = pot_mod(bloco, k_p + 1, p)

        k_q = (q - 3) // 4
        s_q = pot_mod(bloco, k_q + 1, q)

        _, alpha, beta = mdc_extendido(p, q)

        s = (s_p * beta * q + s_q * alpha * p) % (p * q)
        u = (p**(q - 1) - q**(p - 1))

        solucoes      = [s, N - s, u * s % N, u * -s % N]
        decodificoes = list(map(pos_decodificacao, solucoes))

        print(f'\t• bloco = {bloco}:')
        print(f'\t {solucoes[0]:<8} -> {decodificoes[0]}.')
        print(f'\t {solucoes[1]:<8} -> {decodificoes[1]}.')
        print(f'\t {solucoes[2]:<8} -> {decodificoes[2]}.')
        print(f'\t {solucoes[3]:<8} -> {decodificoes[3]}.')

        decodificao += list(
            filter(
                lambda s: s != STR_NULA,
                decodificoes
            )
        )

    print(f'\nDessa forma obtemos \"{"".join(decodificao)}\" como a mensagem original.')

if __name__ == "__main__":
    main()