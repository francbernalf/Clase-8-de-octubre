A = float(input("Ingrese el valor de A:"))
B = float(input("Ingrese el valor de B:"))
C = float(input("Ingrese el valor de C:"))

if(A>B>C):
    print("El orden es",C,B,A)
elif (A>C>B):
    print("El orden es",B,C,A)
elif (C>B>A):
    print("El orden es",A,B,C)
elif (C>A>B):
    print("El orden es",B,A,C)
elif (B>A>C):
    print("El orden es",C,A,B)
else:
    print("El orden es",A,C,B)
    
    