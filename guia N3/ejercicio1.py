""" 
    Hacer un sist para poder administrar las recetas que emiten los medicos a las personas que se atienden en un consultorio.
"""

recetas = [
    {
        "id": 1,
        "paciente": "IdDelPaciente",
        "medicamentos": [
            {
                "id": 1,
                "nombre": "Paracetamol",
                "cantidad": 1,
                "dosis": "10mg cada 8hs"
            }
        ]   
    }
]

id_de_receta = int(input("Ingrese el numero de la receta: "))
#Hacer validación para que pertenezca a un numero y sea distinto de 0 y positivo para empezar a buscar
if id_de_receta > 0:
    for receta in recetas:
        if receta["id"] == id_de_receta:
            print("Receta encontrada")
            print(f"ID de la receta: {receta['id']}")
            print(f"ID del paciente: {receta['paciente']}")
            print("Medicamentos: ")
            for medicamento in receta["medicamentos"]:
                print(f"ID: {medicamento['id']}")
                print(f"Nombre: {medicamento['nombre']}")
                print(f"Cantidad: {medicamento['cantidad']}")
                print(f"Dosis: {medicamento['dosis']}")
        else:
            print("Receta no encontrada")
else:
    print("El numero ingresado no es valido")
    
    