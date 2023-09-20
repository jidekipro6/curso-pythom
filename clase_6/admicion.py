#si intenta un alumno ingresar mas de 4 veces ya no podra postular
intento=0
while intento<=4:
    nota=int(input("ingrese su nota :"))
    intento+=1
    if nota>=14:
        print("INGRESASTE y lo lograste en el intento ",intento)
        break 
else:
    print("ESPERO OTRO AÑO PARA POSTULAR")
    