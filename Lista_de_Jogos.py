import forca
import adivinhacao

print("*" * 33)
print("*" * 33)
print("****** Bem-vindo ao Arcade! *****")
print("* Escolha o jogo que quer jogar *")
print("*" * 33)
print("*" * 33, end="\n\n\n")

print("(1) Forca", "(2) Advinhação", sep=("\n"), end=("\n\n"))
jogo = int(input("Escolha qual jogo você quer jogar: "))

if jogo == 1:
    print("Jogando forca...")
    forca.jogar()

elif jogo == 2:
    print("Jogando Advinhação...")
    adivinhacao.jogar()
