import requests
import csv

URL_API = "https://jsonplaceholder.typicode.com/users"

def obtener_dispositivos():
    try:
        respuesta = requests.get(URL_API, timeout=10)
        respuesta.raise_for_status()

        datos = respuesta.json()
        dispositivos = []

        for usuario in datos[:5]:
            dispositivo = {
                "nombre": "Equipo " + usuario["name"],
                "ip": f"192.168.1.{usuario['id'] + 10}",
                "estado": "Inactivo" if usuario["id"] % 3 == 0 else "Activo"
            }
            dispositivos.append(dispositivo)

        return dispositivos

    except requests.exceptions.Timeout:
        print("Error: La consulta a la API demoró demasiado.")
    except requests.exceptions.ConnectionError:
        print("Error: No se pudo conectar con la API.")
    except requests.exceptions.RequestException as error:
        print("Error al consultar la API:", error)

    return []


def guardar_csv(dispositivos):
    with open("inventario.csv", "w", newline="") as archivo:
        columnas = ["nombre", "ip", "estado"]
        escritor = csv.DictWriter(archivo, fieldnames=columnas)

        escritor.writeheader()
        escritor.writerows(dispositivos)

    print("\nArchivo inventario.csv actualizado correctamente.")


def mostrar_inventario(dispositivos):
    activos = 0
    inactivos = 0

    print("NETCHECK - Inventario de dispositivos\n")

    for dispositivo in dispositivos:
        print("Nombre:", dispositivo["nombre"])
        print("IP:", dispositivo["ip"])
        print("Estado:", dispositivo["estado"])

        if dispositivo["estado"] == "Inactivo":
            inactivos += 1
            print("ALERTA: Este dispositivo necesita revisión.")
        else:
            activos += 1

        print()

    print("RESUMEN")
    print("Total de dispositivos:", len(dispositivos))
    print("Activos:", activos)
    print("Inactivos:", inactivos)


def main():
    dispositivos = obtener_dispositivos()

    if dispositivos:
        mostrar_inventario(dispositivos)
        guardar_csv(dispositivos)
    else:
        print("No se encontraron dispositivos para procesar.")


if __name__ == "__main__":
    main()