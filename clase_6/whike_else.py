intento=1
while intento<=3:
    contraseña=int(input("Intruduce tu contraseña  :"))
    
    if contraseña==1234:
        
        print("Genial , Bienvenido""NrIntento",intento)
        
        break
    intento+=1
   
else :
    print("MUCHOS INTENTOS INTENTELO MAS TARDE")
