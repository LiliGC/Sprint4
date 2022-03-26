#La clase Bodega la cual tendrá los siguientes atributos: 
# ● Id ● Nombre ● __Cantidad total de productos ● Proveedores ( lista de objetos proveedores ) 
# ● Un dato con los productos y su respectivo stock Y también deberá contar con los siguientes métodos:
#  ● Agregar_proveedor ● Eliminar_proveedor ● Transferir productos de una bodega a otra bodega. 
# ● Cantidad total de productos transferidos. ● Mostrar total de tipos de productos transferidos. 
# ● Mostrar total de productos en bodega. 
# La clase Proveedor tendrá los siguientes atributos: ● ID ● Nombre ● Tipo de productos que ofrece 
# Y también los siguientes métodos: ● Inscripción en bodega ● Modificar el tipo de producto ofrecido. 
# Cada Bodega tiene operarios y administradores. Ambos comparten la capacidad de consultar el número de proveedores por bodega. 
# Los administradores tienen la capacidad de conocer el número de proveedores por bodega y el stock.
#Agregue aplicaciones prácticas de los métodos creados en el ejercicio. Recomendamos dividir el ejercicio entre los integrantes del equipo. Consideraciones generales
#Creación de la clase Usuario

class Usuario:
    def __init__(self, run, nombre, contraseña):
        self.run=run
        self.nombre=nombre
        self.__contraseña=contraseña

#Creación de las clases Operarios y Administrador que heredan de Usuario

class Operarios(Usuario):
    pass
#Consultar proveedores
class Administrador(Usuario):
    pass
#Consultar provedores, bodega y stock


#Creación de la clase Bodega

class Bodega:
    def __init__(self, id, nombre, cantidad_productos, proveedores, productos, contador=0):
        self.id= id
        self.nombre= nombre
        self.__cantidad_productos=cantidad_productos
        self.proveedores=proveedores
        self.productos=productos
        self.contador= contador
#Creación de sucursal
class Sucursal(Bodega):
    pass

    #Crear metodos: 1. Agregar proveedor
                #   2. ELiminar proveedor
                #   3. Transferir productos bodega: despacho productos, recepcion de productos como el ABP4.
                #   4. Total productos despachados de bodega.
                #   5. Total por tipo de productos
                #   6. Total productos bodega(sum (productos.stock))

#Creación de la clase Proveedor
class Proveedor:
    def __init__(self, id, nombre, productos):
        self.id= id
        self.nombre= nombre
        self.productos=productos

    #Crear métodos: 1. Inscripción de Bodega
                #   2. Modificar tipo de producto.

#Creación de la clase Productos colaboración con Proveedor
class Productos:
    def __init__(self, sku, nombre, categoria, proveedores, stock):
        self.sku = sku
        self.nombre = nombre
        self.categoria = categoria
        self.proveedores= proveedores
        self.stock= stock

