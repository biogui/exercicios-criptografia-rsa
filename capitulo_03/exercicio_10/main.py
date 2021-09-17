'''
 Números Inteiros e Criptografia RSA - Capítulo 3.
 Exercício 10 - Crivo de Eratóstenes.
'''
def primos_ate_n_com_crivo_eratostenes(n):
    if n < 3: return [2] if n == 2 else []

    crivo              = [i for i in range(3, n + 1, 2)]
    indice_primo_atual = 0
    while crivo[indice_primo_atual]**2 <= n:
        p     = crivo[indice_primo_atual]
        crivo = list(filter(lambda n: n == p or n % p != 0, crivo))
        indice_primo_atual += 1

    return [2] + crivo

def main():
    print('Digite a (> 0), b e c separados por espaço para o polimônio f(x) = ax² + bx + c')
    a, b, c = map(int, input('> ').split())

    f_x = [a * x**2 + b * x + c for x in range(101)]

    f_x[0], f_x[100] = abs(f_x[0]), abs(f_x[100])

    n = max(f_x[0], f_x[100])
    crivo = primos_ate_n_com_crivo_eratostenes(n)

    resultados = sorted(list(map(f_x.index, filter(lambda p: p in f_x, crivo))))
    print(f'\nf(x) é primo para x ∈ {{{", ".join(list(map(str, resultados)))}}}')

if __name__ == '__main__':
    main()