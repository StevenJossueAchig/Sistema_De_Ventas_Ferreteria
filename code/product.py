#Declaración de clase
#Componentes abreviaturas claves: def, __init__, self
#En todos los metodos, tiene que tener como arg el self (primero)
import random
import os
import memory_profiler
import timeit
import time
from tabulate import tabulate


def printPortade():
    print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNK0OkkkOO0KXWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMW0xoddxxkkOOxx0NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXxok00KXXNNNNNNWMMMMMMMMMWNNWMMMMMWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXxooookXWWMMMMMMMMMMMMMWXOdxXMMMMN0OXWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNkodookKXXXXK00XMMMMMMMXxolxXMMMW0dlxKWMMMMMWX00XWMMMMMMMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMWWWMMMMMMMMMMMMMWXkxOxkKXXNXKxooOWMMMMMW0oloxKNWWNkoloOWMMMMWKxoldxO0XNWMMMMMMMMMMMMMMM")
    print("MMMMMMMMMMWNKOxk0NWMMMMMMMMMWX000KXXXXXXKkollkNMMMMMWKdllodxxkxollo0WMMMW0dollollloxOXWWMMMMMMMMMMMM")
    print("MMMMMMMMMMW0olllox0NMMMMMMMMXkk00OkxdddddolllxNMMMMMMW0dllllllllodONMMMW0dlllllllllldO0kOKNMMMMMMMMM")
    print("MMMMMMMMMMWXxllllloxXWMMMMMMNkoolllllllllllllxXMMMMMMMNOolllooodOXWMMMNOololoollllllodolld0WMMMMMMMM")
    print("MMMMMMMMMMMW0dlllolo0WMMMMMMMN0kdoooolllllloldKWMMMMMMNklllllloONMMMMWKxollllllooolllllldONMMMMMMMMM")
    print("MMMMMMMMMMMMW0xoolloONMMMMMMMMWKxddddolllllllo0WMMMMMMKdlllllldKWMMWNKKK0Oxdoloollllllld0WMMMMMMMMMM")
    print("MMMMMMMMMMMMMWNX0xoldONMMMMMMMW0dddxdollllllloOWMMMMMW0olloollxXMMWKxooxk0KK0OxoollllodKWMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMWNOoloONMMMMMMMWKO0OdolllllllokNWWMMMNkollllloOWMMWKxdollodxO0KK0kxooxKWMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMN0dlokXWWWMMMMNO0N0doooddxxxxkkO00KKOxdooolo0WMMMWWX0xollllodxOKKKKXWMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMWKxoodkkOXWMMW00NNOkxxxddoollodxxxkkkkkkxxkXWMMMMMWNOollloollooxKWMMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMMXkollllokNWWX0kkkdoolllllllloxxxxxxxxxxkkO0KXNNWWXkolldOKKOkddONMMMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMWKxoodddxxkkxdolllllllloodxkO0KK0OOkkxxxxxxxxxkkO0Okxxx0WMMMWNNWMMMMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMWWN0xxxddoolllllloodxkOO0KXNNXXXNNNNNXKK0OOkxxxxxxxxxkkO0KXNWWMMMMMMMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMWWNK0OkdooolllllodxkkO0KXXXXK0OkxdddxkkOO0KKXNNNNXKK0OkkxxxxxxxxkO0KKXNWWMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMWXOxdoolllooodxkO0KXXXXK0OkxdoolllllooxxxxxxxxkkOO0KKXNNNXXK00OkkxxxxxxkkO0KNMMMMMMMMMMMM")
    print("MMMMMMMMMMMWKdloodxkO0KKXXXK0000koollllllllllllooxxxxxxxxxxxxxxxkkkO0KKXXXXXKK00OkkxxxkXMMMMMMMMMMMM")
    print("MMMMMMMMMMMMX00KXNWNK0kxk0KOx0NNkoollllllllllllooxxxxxxxxxxxxxxxxxxxxxxxkkO00KNWWNXXK00NMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMXxlllxXWKx0NXkolllllllllllllloxxxxxxxxxxxxxxxxxxxxxxxxxxxxxKWMMMMMMMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMXxloldO0kdxOOdololllllllllllloxxxxxxxxxxxxxxxxxxxxxxxxxxxxxKWMMMMMMMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMXxloldO0OxONXkollloollllllllloxxxxxxxxxxxxxxxxxxxxxxxxxxxxxKWMMMMMMMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMXxlolxXWKx0WNkoloollllllllllloxxxxxxxxxxxxxxxxxxxxxxxxxxxxxKWMMMMMMMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMXxloldO0kdxkxdllllllllllllllloxxxxxxxxxxxxxxxxxxxxxxxxxxxxxKWMMMMMMMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMXxlllooooolllllllloollllllllloxxxxxxxxxxxxxxxxxxxxxxxxxxxxxKWMMMMMMMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMXxllllllllllllllllllllllllllloxxxxxxxxxxxxxxxxxxxxxxxxxxxxxKWMMMMMMMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMXxllllllllllllllllllllllllllloxxxxxxxxxxxxk0KKK000OkxxxxxxxKWMMMMMMMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMXxllllllllllllllllllllllllllloxxxxxxxxxxxxkXWMMMMWWXkxxxxxxKWMMMMMMMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMXxllllllllllllllllllllllllllloxxxxxxxxxxxxkXMMMMMMMXkxxxxxxKWMMMMMMMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMXxllllllllllllllllllllllllllloxxxxxxxxxxxxkXMMMMMMMXkxxxxxxKWMMMMMMMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMXxllllllllllllllllllllllllllloxxxxxxxxxxxxkXMMMMMMMXkxxxxxxKWMMMMMMMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMXxllllllllllllllllllllllllllloxxxxxxxxxxxxkXMMMMMMMXkxxxxxxKWMMMMMMMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMXxllllllllllllllllllllllllllooxxxxxxxxxxxxkXMMMMMMMXkxxxxxxKWMMMMMMMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMXxllllllloolllllllllllllllllooxxxxxxxxxxxxkXMMMMMMMXkxxxxxxKWMMMMMMMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMXxllllllllllllllllllllllllllloxxxxxxxxxxxxkXMMMMMMWKkxxxxxxKWMMMMMMMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMN0kkkkkkkkkkkkkkkkkkkkkkkkkkkO000000000000KNMMMMMMMNK00000KXWMMMMMMMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMMMWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")

