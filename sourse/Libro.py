class Libro: 
    
    def __init__(self, titulo, isbn, precioVenta, PrecioCompra, cantidad, rutaImagen):
        self.__titulo = titulo
        self.__isbn = isbn 
        self.__precioVenta = precioVenta
        self.__precioCompra = PrecioCompra
        self.__cantidad = cantidad
        self.__rutaImagen = rutaImagen
        self._transaccion = []
        
    def getTitulo(self):
        return self.__titulo
        
    def getIsbn(self):
        return self.__isbn
    
    def getPrecioVenta(self):
        return self.__precioVenta
    
    def getPrecioCompra(self):
        return self.__precioCompra
    
    def getCantidad(self):
        return self.__cantidad
    
    def getRutaImagen(self):
        return self.__rutaImagen
    