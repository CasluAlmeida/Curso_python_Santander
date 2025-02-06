print('Olá, Mundo!')


idade = 20
if idade < 18:
    print('Menor de idade!')
elif 18 <= idade <= 21:
    print("Adulto!")
else:
    print('Maior de idade!')

# Este é um comentário de uma única linha

"""
Este é um comentário
de várias linhas
"""

a = 20.5
b = 41
c = 10


resultado = (a + b) * c

tipo = type(a)

print(tipo)
print(f'O resultado é {resultado}')