class Product:
    """
    Clase Producto para la implementacion de los productos
    Atributos:
        name: nombre del producto
        ID: id del producto para la venta
        stock: cantidad del producto presente
        price: precio del producto
        expirationDate: fecha de expiracion
        description: breve descripcion del sistema
    Metodos:
        constructor:
        validarStockFormatNumbre:
        validatePriceFormatNumberDecimal: 
    """
    #constructor = __init__ de la clase Product
    def __init__(self, name, stock, price, expirationDate, description):
        """
        Constructor para inicializa la clase ferreteria
        Recibe:
            self = clase producto, un objeto
            name = nombre de la ferreteria
        Retorna:
            no retorna
        """
        #definimos las variables de los atributos para el constructor
        self.ID = random.randint(10001,99999)
        self.name = name
        self.stock = stock
        self.price = price
        self.expirationDate = expirationDate
        self.description = description

    def validateStockFormatNumber(self):
        """
        Funcion para validar si el stock es un numero, perteneciente a la clase product
        Recibe:
            self = classe producto, un objeto
        Retorna:
            verdadero o falso dependiendo de si es o no un numero
        """
        #si el stock del obejto self es numerico
        if self.stock.isnumeric():
            #transformamos el stock de self en entero
            self.stock = int(self.stock)
            #retornamos verdadero
            return True
        #si el stock ingresado no es numerico
        else:
            #se imprime un mensaje que diga que la cantidad no esta en el formato numerico
            print("\n¡La cantidad del producto no esta en formato numérico.!\n")
            #retorna un falso
            return False

    def validatePriceFormatNumberDecimal(self):
        """
        Funcion para validar si el precio es un numero, perteneciente a la clase product
        Recibe:
            self = classe producto, un objeto
        Retorna:
            verdadero o falso dependiendo de si es o no un numero
        """
        #try condicion para validar un numero decimal
        try:
            #usando el precio del objeto enviado analizar si es flotante
            self.price = float(self.price)
            #retorna verdadero si es un decimal
            return True
        #excepcion para el valor erroneo
        except ValueError:
            #imprimir que el precio no esta en formato decimal
            print("\n¡El precio del producto no esta en formato numérico decimal.!\n")
            #retorna falso
            return False

