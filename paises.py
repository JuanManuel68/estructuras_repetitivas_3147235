paises=[
    {
        "nombre" : "venezuela",
        "capital" : "caracas",
        "moneda" : "bolivar",
        "poblacion" : 
            {
              "censo" : 28,
              "desidad" : 31,
            },
        "ciudades" : 
            [
                "carabobo",
                "maracaibo",
                "valencia",
                "barquisimeto"
            ],
        "superficie" : 916.44
    },
    {
        "nombre" : "brasil",
        "capital" : "brasilia",
        "moneda" : "real",
        "poblacion" :
            {
            "censo" : 213,
            "desidad" : 25,
            },
        "ciudades" :
            [
                "rio de janeiro",
                "sao paulo",
                "belo horizonte",
                "porto alegre"
            ],
        "superficie" : 8.515767049
    },
    {
        "nombre" : "paraguay",
        "capital" : "asuncion",
        "moneda" : "guarani",
        "poblacion" : 
            {
            "censo" : 7,
            "desidad" : 3,
            },
        "ciudades" :
            [
                "ciudad del este",
                "luque",
                "pedro juan caballero"
            ],  
        "superficie" : 406752
    }
]
for pais in paises:  
    print("nombre:", pais["nombre"])
    print("capital:", pais["capital"])
    print("poblacion:")
    print("-censo:", pais["poblacion"]["censo"], "por km2")
    print("superficie:", pais["superficie"], "por km2")
    print("------------------------") 
    print("ciudades principales")
    for ciudad in pais["ciudades"]:
        print("-", ciudad)
    print("------------------------") 