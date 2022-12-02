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
            print("\nDados")
            dados()
        elif i == 3:
            break
        else:
            print("Opcion invalida")
            
#Los datos al azar
def dados_@usuario():
    dato1 = random.randint(1,6)
    dato2 = random.randint(1,6)
    print("Primer dato: ", dato1)
    print("Segundo dato: ", dato2)
    suma= dato1+dato2
    if suma==7:
        print("¡GANASTE!")
    else:
        print("Mejor suerte para la proxima")

if __name__ == "__main__":
    menu()