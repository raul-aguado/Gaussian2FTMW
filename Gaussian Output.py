import os
from os import scandir, getcwd
import sys
import time

print(""*100)
print("        === Menu principal ===        ")
print()
print("1. Comprobacion de archivos")
print("2. Busqueda de constantes de rotacion")
print()
print("======================================")
print()
opt = input("Elija una opcion... ")
print(""*2)

mylines = []
chars = []

if opt == "1":
    ruta = input("Introduce la ruta de los acrhivos para analizar... ")
    print()

    filepaths = [arch.name for arch in scandir(ruta) if arch.is_file()]
    for fp in filepaths:
        ext = os.path.splitext(fp)[-1].lower()
        
        if ext == ".log":
            ruta_completa = ruta + "/" + fp
            with open (ruta_completa, "r") as log:
                for myline in log:
                    mylines.append(myline)

                n = (int(len(mylines))-1)

                for char in mylines[n]:
                    chars.append(char)

                linea_final = ''.join([str(elem) for elem in chars[0:31] if elem!=" "])
                
                if linea_final == "NormalterminationofGaussian":
                    print("El archivo " + fp + " es correcto.")
                    print()

                else:
                    print("El archivo " + fp + " no es correcto")
                    print()
    pause

elif opt == 2:
    ruta = input("Archivo para analizar... ")
    print()

    with open (ruta, "r") as log:
        for myline in log:
            mylines.append(myline)
            
    n = (int(len(mylines))-1)

    if mylines[n] == " Rotational constants (MHZ):\n":
        n=n-1
        
    else:
        m = n+13
        while n<m:
            print(mylines[n])
            n=n+1    
    pause

else:
    exit
