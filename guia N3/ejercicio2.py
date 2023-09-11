"""Dentro de este mismo consultorio surge la idea de poder imprimirle junto con la receta el
próximo turno al paciente. Para ello te pedimos que modifiques el código anterior,
solicitando los datos necesarios para completar la resolución y subas esos cambios al
repositorio ya creado. Añade al word ya creado el nuevo análisis, diseño y codificación """

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

#función para buscar en el id de paciente y ver si tiene turnos pendientes
def buscar_turnos(id_paciente):
    turnos = [
        {
            "id": 1,
            "paciente": "IdDelPaciente",
            "fecha": "20/10/2021",
            "hora": "10:00"
        }
    ]
    for turno in turnos:
        if turno["paciente"] == id_paciente:
            print("Turno encontrado")
            print(f"ID del turno: {turno['id']}")
            print(f"Fecha del turno: {turno['fecha']}")
            print(f"Hora del turno: {turno['hora']}")
        else:
            print("Turnos no encontrados")

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
            print("Turnos: ")
            buscar_turnos(receta["paciente"])
        else:
            print("Receta no encontrada")
else:
    print("El numero ingresado no es valido")
    
    
    
    
    