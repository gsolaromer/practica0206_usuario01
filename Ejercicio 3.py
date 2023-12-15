def numero(n,m):

    '''Recibe dos numeros n y m, entre 1 y 10, 
    lea el fichero y muestre la linea m del fichero'''
    
    if (n<0 or n>10) or (m<0 or m>10):
        print("Error... Verifica los numeros que escribiste")
    else:
        nombre = "tabla-" + str(n) + ".txt."
        try:
            f = open(nombre)
        except FileNotFoundError:
            print("NO SE ENCONTRO EL ARCHIVO")
        else: 
            lineas = f.readlines()
            print(lineas(m-1))
            f.close
            return("Listo!!!")
        
print(numero(2,3))