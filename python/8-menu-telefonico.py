def mostrar_menu():
    print('''
    ************************************
    *  Menu USSD
    *  1. Ver saldo
    *  2. Recargar saldo
    *  3. Transferir saldo
    *  4. Salir
    ************************************
          ''')
    
def mostrar_saldo(saldo):
    print(f'''
    ************************************
    Su saldo actual es: {saldo} pesos
    ************************************
          ''')
    
def recargar_saldo(saldo):
    recarga = float(input("Ingrese el monto a recargar: "))
    saldo += recarga
    print(f"Se ha recargado {recarga} pesos")
    mostrar_saldo(saldo)
    
def transferir_saldo(saldo):
    transferencia = float(input("Ingrese el monto a transferir: "))
    if transferencia > saldo:
        print("No tiene saldo suficiente para realizar la transferencia.")
    else:
        saldo -= transferencia
        print(f"Se ha transferido {transferencia} pesos")
        mostrar_saldo(saldo)
        
def limpiar_pantalla():
    import os
    os.system("cls" if os.name == "nt" else "clear")

def main():
    saldo = 1000  # saldo inicial de ejemplo
    
    while True:
        mostrar_menu()
        
        opcion = input("Seleccione una opción --> ")
        
        if opcion == "1":
            mostrar_saldo(saldo)
        elif opcion == "2":
            recargar_saldo(saldo)
        elif opcion == "3":
            transferir_saldo(saldo)
        elif opcion == "4":
            print("Gracias por utilizar nuestro servicio USSD.")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del menú.")

if __name__ == "__main__":
    main()
