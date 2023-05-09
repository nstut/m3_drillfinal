nombres = ["Harry Houdini", "Newton", "David Blaine", "Hawking", "Messi", "Teller", "Einstein", "Pele", "Juanes"]
magos = ["Harry Houdini","David Blaine","Teller"]
cientificos = ["Newton", "Hawking", "Einstein"]
otros = nombres[:]

for i in nombres:
    if i in magos or i in cientificos:
        otros.remove(i)

def hacer_grandioso(magos):
    aux = []
    for x in magos:
         aux.append("El gran " + x)
    return aux

magos = hacer_grandioso(magos)   
    
def imprimir_nombres(nombres):
    print("Los nombres originales son:", nombres)

mostrar = imprimir_nombres(nombres)
print ("Los primeros son los magos:", magos, "\n"
       "Los siguientes son los cientificos:", cientificos, "\n" 
        "y estos son los restantes:", otros)