#Taladro;100;10.80;No aplica;De acero resistente incluido tuercas
#Pintura;100;35.10;01/01/2024;Pintuco de color blanco,1L

class HardwareStore:
    """
    Clase Hardwarstore o Ferreteria para la composicion de productos
    Atributos:
        name = nombre de la ferreteria
    Metodos:
        sellProduct:
    """
    #arreglo productos para almacenar los productos
    products = []
    #variable para las ganancias
    earns = 0

    def __init__(self, name):
        """
        Constructor para inicializa la clase ferreteria
        Recibe:
            self = clase producto, un objeto
            name = nombre de la ferreteria
        Retorna:
            no retorna
        """
        self.name = name
    @profile
    def sellProduct(self):
        """
        Funcion para vender un producto
        Recibe:
            self = clase producto, un objeto
        Retorna:
            no retorna
        """
        #hacemos el llamado a la funcion listar productos para ver los productos que existen
        self.listProducts()
        #declaramos la variable idProducto para que se ingrese el id del producto que se escoja para vender
        idProducto = input("Ingrese el ID del producto a vender:")
        #variable existID para preguntar si el ID existe o no lo inicializamos con falso
        existID = False
        #para un producto en el arreglo de productos
        for product in self.products:
            #si el producto del ID es un entero y es encontrado
            if product.ID == int(idProducto):
                #el stock del objeto producto se reduce en 1 es decir que se ha vendido
                product.stock -= 1
                #y las ganancias se suman el precio del producto que se vendio
                self.earns += product.price
                #la variable bandera existe ID se asgina como verdadera
                existID = True
                #y se immprime que el producto a sido existosamente vendido
                print("\n¡Producto vendido exitosamente.!\n")
        #si el ID ingresado no existe es decir no es valido
        if not existID:
            #se imprime que el ID ingresado no existe
            print("\n¡El ID ingresado no existe.!\n")

    @profile
    def listEarns(self):
        """
        Funcion para listar las ganancias
        Recibe:
            self = clase producto, un objeto
        Retorna:
            no retorna
        """
        #se imprime las ganancias totales y se redondea las ganancias a dos decimales
        print("Ganancias totales: $"+str(round(self.earns,2))+"\n")
    @profile
    def addProduct(self):
        """
        Funcion para agregar un producto
        Recibe:
            self = clase producto, un objeto
        Retorna:
            no retorna
        """
        #definimos una variable data para el ingreso de los datos del objeto producto, que estaran en un formato separado por ";"
        name = input("Ingrese el nombre del producto: ")
        stock = input("Ingrese la cantidad del producto: ")
        price = input("Ingrese el precio del producto: ")
        expirationDate = input("Ingrese la fecha de caducidad del producto (DD/MM/AA): ")
        description = input("Ingrese la descripcion del producto: ")
        #color blanco, pintuco, 2L
        #Enviamos al constructor de la clase producto los parametros propios de el, de cada elemento ingresado
        product = Product(name=name, stock= stock, price=price, expirationDate=expirationDate,description=description)
        #Variables booleanas del tipo bandera
        validProduct = True
        #hacemos el llamado a la validacion del formato de numero enf el stock si no es valido
        if not product.validateStockFormatNumber():
            #entonces el producto valido es falso
            validProduct = False
        # o si el precio no es valido no es decimal
        if not product.validatePriceFormatNumberDecimal():
            #el producto no es valido
            validProduct = False
        #si el prodcuto es valido y el producto agregado no existe ya en la lista de prodcutos enviando su nombre
        if validProduct and not self.checkIsProductExistInList(name):
            #agregamos el producto a la lista de productos
            self.products.append(product)
            #variable linea asignada con todos los datos ingresados se concatenan para formar una sola cadena de caracteres separada por comas
            line = name+","+stock+","+price+","+expirationDate+","+description+"\n"
            #usamos la clase utils para ingresar el producto en un archivo de texto
            Utils.saveObjectsOnFile(filename="products.txt",line=line) 
            #imprimimos que el producto ha sido agregado correctamente
            print("\n¡Producto agregado correctamente.!\n")
        #si el producto ya existe
        else:
            #se imprime que el producto ingresado ya existe
            print("\n¡El producto que desea ingresar ya existe.!\n")
    @profile
    def listProducts(self):
        """
        Funcion para listar los productos
        Recibe:
            self = clase producto, un objeto
        Retorna:
            no retorna
        """
        # irmprimos el titulo lista de productos
        print("\nLISTA DE PRODUCTOS:\n")
        #si el tamanio de los productos es igual a cero entonces se envia el mensaje de que no existen productos
        if len(self.products) == 0:
            #se imprime que no existen productos agregados
            print("No existen productos agregados.\n")
        #si el tamanio no es cero
        else:
            #para los productos en la lista de productos
            for product in self.products:
                #hacemos el llamado a la funcion imprimir productos y enviamos el producto a imprimir
                self.printProduct(product=product)
    @profile
    def checkIsProductExistInList(self,name):
        """
        Funcion para analizar si el producto ya ha sido agregado
        Recibe:
            self = clase producto, un objeto
            name = nombre del producto
        Retorna:
            no retorna
        """
        #para un producto en el arreglo de productos
        for product in self.products:
            #si el nombre del producto transformado en minusculas es igual al nombre que recibio como parametro igual transformado en minusculas
            if product.name.lower() == name.lower():
                #retorna verdadero
                return True
        #si no existe retorna falso
        return False
    @profile
    def printProduct(self, product):
        """
        Funcion para imprimir el prodcto
        Recibe:
            self = clase producto, un objeto
            product = el producto que se va a imprimir
        Retorna:
            no retorna
        """
        print("---------------------------------------------------------------------------------------------")
        #definimos una variable d usando el formato de tabulate para imprimir el producto
        d = [ [str(product.ID), product.name, str(product.stock), str(product.price), product.expirationDate, product.description]]
        #imprimimos el producto
        print(tabulate(d, headers=["ID", "NOMBRE", "CANTIDAD", "PRECIO", "FECHA EXPIRACIÓN", "DESCRIPCIÓN"]))
        print("---------------------------------------------------------------------------------------------\n")
        
    @profile
    def searchProduct(self):
        """
        Funcion para buscar un producto
        Recibe:
            self = clase producto, un objeto
        Retorna:
            no retorna
        """
        #inicializamos a la variable existe producto como falsa
        existProduct = False
        #imprimios el tipo de busqueda que quiera realizar
        print("\nEscoja el tipo de busqueda que desea realizar\n")
        #opcion 1 por nombre
        print("1: Por nombre")
        #opcion 2 por ID
        print("2: Por ID")
        #uso de try para una excepcion
        try:
            #opcion de busqueda para ingresar con que se quiere buscar el producto
            optionSearch = int(input("Ingrese el número de la opción de busqueda deseada:"))
            #si la opcion de busqueda es por nombre
            if optionSearch == 1:
                #Pedimos el ingreso del nombre a buscar
                nombreProducto = input("Ingrese el nombre del producto que desea buscar:")
                #para un producto en la lista de productos
                for product in self.products:
                    #Pintura, pintura
                    #produc.name.lower() = Pintura = pintura
                    #produc.name.upper() = Pintura = PINTURA
                    #si el nombre del producto transformado a minusculas es igual al nombre de uno de los elementos igual transformado a minusculas
                    if product.name.lower() == nombreProducto.lower():
                        #imprimos que el producto ha sido encontrado
                        print("\nProducto encontrado.\n")
                        #y llamamaos a la funcion imprimir producto
                        self.printProduct(product=product)
                        #y la existencia del prodcuto pasa a ser verdadera
                        existProduct = True
            #Si en cambio la opcion de busqueda es por el ID
            elif optionSearch == 2:
                #se solicita el ID que se quiera buscar
                idProducto = int(input("Ingrese el ID del producto que desea buscar:"))
                #se realiza nuevamente la busqueda como en el anterior caso pero ahora con el ID
                for product in self.products:
                    #si el ID es igual al ID de algun producto 
                    if product.ID == idProducto:
                        #se muestra que el producto ha sido encontrado
                        print("\nProducto encontrado.\n")
                        #se llama a la funcion imprimir producto y se le envia el producto a imprimir
                        self.printProduct(product=product)
                        #la existencia del prodcuto cambia a verdadera
                        existProduct = True
            #si el producto no existe
            if not existProduct:
                #se muestra un mensaje de producto no encontrado
                print("Producto no encontrado.\n")
                #mostramos los productos existentes
                print("los productos que existen son: \n")
                #llamamos a la funcion para listar los productos
                hardwareStore.listProducts()
        #si se ingresa una opcion incorrecta
        except:
            #se imprime que la opcion ingresada no ha sido correcta
            print("Ingrese una opción correcta.\n")
    @profile
    def loadProducts(self):
        """
        Funcion para cargar los productos del documento de texto
        Recibe:
            self = clase producto, un objeto
        Retorna:
            no retorna
        """
        #en una variable line_list cargamos la funcion de cargar objetos de un archivo enviamos el nombre del archivo
        line_list = Utils.loadObjectsFromFile(filename="products.txt")
        #par una linea en el arreglo line_list
        for line in line_list:
            #separamos las palabras que esten igresadas con la llave siendo una coma
            line = line.split(",")
            #su el producto existe en el archivo
            if not self.checkIsProductExistInList(line[0]):
                #asignamos cada dato a cada posicion del arreglo
                product = Product(name=line[0], stock= int(line[1]), price=float(line[2]), expirationDate=line[3],description=line[4])
                #y en la clase productos agregamos cada producto para cargarlos en memeoria
                self.products.append(product)
        #demostramos que la carga ha sido exitosa
        print("\n¡Productos cargados desde txt exitosamente.!\n")
    
