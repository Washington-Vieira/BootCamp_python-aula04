# x = -3
# if x <= 2:
#     print("e menor do que zero")
# elif x <= 00:
#     print("e menor do que dois")
# else:
#     print("More")

# range não gera até o ultimo valor.

# lista = ["fabio", "luciano", "washington"]

# for aluno in lista:
#     print(aluno)

#estrutura complexa dicionarios
texto = "Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation."

palavras = texto.split()
print(palavras)
contagem_de_palavra = {}

# Eu quero percorrer todas as palavras dentro de palvras e checar se ela ja está no meu conta palavras

for palavra in palavras:
    if palavra in contagem_de_palavra:
        contagem_de_palavra[palavra] = +1
    else:
        contagem_de_palavra[palavra] = 1

hoje = 1
e = 1
bootcamp = 2
