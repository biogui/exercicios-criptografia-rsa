'''
 Números Inteiros e Criptografia RSA - Capítulo 1.
 Exercício 9 - Teste de probabilidade para par de co-primos.
'''
from math import pi
from tqdm import tqdm
from random import randint

UI_BAR         = '-' * 50
EXPEC_QUOTIENT = 6.0 / pi**2

get_rand = lambda: randint(0, 1e30)

# Realiza o algoritmo de euclides
def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

# Executa o teste para diferentes quantides de pares
def run_test():
    results   = dict()
    amts_list = map(int, [1e1, 1e2, 1e3, 1e4, 1e5, 1e6, 1e7])
    for cur_amt in amts_list:
        description  = f'Rodando para {cur_amt:8d} pares'
        amt_equals_1 = 0
        for _ in tqdm(range(cur_amt), ncols=90, desc=description):
            amt_equals_1 += (gcd(get_rand(), get_rand()) == 1)
        
        results[cur_amt] = amt_equals_1 / cur_amt

    return results

def main() -> None:
    # Realiza testes para diferentes quantidades de pares
    results = run_test()

    # Printa os dados do resultado como um todo
    header=[
        UI_BAR,
        f'Quociente esperado = 6/pi² = {EXPEC_QUOTIENT}',
        UI_BAR
    ]
    print('\n'.join(header))
    print(f'Quantidade de pares | Quociente obtido ')
    for amt_pair, quotient in results.items():
        print(f' {amt_pair:<18} |  {quotient:<16}')

    print('\nAssim, verificamos que quanto maior a quantidade de pares testados ' +
        'mais próximo de 6/pi² é o quociente.')

if __name__ == '__main__':
    main()