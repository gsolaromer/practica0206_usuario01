def numero (n):

    '''Recibe un número del 1 al 10 y entrega un fichero con su tabla de multiplicar'''

    nombre = "tabla-" + str(n) + ".txt"
    file = open(nombre, "w")
    
    for i in range(1,11):
        file.write (str(i) + "x" + str(n) + "=" + str(i*n) + "\n")
    file.close()
    return("tabla generada: " + nombre)

print(numero(2))