#ciclo for
#Especial para recorrer
#Estructuras de datos
#Todo lo que esta entre [] se denomina lista

#funcion range(python)
#crea una lista de numeros, en el rango definido por el usuario
#ejecicio 1
#Imprimir la tabla de multiplicar de un numero que el ususario ingrese por teclado, utilizando un ciclo for

numero= int(input("Ingrese un numero: "))
for i in range(1,11):
    result = numero*i
    print( numero, "x" , i, "=" , result )
