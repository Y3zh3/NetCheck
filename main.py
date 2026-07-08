import requests
import csv

URL_API = "https://6a4da947e1cf82a4a17e7870.mockapi.io/api/v1/dispositivos"

def obtener_dispositivos():
    try:
        respuesta = requests.get(URL_API, timeout=10)
        respuesta.raise_for_status()
        dispositivos = respuesta.json()
        return dispositivos
    except Exception as error:
        print("Error al consultar la API:", error)
        return []

def guardar_csv(dispositivos):
    with open("inventario.csv", "w", newline="") as archivo:
        columnas = ["id", "nombre", "ip", "estado"]
        escritor = csv.DictWriter(archivo, fieldnames=columnas)
        escritor.writeheader()
        escritor.writerows(dispositivos)
    print("\nArchivo inventario.csv actualizado correctamente.")

def mostrar_inventario(dispositivos):
    activos = 0
    inactivos = 0
    print("\nNETCHECK - Inventario de dispositivos\n")
    
    for dispositivo in dispositivos:
        print("ID:", dispositivo.get("id"))
        print("Nombre:", dispositivo.get("nombre"))
        print("IP:", dispositivo.get("ip"))
        print("Estado:", dispositivo.get("estado"))

        if dispositivo.get("estado") == "Inactivo":
            inactivos += 1
            print("ALERTA: Este dispositivo necesita revisión.")
        else:
            activos += 1
        print("-" * 30)

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