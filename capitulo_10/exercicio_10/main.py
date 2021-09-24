'''
 Números Inteiros e Criptografia RSA - Capítulo 10.
 Exercício 10 - Teste de Pepin.
'''
import datetime

F = lambda k: 2**(2**k) + 1

def pot_mod(a, k, n):
    modulo = 1
    while k != 0:
        if k % 2 == 1:
            modulo = (a * modulo) % n
            k = (k - 1) // 2
        else:
            k = (k - 1) // 2

        a = (a * a) % n

    return modulo

def teste_de_pepin(k):
    num_de_fermat = F(k)

    return (pot_mod(5, (num_de_fermat - 1) // 2, num_de_fermat) == num_de_fermat - 1)

def main():
    print('Verificando qual maior n é computacionalmente aplícavel ao teste de Pepin ...')

    n = 5
    duracao = datetime.datetime.now() - datetime.datetime.now()
    while duracao.total_seconds() < 60:
        inicio = datetime.datetime.now()

        resultado = 'primo' if teste_de_pepin(n) else 'composto'

        print(f'\tn = {n} -> F({n}) é {resultado}.')
        n += 1

        duracao = datetime.datetime.now() - inicio

    duracao = duracao.total_seconds() // 60
    print(f'Para n = {n - 1} o programa já começa a demora mais que cerca de {duracao} minutos.')

if __name__ == "__main__":
    main()