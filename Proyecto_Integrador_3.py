# Importar las funciones readkey y key del módulo readchar
import os
from readchar import readkey, key

# Función para limpiar la terminal
def clear_and_print(n):
    os.system('cls' if os.name == 'nt' else 'clear' )
    print(f"Contador: {n}")
    
#Inicializamos el contador
contador = 0

# Pedir al usuario que presione una tecla y explicar cómo detener el programa
print(input("Por favor presione 'n' para incrementar el contador y para detener presione flecha 🡩 ")) 

# Inicia un bucle infinito
while True:
    # Leer la tecla presionada por el usuario
    k = readkey()

    # Verificar si la tecla presionada es la flecha hacia arriba
    if k == key.UP:
        # Si es así, imprimir un mensaje y romper el bucle para terminar el programa
        print("Oh!! has presionado 🡩  para detener ")
        break
    
        # Acá se verifica si la tecla n es presionada
    elif k == 'n':
        # Incrementamos el contador y mostraremos el nuevo número
        contador+= 1
        clear_and_print(contador) 
        
        # Verificamos si el contador ha llegado a 50
        if contador ==50:
            print("Has llegado al número 50, el programa se detendrá.")
            break