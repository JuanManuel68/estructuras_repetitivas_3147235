#diccionario 
#es una coleccion de datos que los almacena en pares
#clave-valor
#-un diccionario comienza y termina con llaves (curly braces)
#-la clave se separa del valor por dos puntos (:)
#-cada clave es un string
#-el valor puede ser de cualquier tipo
#-cada elemento (propiedad) del diccionario se separa
#por una coma (,)

#ejemplo: diccionario 
#que almacene los datos de un pais 

pais1={
    "nombre": "argentina",
    "capital": "ciudad autonoma de buenos aires",
    "moneda" : "peso argentino",
    "ciudades" : [
        "cordoba",
        "mendoza",
        "rosario",
        "mar del plata",
        "la plata"
    ],
    "poblacion" : {
        "censo": 46,
        "densidad": 16
        }
    }

pais2={
    "nombre": "ecuador",
    "capital": "quito",
    "moneda" : "dolar estadounidense",
    "ciudades" : [
        "guayaquil",
        "cuenca",
        "manta",
        "ambato",
        "loja"
        ],
    "poblacion" : {
        "censo" : 18,
        "desidad" : 29
    }
}

pais3={
    "nombre": "paraguay",
    "capital": "asuncion",
    "moneda" : "guarani",
    "ciudades" : [
        "ciudad del este",
        "luque",
        "capiata",
        "san bernardo",
        "pedro juan caballero"
        ],
    "poblacion" : {
        "censo" : 7,
        "desidad" : 3
    }
}
#acceder a la informacion del pais 

print(pais1["nombre"])
print(pais1["capital"])
#acceder a una ciudad del pais
print(pais1["ciudades"][0])
print("-------------")
#iterar las ciudades del pais 1
for ciudad in pais1["ciudades"]:
    print(ciudad)
print("-------------------------------")
#acceder a datos poblacionales
print("censo:", pais1["poblacion"]["censo"], "millones de habitantes")
print("censo:", pais1["poblacion"]["densidad"], "por km2")
print("-------------------------------")
