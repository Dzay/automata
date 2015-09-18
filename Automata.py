__author__ = 'ING26'
#----------------------------Lectura y armado del automata-------------------------------

text_file = open("Automata.txt", "r")
list = text_file.read().splitlines()#Lee el archivo Automata.txt y guarda los datos en un
                                    #arreglo (list)

# 
q =         list[0].split(" ")     #Lista de estados
sigma =     list[1].split(" ")     #Alfabeto del lenguaje
inicio =    list[2].split(" ")[0]  #Estado de inicio
finales =   list[3].split(" ")     #Estados finales
temporal =  list[4].split(" ")     #Lista temporal para guardar las transiciones del automata
transiciones = []

for tran in temporal:
    transiciones.append(tran.split("-")) #Conjunto de transiciones del automata

#-----------------------------Finaliza la lectura y armado del automata------------------


palabras=["AB","AA","AAA","AAAA","ABBA"] #Conjunto de cadenas que va a evaluar el automata


#----------------------------Evaluacion de las cadenas-----------------------------------

estadoActual=inicio
text_file.close()
estados=len(q)
lensigma=len(sigma)
for palabra in palabras:
    for char in palabra:
        if char in sigma:
            for i in range(lensigma*estados):
                if transiciones[i][0]==estadoActual:
                    if transiciones[i][1]==char:
                        estadoActual=transiciones[i][2]
                        break
        else:
            estadoActual=""
            break
    
    if estadoActual in finales:
        print("La cadena "+palabra+" SI es aceptada")
    else:
        print("La cadena "+palabra+" NO es aceptada")
    estadoActual=inicio

#--------------------------Fin de la evaluacion de las cadenas---------------------------

#--------------------------Generacion de Grafico del automata----------------------------
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

#--------------------Fin de la generacion del Grafico del automata-----------------------

