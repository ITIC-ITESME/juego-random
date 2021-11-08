# Juegos de azar, utilizando numeros aleatoreos.
import random

def tombola():
    oportunidades = 10 
    for i in range(oportunidades):
        numeroSuerte = int(input('Escribe un numero del 1 al 10: '))
            # randint([inicio],[final])
        tombola = random.randint(1,10)
        print('El numero es ', tombola)
        if numeroSuerte==tombola:
            print('!Ganaste!')
            break
        else:
            print('Sigue paticipando')

def dados():
    dado1 = random.randint(1,6)
    dado2 = random.randint(1,6)
    print("Primer dado: ",dado1)
    print("Segundo dado: ",dado2)
    suma = dado1 + dado2
    if suma == 7:
        print("!Ganaste!")
    else:
        print("Mejor suerte para la proxima")

# Menu de juego
def menu():
    i = 0
    while True:
        print("\nSeleciona el juego:")
        print("1. Tombola")
        print("2. Dados")
        print("3. Salir")
        i = int(input("Ingresa seleccion: "))
        if i == 1:
            print("\nTombola")
            tombola()
        elif i == 2:
            print("\nDados, que suman 7")
            dados()
        elif i == 3:
            break
        else:
            print("Opcion invalida")

if __name__ == "__main__":
    menu()