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

