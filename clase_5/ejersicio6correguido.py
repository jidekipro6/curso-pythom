#Verano: Del 20 o 21 de diciembre al 20 o 21 de marzo. 1 -3
#Otoño: Del 20 o 21 de marzo al 20 o 21 de junio. 3-6 
#I#nvierno: Del 21 de junio al 23 de septiembre. 6 -8
#Primavera: Del 23 de septiembre al 21 de diciembre. 8 -12


print("\n\n\n<-------------------------------------------------------------->\n\n\n")
# 5. Estaciones del Año
# Dado un mes (1-12), indica a qué estación pertenece.
mes = int(input("Introduce un mes (1-12): "))


if mes >=1 and mes <=12:
    if mes>=1 and mes <=3:
        print("VERANO")
    elif mes >=4 and mes <=6 :
        print("OTOÑO")
    elif mes >=7 and mes <=8 :
        print("INVIERNO")
    elif mes >=9 and mes <=12 :
        print("PRIMAVERA")
else:
    print("NO EXISTE ESA ESTACION")

print("\n\n\n<-------------------------------------------------------------->\n\n\n")