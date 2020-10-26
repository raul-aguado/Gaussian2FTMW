import os
from os import scandir, getcwd
import sys

def pause():
    print()
    print("Press enter to exit...")
    input("")
    pass

print("Path...")
path = input()
print("Number of atoms in the molecule...")
n_atoms = int(input())

filepaths = [arch.name for arch in scandir(path) if arch.is_file()]
for fp in filepaths:
    ext = os.path.splitext(fp)[-1].lower()
        
    if ext == ".log":
        full_path = path + "/" + fp
        with open (full_path, "r") as log:
            mylines = []
            for myline in log:
                chars = []
                mylines.append(myline)

            n = (int(len(mylines))-1)

            print(str(n) + "lines in the log")

            while mylines[n] != " and normal coordinates:\n":
                n=n-1
            else:
                n=n+3
                while mylines[n] != " - Thermochemistry -\n":
                    chars = []
                    for char in mylines[n]:
                        chars.append(char)
                    freq_1 = ''.join([str(elem) for elem in chars[18:33] if elem!=" "])
                    freq_2 = ''.join([str(elem) for elem in chars[34:60] if elem!=" "])
                    freq_3 = ''.join([str(elem) for elem in chars[60:74] if elem!=" "])
                    
                    if (float(freq_1) < 0 or float(freq_2) < 0 or float(freq_3) < 0):
                        print("Error with the frequencies in " + fp)
                        break

                    n = (n + n_atoms + 7)
                else:
                    print("Frequencies for " + fp + " are CORRECT")

                
pause()
