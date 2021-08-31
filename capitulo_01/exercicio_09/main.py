'''
 Números Inteiros e Criptografia RSA - Capítulo 1.
 Exercício 9 - Teste de probabilidade para par de co-primos.
'''
from math   import pi
from tqdm   import tqdm
from random import randint

BARRA_GRAFICA         = '-' * 50
QUOCIENTE_ESPERADO    = 6.0 / pi**2

get_rand = lambda: randint(0, 1e30)

# Realiza o algoritmo de euclides
def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

# Executa o teste para diferentes quantides de pares
def roda_teste():
    resultados = dict()
    qtds       = map(int, [1e1, 1e2, 1e3, 1e4, 1e5, 1e6, 1e7])
    for qtd_atual in qtds:
        descricao  = f'Rodando para {qtd_atual:8d} pares'
        qtd_de_iguais_a_1 = 0
        for _ in tqdm(range(qtd_atual), ncols=90, desc=descricao):
            qtd_de_iguais_a_1 += (gcd(get_rand(), get_rand()) == 1)

        resultados[qtd_atual] = qtd_de_iguais_a_1 / qtd_atual

    return resultados

def main():
    # Realiza testes para diferentes quantidades de pares
    resultados = roda_teste()

    # Printa os dados do resultado como um todo
    cabecalho=[
        BARRA_GRAFICA,
        f'Quociente esperado = 6/pi² = {QUOCIENTE_ESPERADO}',
        BARRA_GRAFICA
    ]
    print('\n'.join(cabecalho))
    print(f'Quantidade de pares | Quociente obtido ')
    for qtd_pares, quotient in resultados.items():
        print(f' {qtd_pares:<18} |  {quotient:<16}')

    print(
        '\nAssim, verificamos que quanto maior a quantidade\n' +
        'de pares testados mais próximo de 6/pi² é o quociente.'
    )

if __name__ == '__main__':
    main()