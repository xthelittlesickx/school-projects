from collections import deque

class BloqueMemoria:
    def __init__(self, tamano):
        self.tamano = tamano
        self.direccionMemoria = bytearray(tamano)

colaMemoria = deque()

def asignarMemoria(tamano):
    bloque = BloqueMemoria(tamano)
    colaMemoria.append(bloque)
    print(f"Asignados {tamano} bytes en la direccion {id(bloque.direccionMemoria)}")

def liberarMemoria():
    if colaMemoria:
        bloque = colaMemoria.popleft()
        print(f"Liberados {bloque.tamano} bytes de {id(bloque.direccionMemoria)}")
    else:
        print("No hay memoria para liberar.")

def mostrarCola():
    print("Estado actual de la memoria (FIFO):")
    for bloque in colaMemoria:
        print(f"[ {bloque.tamano} bytes en {id(bloque.direccionMemoria)} ] -> ", end='')
    print("FIN")

def main():
    while True:
        print("1. Asignar memoria")
        print("2. Liberar memoria")
        print("3. Mostrar estado de la memoria")
        print("4. Salir")
        opcion = int(input())

        if opcion == 1:
            tamano = int(input("Ingrese el tamano de memoria a asignar: "))
            asignarMemoria(tamano)
        elif opcion == 2:
            liberarMemoria()
        elif opcion == 3:
            mostrarCola()
        elif opcion == 4:
            break
        else:
            print("Opcion no valida")

if __name__ == "__main__":
    main()
