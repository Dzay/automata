__author__ = 'ING26'
#Acepta cadenas que terminan en A y tienen un numero par de caracteres
'''
q=["q0","q1","q2","q3"]
sigma=["A","B"]
transiciones=[["q0","A","q1"],["q0","B","q3"],["q1","A","q2"],["q1","B","q0"],["q2","A","q1"],["q2","B","q3"],["q3","A","q2"],["q3","B","q0"]]
inicio="q0"
finales=["q2"]'''

palabras=["AB","AA","AAA","AAAA","ABBA"]

text_file = open("Automata.txt", "r")
list = text_file.read().splitlines()

q =         list[0].split(" ")     #Lista de estados
sigma =     list[1].split(" ")     #Alfabeto del lenguajes
inicio =    list[2].split(" ")[0]  #Estado de inicio
finales =   list[3].split(" ")     #Estados finales
temporal =  list[4].split(" ")     #
transiciones = []

for tran in temporal:
    transiciones.append(tran.split("-"))
estadoActual=inicio
text_file.close()
estados=len(q)
lensigma=len(sigma)
for palabra in palabras:
    for char in palabra:
        if char in sigma:
            for i in range(lensigma*estados):
#                print(i)
                if transiciones[i][0]==estadoActual:
#                    print(i)
                    if transiciones[i][1]==char:
                        estadoActual=transiciones[i][2]
#                        print(estadoActual)
                        break
        else:
            estadoActual=""
            break
    if estadoActual in finales:
        print("La cadena "+palabra+" SI es aceptada")
    else:
        print("La cadena "+palabra+" NO es aceptada")
    estadoActual=inicio[0]
#comentario de linea
"""comentario multilinea
ID	A	B
q0	q1	q3
q1	q2	q0
q2	q1	q3
q3	q2	q0"""
#----------------------------Generando Grafico--------------------------------------
file=open("graph.gv","w")
file.write("digraph G {\n")
file.write("rankdir=LR;\n")
file.write('inicio [shape=none,label=""];\n')
file.write("node [shape=doublecircle];")
for acept in finales:
    file.write(" "+acept)
file.write(";\n")
file.write("node [shape=circle];\n")
file.write("inicio->"+inicio+"\n")

for i in range(lensigma*estados):
    file.write(transiciones[i][0]+"->"+transiciones[i][2]+'[label="'+transiciones[i][1]+'"];\n')
file.write("}")
file.close()


import os
os.system("dot -Tpng graph.gv -o graph.png")
os.system("xdg-open graph.png")

"""The simplest way, not recommendable:

import os
# ...

os.system(commandString)
Better use subprocess, e.g.:

import subprocess
# ...

subprocess.call(['echo', i], shell=True)
Note that shell escaping is your job with these functions and they're a security hole if passed unvalidated user input.

If you do not need shell features (such as variable expansion, wildcards, ...), never use shell=True. Then you don't need to do escaping yourself etc."""
