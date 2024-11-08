print("Binvenido al sistema de control de stock: ".center(60,'-'))
cantidad=[]
productos=[]
precio=[]

while True:
    print(""""
    (1) Añadir Articulos
    (2) Buscar productos
    (3) Modificar productos
    (4) Ver productos
    """)
    
    respuesta=int(input("Use una opción: "))
    if respuesta == 1:
        
        '''
        ac = añadir cantidad
        ap = añadir producto
        apre = añadir precio
        '''
        ac= int(input("Ingrese la cantidad de productos: "))
        ap=input("Ingrese nombre del producto: ")
        apre=int(input("Ingrese el precio del producto: "))
        
#añadimos productos, cantidades y/o precios
        cantidad.append(ac)
        productos.append(ap)
        precio.append(apre)
    elif respuesta ==2:
        buscador = input("Ingrese el nombre del producto: ")    
        #buscamos el producto y lo imprimimos
        posicion=productos.index(buscador)
        print("La cantidad del producto es: ",cantidad[posicion])
        print("El nombre del producto es: ",productos[posicion])
        print("El precio del producto es: ",precio[posicion])
    elif respuesta==3:
        buscador = input("Ingrese el nombre del producto a modificar: ")    
        posicion=productos.index(buscador)
        ac= int(input("Ingrese la cantidad de productos: "))
        ap=input("Ingrese nombre del producto: ")
        apre=int(input("Ingrese el precio del producto: "))
        cantidad[posicion] = ac
        productos[posicion] = ap
        precio[posicion] = apre
    elif respuesta==4:
        print("La cantidad es: ",cantidad)
        print("El nombre es: ",productos)
        print("El precio del producto es: ",precio)
    else:
        break