import csv

print("NETCHECK - Inventario de dispositivos")

dispositivos = [
    {"nombre": "Router Principal", "ip": "192.168.1.1", "estado": "Activo"},
    {"nombre": "Switch Oficina", "ip": "192.168.1.2", "estado": "Inactivo"},
    {"nombre": "Access Point Aula", "ip": "192.168.1.3", "estado": "Activo"}
]

activos = 0
inactivos = 0

for dispositivo in dispositivos:
    print("\nNombre:", dispositivo["nombre"])
    print("IP:", dispositivo["ip"])
    print("Estado:", dispositivo["estado"])

    if dispositivo["estado"] == "Activo":
        activos += 1
    else:
        inactivos += 1
        print("ALERTA: Este dispositivo necesita revisión.")

print("\nRESUMEN")
print("Total de dispositivos:", len(dispositivos))
print("Activos:", activos)
print("Inactivos:", inactivos)

with open("inventario.csv", "w", newline="") as archivo:
    columnas = ["nombre", "ip", "estado"]
    escritor = csv.DictWriter(archivo, fieldnames=columnas)
    escritor.writeheader()
    escritor.writerows(dispositivos)

print("\nArchivo inventario.csv creado correctamente.")