class Utils:
    """
        Clase utils para el manejo de un archivo txt
        atributos:
            
        metodos:
            sabeObjectsOnfile = guarda texto en el archivo
            loadObjectsFromFile = carga el texto del archivo
    """
    
    def validateExistenceOfFile(filename):
        """
        Funcion para validar la existencia del archivo de texto
        Recibe:
            filename = nombre del archivo de texto
        Retorna:
            true si el archivo existe
            false si el archivo no existe
        """
        #uso de try y excepcion para validar la existencia de un archivo
        try:
            #abriendo el archivo con el nombre que se envia como parametro y guardandolo en una variable
            with open(filename) as f_obj:
                #leemos el archio y lo almacenamos en una variable
                contents = f_obj.read()
        #si el archivo no existe
        except FileNotFoundError:
            #se muestra un mensaje de que el archivo no existe
            msg = "El archivo "+ filename + " no existe agrega productos para crearlo."
            #se imprime el mensaje
            print(msg)

    def saveObjectsOnFile(filename,line):
        """
        Funcion para guardar los objetos en un archivo de texto
        Recibe:
            filename = nombre del archivo de texto
            line = el texto a guardar
        Retorna:
            lines = lineas con el texto del documento
        r = solo lectura
        w = solo escritura (sobreescribe totalmente el archivo)
        a = agregación al final del archivo
        r+ = leer y escribir
        """
        #tomamos la direccion de donde se ejecuta el programa
        cwd = os.getcwd()
        #conformamos el nombre del archivo con la direccion que hemos sacado antes
        filename = cwd + "\\" + filename
        #abrimos el archivo donde enviamos el nombre del archivo para saber que archivo abrir
        file = open(filename,"a")
        #imprimimos la direccion del archivo que hemos abierto
        print(filename)
        #escribimos la linea que hemos enviado como parametro en el archivo
        file.write(line)
        #finalmente cerramos el archivo
        file.close()

    def loadObjectsFromFile(filename):
        """
        Funcion para cargar los objetos de un archivo de texto
        Recibe:
            filename = nombre del archivo de texto
        Retorna:
            lines = lineas con el texto del documento
        """
        #tomamos la direccion de donde se ejecuta el programa
        cwd = os.getcwd()
        #conformamos el nombre del archivo con la direccion que hemos sacado antes
        filename = cwd +"\\"+ filename
        #abrimos el archivo donde enviamos el nombre del archivo para saber que archivo abrir
        file = open(filename,"r")
        #y almacenamos las lineas en que se leen del archivo en una variable lineas
        lines = file.readlines()
        #cerramos el archivo
        file.close()
        #retronamos todo lo que se cargo y se leyo
        return lines

