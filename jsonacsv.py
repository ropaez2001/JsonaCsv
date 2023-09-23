import json

Datos={} # creo la variable datos de tipo diccionario
Datos["Clientes"]=[]  # dento de datos que es un diccionario creo una lista
Datos["Clientes"].append({ "Nombre": "Roberto",
                        "Apellido":"Paez",
                        "Edad":53
                        })
Datos["Clientes"].append({ "Nombre": "Alejandro" ,
                            "Apellido": "Rodriguez",
                            "Edad": 50 })
Datos["Clientes"].append({ "Nombre": "Elena" ,
                            "Apellido": "Perz",
                            "Edad": 49 })
Datos["Clientes"].append({ "Nombre": "Maria" ,
                            "Apellido": "Rossi",
                            "Edad": 35 })

with open("Datos.json", "w") as file:
    json.dump(Datos,file, indent=4)
    
import json
import csv

# Leer el archivo JSON
with open("Datos.json", "r") as json_file:
    data = json.load(json_file)

# Obtener la lista de clientes del diccionario
clientes = data.get("Clientes", [])

# Crear un archivo CSV y escribir los datos en él con espacio como delimitador
with open("Clientes.csv", "w", newline="") as csv_file:
    # Usar un tabulador como delimitador personalizado
    csv = csv.writer(csv_file)

    # Escribir los encabezados
    csv.writerow(["Nombre", "Apellido", "Edad"])

    # Usar un bucle for  para iterar sobre la lista de clientes sobre cada fila
    for fila in range(len(clientes)):
        cliente = clientes[fila]
        csv.writerow([cliente["Nombre"], cliente["Apellido"], cliente["Edad"]])

print("Se ha convertido el archivo JSON a CSV con éxito con espacio como delimitador.")