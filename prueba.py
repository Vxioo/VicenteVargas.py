nominaLibros=[]
generos=("Ficción","No Ficción","Ciencia")
def registrarLibros():
    try:
        nombreLibro=input("Ingrese el nombre del libro ")
        autorLibro=input("Ingrese el autor del libro ")
        print("generos disponibles")
        
        print(generos)
        SeleccionGenero = (input("escriba el genero ")).lower()
            
        precio=input("Ingrese el precio ")
        libros=[nombreLibro, autorLibro,SeleccionGenero,precio]
        nominaLibros.append(libros)
    except ValueError:
          print("Porfavor ingrese todos los datos")
def listaLibros():
      print("Nombre:\tAutor:\tGenero:\tPrecio:")
      print("..................................")
      for i in range(len(nominaLibros)):
        print(nominaLibros[i][0],end="\t")
        print(nominaLibros[i][1],end="\t")
        print(nominaLibros[i][2],end="\t")
        print(nominaLibros[i][3],end="\t")
        print()
        print("................................")
       
def registrarVenta():
    precioLibroUnidad=10000
    nombre=input("Ingrese el nombre del libro ")
    if nombre in nominaLibros[0]:
         print("libro encontrado ")
    cantidad=int(input("Ingrese la candidad de libros vendidos "))

    if cantidad<=50:
         precionfinal=cantidad*precioLibroUnidad
         print("Precio unidad", precioLibroUnidad)
         print("Precio final:",precionfinal)


     
def imprimirReporte():
    op=int(input("1.Imprimir todos  2.Por genero "))
    if op ==1:
        print("Nombre:\tAutor:\tGenero:\tPrecio:")
        print("----------------------------------------------------")
        print("..................................")
        for i in range(len(nominaLibros)):
            print(nominaLibros[i][0],end="\t")
            print(nominaLibros[i][1],end="\t")
            print(nominaLibros[i][2],end="\t")
            print(nominaLibros[i][3],end="\t")
            print()
            print("................................")
       
    elif op==2:
        GeneroBuscar = input("Ingrese el genero ")
        if GeneroBuscar in generos:
            print("genero encontrado")
            
             







while True:

    print("""1. Registrar libro
2. Listar todos los libros
3. Registrar venta
4. Imprimir reporte de ventas
5. Generar txt
6. Salir del Programa
""")
    

    opcion=int(input("Ingrese una opcion "))
    if opcion==1:
        registrarLibros()
    elif opcion==2:
        listaLibros()
    elif opcion==3:
           registrarVenta()

    elif opcion==4:
            imprimirReporte()

    elif opcion==5:
            print(":(")

    elif opcion==6:
            break

 