def calculateComplexityTime():
        """
        Funcion para calcular lcomplejidad de tiempo
        Recibe:
            no recibe
        Retorna:
            no retorna
        """
        print("Complejidad de tiempo de ejecución: O(n)")
        #python -m timeit -n 100 -s "import product" "product.Product()"
        inicio = time.time()
        hardwareStore.loadProducts()
        hardwareStore.sellProduct()
        hardwareStore.addProduct()
        hardwareStore.listProducts()
        hardwareStore.searchProduct()
        hardwareStore.listEarns()
        fin = time.time()
        print("Tiempo de ejecución: ", fin - inicio)

def menu():
    """
        Funcion para mostrar el menu
        Recibe:
            no recibe
        Retorna:
            option = a la option que el usuario escoga
    """ 
    #se imprime cada una de las opciones que puede ecoger
    print("\nEscoja un número del menú:\n")
    #el caso 1 para cargar productos
    print("1: Cargar Productos")
    #el caso 2 para vender productos
    print("2: Vender Producto")
    #el caso 3 para agregar un producto
    print("3: Agregar Producto")
    #el caso 4 para listar los productos
    print("4: Listar Productos")
    #el caso 5 para buscar los productos
    print("5: Buscar Productos")
    #el caso 6 para ver las ganancias
    print("6: Ver ganancias")
    #para el caso 7 el calculo de las compljidades
    print("7. Calcular complejidad de tiempo")
    #el casos 8 para salir
    print("8: Calcular complejidad de espacio")
    #se solicita la opcion y se almacena en option
    option = input("Escriba el número y presione enter...")
    #se retorna la opcion
    return option

