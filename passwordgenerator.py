import random

print('Bem-vindo(a) ao seu gerador de senhas aleatórias')
caracteres = 'abcdefghijklmnopqrstuvwsyzABCDEFGHIJKLMNOPQRSTUVWSYZ!@#$%&*^(),.0123456789'
num_senhas = input('Quantas senhas você quer gerar? ')
num_senhas = int(num_senhas)

tamanho = input('Quantidade de caracteres da sua senha: ')
tamanho = int(tamanho)

print('\nEssas são as suas senhas: ')

for senha in range(num_senhas):
    senhas = ''


