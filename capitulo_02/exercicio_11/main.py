'''
 Números Inteiros e Criptografia RSA - Capítulo 2.
 Exercício 11 - Números altamente compostos.
'''
from math  import sqrt
from sympy import primerange

def fatora(n):
    possiveis_fatores = primerange(2, n + 1)

    fatoracao = dict()
    for fator in possiveis_fatores:
        if n % fator == 0:
            fatoracao[fator] = 0
            while n % fator == 0:
                fatoracao[fator] += 1
                n /= fator

    return fatoracao

def conta_divisores(n):
    raiz_de_n = int(sqrt(n))

    num_de_divs = 0
    for i in range(1, raiz_de_n + 1):
        if n % i == 0:
            num_de_divs += 1 if n / i == i else 2

    return num_de_divs

def main():
    print('Obtendo todos os números inteiros positivos altamente compostos menores que 5000:')
    r = 5000
    qtds_de_divs = [conta_divisores(i + 1) for i in range(r)]

    nums_altamente_compostos = [1]
    qtd_max_atual = qtds_de_divs[0]

    for n, qtd_de_divs in enumerate(qtds_de_divs):
        if qtd_de_divs > qtd_max_atual:
            nums_altamente_compostos.append(n + 1)
            qtd_max_atual = qtd_de_divs

    print(nums_altamente_compostos[0])
    for n in nums_altamente_compostos[1:]:
        fatores = [f'{p}^{e}' if e != 1 else str(p) for p, e in fatora(n).items()]
        print(f'{n} = {(' * ').join(fatores)}')

    print(
        '\nObservamos algumas coisas nessas dessa lista:\n' +
        '\t- Todos números altamentes compostos (exceto o 1) são pares, justificado abaixo;\n' +
        '\t- Numa fatoração aparecem todos os primos menores que o maior primo dessa fatoração;\n' +
        '\t- Nas fatorações as multiplicidades de cada primo aparecem de forma decrescente\n' +
        '\t  (para p_1^e_1 e p_2^e_2, temos p_1 < p_2 ==> e_1 >= e_2).\n'
    )

if __name__ == '__main__':
    main()