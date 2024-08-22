# Imprima a frase: Python na Escola de Programação da Alura
def exercicio1():
    print("Python na Escola de Programação da Alura")

# Imprima a frase: Meu nome é {nome} e tenho {idade} anos em que nome e idade precisam ser valores armazenados em variáveis.
def exercicio2():
    nome = "Josecreisson"
    idade = 27
    print(f"Meu nome é {nome} e tenho {idade} anos")

'''
Imprima a palavra: ‘ALURA’ de modo que cada letra fique em uma linha, como mostrado a seguir:
A
L
U
R
A
'''
def exercicio3():
    alura = "ALURA"
    for letra in alura:
        print(letra)
    print("\n")
    print("A","L","U","R","A"," ", sep="\n")


"""
Imprima a frase: 
O valor arredondado de pi é: {pi_arredondado} 
em que o valor de pi precisa ser armazenado em uma variável e arredondado para apenas duas casas decimais. 
Para facilitar, utilize pi = 3.14159
"""

def exercicio4():
    pi = 3.14159
    pi_arredondado = round(pi,2)
    print(f'O valor arredondado de pi é: {pi_arredondado}')



# Solicite ao usuário que insira um número e, em seguida, use uma estrutura if else para determinar se o número é par ou ímpar.
def exercicio5():
    numero = int(input("insira um número: "))
    if numero % 2 == 0:
        print("Numero Par")
    else:
        print("Numero Impar")



"""
Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else para classificar a idade em categorias de acordo com as seguintes condições:

Criança: 0 a 12 anos;
Adolescente: 13 a 18 anos;
Adulto: acima de 18 anos.

"""

def exercicio6():
    idade = int(input('Digite a sua idade: '))
    if 0 < idade < 12:
        print("Criança")
    elif 13 < idade < 18:
        print("Adolescente")
    else:
        print("Adulto")
        
def exercicio6v2():
    idade = int(input('Digite a sua idade: '))
    match idade:
        case i if 0 < i < 12:
            print("Criança")
        case i if 13 < i < 18:
            print("Adolescente")
        case i if i > 18:
            print("Adulto")


"""
Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o 
nome de usuário e a senha fornecidos correspondem aos valores esperados determinados por você.
"""
def exercicio7():
    usuario = input('Digite o usuario: ')
    senha = input('Digite a senha: ')

    if usuario == 'Lumbert' and senha == 'senha123':
        print('Sucesso')
    else:
        print('Errou')

"""
Solicite ao usuário as coordenadas (x, y) de um ponto qualquer e utilize uma estrutura if elif else para determinar em qual quadrante do plano cartesiano o ponto se encontra de acordo com as seguintes condições:

Primeiro Quadrante: os valores de x e y devem ser maiores que zero;
Segundo Quadrante: o valor de x é menor que zero e o valor de y é maior que zero;
Terceiro Quadrante: os valores de x e y devem ser menores que zero;
Quarto Quadrante: o valor de x é maior que zero e o valor de y é menor que zero;
Caso contrário: o ponto está localizado no eixo ou origem.
"""

