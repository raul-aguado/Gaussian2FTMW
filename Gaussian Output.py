import os
from os import scandir, getcwd
import sys
import time

print(""*100)
print("           === Main menu ===           ")
print()
print("1. Prepare .COM files from .xyz files")
print("2. Gaussian .log check")
print("3. Rotational cosntants")
print()
print("=======================================")
print()
opt = input("Choose an option... ")
print(""*2)

mylines = []
chars = []

if opt == "1":
    ruta = input("Path of .xyz files to prepare... ")
    print()

    filepaths = [arch.name for arch in scandir(ruta) if arch.is_file()]
    for fp in filepaths:
        ext = os.path.splitext(fp)[-1].lower()
        
        if ext == ".xyz":
            ruta_completa = ruta + "/" + fp
            com = ruta_completa.replace(".xyz", ".txt")
            com_file = open(com, "w")

            com_file.write("%mem=2048mb\n")
            com_file.write("%nproc=2\n")
            com_file.write("%chk=" + fp + "\n")
            com_file.write("#B3LYP/6-311++G(d,p) opt freq output=pickett empiricaldispersion=GD3")
            com_file.write(os.linesep)
            com_file.write(fp )
            com_file.write(os.linesep)
            com_file.write("0 1\n")
            
            with open (ruta_completa, "r") as log:
                for myline in log:
                    com_file.write(myline)

            com_file.write(os.linesep*10)
            com_file.close()

if opt == "2":
    ruta = input("Path of files to check... ")
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
                    print("File " + fp + " is CORRECT.")
                    print()

                else:
                    print("Bad termination of " + fp + " file.")
                    print()

elif opt == "3":
    ruta = input("File to check... ")
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

else:
    exit
