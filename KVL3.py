Vin=float(input("enter the input voltage value= "))
R1=float(input("enter the resistance R1 value= "))
R2=float(input("enter the resistance R2 value= "))
R3=float (input("enter the resistance R3 value= "))
RT=float(R1+R2+R3)
Req= print("equivalent resistance:  ",RT,"ohm")
I= Vin/RT
print("total current:",I,"amps")
v1=I*R1
v2=I*R2
v3=I*R3
v11=print("voltage across R1 i.e v1:",v1,"volts")
v21=print("voltage across R2 i.e v2:",v2,"volts")
v31=print("voltage across R3 i.e v3:",v3,"volts")
Vout=float(v1+v2+v3)
vo= print("total voltage",Vout,"volts")
if (Vin==Vout):
    print("kvl is verified for given circuit")
else:
    print("kvl is not verified for given circuit")
        
