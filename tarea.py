partido_rojo=""
eleccion=""
dpi=0
partido=""
partido_azul=""
rojo=""
verde=""
naranja=""
azul=""
dpi=(input("ingrese su dpi:"))
if len (dpi)<13:
    print("el numero de digitos no es valido")
if len (dpi)>13:
    print("no valido")

if len(dpi)==13:
    print("valido")
    print("opciones presidenciales: ")
    print("partido rojo")
    print("partido azul")
    eleccion= input("seleccione el partido que desea: ")
    if eleccion== "rojo":
        print("su eleccion es rojo")
    elif eleccion== "azul":
        print("su eleccion es azul")
    elif eleccion== "nulo":
        print("su voto ha sido nulo")
    else:
        print("voto invalido")


alcaldia=""
confirmacion=""
resumen=""
print("partido rojo")
print("partido azul")
print("partido verde")
print("partido naranja")
alcaldia= input("seleccione el partido que votara para la alcaldia de Guatemala: ")
if alcaldia== "partido rojo":
    print("Su voto ha ido para el partido rojo")
elif alcaldia== "partido azul":
    print("su voto ha ido para el partido azul")
elif alcaldia== "partido verde":
    print("su voto ha ido para el paertido verde")
elif alcaldia== "partido naranja":
    print("su voto ha ido para el partido naranja")

else:
    print("voto no valido")
    alcaldia= "invalido"

if alcaldia !="invalido" and eleccion !="invalido":
    confirmacion= input("Quiere confirmar su voto?")
    if confirmacion == "si":
        print("su voto ha sido confirmado")

else:
    print("no se guardaron sus votos")