def executeOptionFromMenu(option, hardwareStore):
    """
        Funcion para hacer el llamado de las funciones
        Recibe:
            option = opcion escogida por el usuario
            hardwarstore = objeto de tipo ferreteria
        Retorna:
            No retorna 
    """ 
    #si la opcion 1
    if option == 1:
        #hacemos el llamado a la funcion de la ferreteria de cargar productos
        hardwareStore.loadProducts()
    #si la opcion es 2
    elif option == 2:
        #hacemos el llamado a la funcion de la ferreteria para vender un producto
        hardwareStore.sellProduct()
    #si la opcion es igual a 3
    elif option == 3:
        #hacemos el llamado a la funcion de la ferreteria para añadir un producto
        hardwareStore.addProduct()
    #si la ocion es igual a 4
    elif option == 4:
        #hacemos el llamado a la funcion de la ferreteria para listar los productos
        hardwareStore.listProducts()
    #si la opcion es igual a 5
    elif option == 5:
        #hacemos el llamado a la funcion de la ferreteria para buscar un producto 
        hardwareStore.searchProduct()
    #si la opcion es igual a 6
    elif option == 6:
        #hacemos el llamado a la funcion de la ferreteria para ver las ganancias
        hardwareStore.listEarns()
    #si la opcion es igual a 7
    elif option == 7:
        #hacemos el llamado a la funcion para calcular las complejidades
        calculateComplexityTime()
    #si la opcion es igual a 8
    elif option == 8:
        #salimos
        exit()
    #si la opcion es invalida
    else:
        #llamamos nuevamente al menu y mandamos la opcion y el objeto ferreteria
        executeOptionFromMenu(option=menu(), hardwareStore = hardwareStore)


#if __name__ == "__main__": se inicializa el codigo desde esta linea (main)
if __name__ == "__main__":
    """
        Funcion usar el menu
        Recibe:
            No recibe
        Retorna:
            No retorna 
    """ 
    #imprimir la portada
    printPortade()
    #imprimir una bienvenida al sistema
    print("\n¡Bienvenido al sistema de gestión de venta de productos!\n")
    #instancia de la clase ferreteria enviando el nombre
    hardwareStore = HardwareStore(name="Ferreteria Popular")
    #variable para seguir mientras es verdadera
    loop = True
    #mientras lopp sea vedadero
    while(loop):
        #try para cpaturar la opcion del menu sea un entero
        try:
            #opcion como entero
            option=int(menu())
        #excepcion
        except:
            #option None
            option = None
            #imprimir que se ha seleccionado una opcion erroena
            print("\n¡Se ha seleccionado una opción que no existe.!\n")
        #si la opcion es diferente de none
        if option != None:
            #hacemos el llamado a la funcion para ejecutra el menu mandamos el objeto ferreteria y la opcion
            executeOptionFromMenu(option, hardwareStore=hardwareStore)
            #si la opcion es igual a 8
            if option == 8:
                #exit()
                #loop = False
                #se imprime un adios
                print("Adios\n")
                #se rompe el bucle
                break