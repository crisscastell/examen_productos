import os
import libre.menu as menu

def clear():
    if os.name == 'nt':
        os.system('cls')
    else: 
        os.system('clear')

opcion_menu={
    1 : "Agregar un producto",
    2 : "Actualizar cantidad de productos",
    3 : "Inventario completo",
    4 : "Buscar producto",
    5 : "salir"
}

def main():
    opcion=None
    while True:

        clear()
        print("MENU")
        for key, value in opcion_menu.items():
            print(f"{key} - {value}")

        opcion=input("ingrese una opcion: ")

        if not opcion.isdigit():
            print("opcion no valida, ingrese nuevamente")
            opcion=None
            input("presione ENTER para continuar")
            continue

        opcion=int(opcion)
        if not opcion in opcion_menu.keys():
            print("numero no valido, ingrese nuevamente")
            opcion=None
            input("presione ENTER para continuar")
            continue

        menu.menu_opciones(opcion)
main()

