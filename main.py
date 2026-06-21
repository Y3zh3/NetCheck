import csv
import requests

print("NETCHECK - Inventario desde API")

url = "https://jsonplaceholder.typicode.com/users"

try:
    respuesta = requests.get(url, timeout=10)

    if respuesta.status_code == 200:
        datos = respuesta.json()
        dispositivos = []

        for usuario in datos[:5]:
            dispositivo = {
                "nombre": "Equipo " + usuario["name"],
                "ip": usuario["address"]["geo"]["lat"],
                "estado": "Activo"
            }
            dispositivos.append(dispositivo)

        for dispositivo in dispositivos:
            print("\nNombre:", dispositivo["nombre"])
            print("IP:", dispositivo["ip"])
            print("Estado:", dispositivo["estado"])

        with open("inventario.csv", "w", newline="") as archivo:
            columnas = ["nombre", "ip", "estado"]
            escritor = csv.DictWriter(archivo, fieldnames=columnas)
            escritor.writeheader()
            escritor.writerows(dispositivos)

        print("\nArchivo inventario.csv actualizado correctamente.")

    else:
        print("Error al consultar la API:", respuesta.status_code)

except requests.exceptions.Timeout:
    print("Error: La API tardó demasiado en responder.")

except requests.exceptions.ConnectionError:
    print("Error: No hay conexión con la API.")

except requests.exceptions.RequestException as error:
    print("Error general al consultar la API:", error)