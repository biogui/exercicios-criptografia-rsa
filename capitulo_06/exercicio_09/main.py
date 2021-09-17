'''
 Números Inteiros e Criptografia RSA - Capítulo 6.
 Exercício 9 - Números de Carmichael.
'''
from itertools import combinations
from sympy     import primerange
from numpy     import prod

LIMITE_PRIMOS = 1000

def gera_impares_com_fatores_unicos(d):
    possiveis_fatores = list(primerange(3, LIMITE_PRIMOS))
    possiveis_n       = list(combinations(possiveis_fatores, d))

    return possiveis_n

def eh_de_carmichael(fatores):
    for p in fatores:
        modulos = [f % (p - 1) for f in fatores]
        if prod(modulos) % (p - 1) != 1: return False

    return True

def main():
    print('Obtendo os números de carmichael com d primos (< 10^3) em sua fatoração, temos:')
    for d in range(1, 5):
        impares_fatorados  = gera_impares_com_fatores_unicos(d)

        nums_de_carmichael = list(
            map(
                lambda fatoracao: f'n = {"x".join(map(str, fatoracao))}',
                filter(
                    lambda fatoracao: eh_de_carmichael(fatoracao),
                    impares_fatorados
                )
            )
        )

        nums_carmichael_str = "\n\t".join(map(str, nums_de_carmichael))
        if nums_de_carmichael:
            print(f'• d = {d}: ')
            print(f'\t{nums_carmichael_str}')
        else:
            print(f'• d = {d}: nenhum número encontrado.')
    print('O número de combinações entre 5 ou mais primos menores que 10^3 é muito grande para ser processada ...')

if __name__ == "__main__":
    main()