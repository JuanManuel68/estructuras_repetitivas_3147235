#ejecicio 1
#Imprimir la tabla de multiplicar de un numero que el ususario ingrese por teclado, utilizando un ciclo while 
#variable contadora
numero= int(input("Ingrese un numero: "))
i=10
while i>=1:
    result = numero*i
    print( numero, "x" , i, "=" , result ) 
    i=i-1