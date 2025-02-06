nome = "Lucas"
idade = 24
altura = 1.80
# altura_ajustada = "{:.2f}".format(altura)
is_estudante = False

if is_estudante:
    estudante = 'estou estudando.'
else:
    estudante = 'não estou estudando.'

print(f'O meu nome é {nome}, tenho {idade} anos de idade, possuo {altura:.2f} de altura e {estudante}')