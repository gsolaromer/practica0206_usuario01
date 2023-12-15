def numero(n):
    '''Recibe un numero del 1 al 10, lee el 
    fichero y muestra su tabla de multiplicar'''

    nombre = "tabla-" + str(n) + ".txt"
    if n>0 and n<11:
        try:
            f = open(nombre)
        except FileNotFoundError:
            return("Fichero no encontrado")
        else:
            print(f.read())
            f.close()
            return("Listo!!!")
    else:
        return("Numero invalido")

print(numero(3))