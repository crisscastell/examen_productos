
inventario={}

def menu_opciones(opcion):
    match opcion:
        case 1: #agregar 
            nombre=input("que producto desea agregar?: ")
            cantidad=input("ingrese la cantidad: ")
            precio= input("ingrese el precio del producto: ")
            producto = { 'nombre' : nombre,
                        'cantidad' : cantidad,
                        'precio' : precio }
            inventario[nombre]=producto
            print("producto agregado")
            input("presione ENTER si desea continuar...")
            return
        case 2: #actualizar cantidad
            nombre=input("escriba el nombre del producto: ")
            if nombre in inventario.keys():
                producto = inventario[nombre]
                cantidad = input("ingrese la cantidad: ")
                producto['cantidad']=cantidad                
                inventario[nombre]=producto
            print("cantidad actualizada")
            input("presione ENTER si desea continuar...")
            return
        case 3: #inventario completo
            for key, value in inventario.items():
                print(f"{key}\ncantidad: {value["cantidad"]}\nprecio: {value["precio"]}")
                print("=============")
            input("presione ENTER para continuar...")
            return
        case 4:
            nombre_producto=input("ingrese el nombre del producto: ")
            producto = inventario.get(nombre_producto)
            if producto==None:
                print("producto no encontrado")
                input("presione ENTER para continuar...")
            else:
                print(f"NOMBRE: {producto["nombre"]}\ncantidad: {producto["cantidad"]}\nprecio: {producto["precio"]}")
                print("=============")
                
            input("presione ENTER para continuar...")
        case 5: 
             exit()





