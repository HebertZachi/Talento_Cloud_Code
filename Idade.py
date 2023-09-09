# Desenvolva um programa que recebe do usuário nome completo e ano de nascimento que seja entre 1922 e 2021.
# A partir dessas informações, o sistema mostrará o nome do usuário e a idade que completou, ou completará, no ano atual (2022).

# Caso o usuário não digite um número ou apareça um inválido no campo do ano, o sistema informará o erro e continuará perguntando até que um valor correto seja preenchido.

def pegarAno():
    while True:
        try:
            print("")
            ano = int(input("Digite o ano de nascimento entre 1922 e 2021: "))
            if (ano >= 1922) and (ano <= 2021):
                return ano
            else:
                print("")
                print("Ano fora do intervalo permitido.")
        except:
            print("")
            print("Valor digitado está incorreto. Digite o ano de nascimento entre 1922 e 2021")

def calcularIdade(anoNascimento):
    anoAtual = 2022
    return anoAtual - anoNascimento

nome = input("Digite seu nome completo: ")
anoNascimento = pegarAno()
idade = calcularIdade(anoNascimento)

for i in range(1, 20):
  print("")
print("Nome: ", nome)
print("A sua Idade em 2022 é", idade,"anos")