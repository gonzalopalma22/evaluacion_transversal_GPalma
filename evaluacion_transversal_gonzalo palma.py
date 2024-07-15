import random
import csv

trabajadores = ["Juan Pérez”,”María García”,”Carlos López”,”Ana Martínez”,”Pedro Rodríguez”,”Laura Hernández”,”Miguel Sánchez”,”Isabel Gómez”,”Francisco Díaz”,”Elena Fernández"]


sueldos = [random.randint(300000, 2500000) for _ in range(10)]


def asignar_sueldos_aleatorios():
    global sueldos
    sueldos = [random.randint(300000, 2500000) for _ in range(10)]

def clasificar_sueldos():
    menor_a_800k = []
    entre_800k_2m = []
    mayor_a_2m = []

    for i in range(len(trabajadores)):
        nombre = trabajadores[i]
        sueldo = sueldos[i]

        if sueldo < 800000:
            menor_a_800k.append((nombre, sueldo))
        elif sueldo <= 2000000:
            entre_800k_2m.append((nombre, sueldo))
        else:
            mayor_a_2m.append((nombre, sueldo))

    print("Sueldos menores a $800.000\nTOTAL:", len(menor_800k))
    for nombre, sueldo in menor_a_800k:
        print(nombre, "$", sueldo)

    print("\nSueldos entre $800.000 y $2.000.000\nTOTAL:", len(entre_800k_2m))
    for nombre, sueldo in entre_800k_2m:
        print(nombre, "$", sueldo)

    print("\nSueldos superiores a $2.000.000\nTOTAL:", len(mayor_a_2m))
    for nombre, sueldo in mayor_a_2m:
        print(nombre, "$", sueldo)

    print("\nTOTAL SUELDOS: $", sum(sueldos))

def ver_estadisticas():
    sueldo_mas_alto = max(sueldos)
    sueldo_mas_bajo = min(sueldos)
    promedio_sueldos = sum(sueldos) / len(sueldos)

    from math import prod
    media_geom = prod(sueldos) ** (1 / len(sueldos))

    print("Sueldo más alto:", sueldo_mas_alto)
    print("Sueldo más bajo:", sueldo_mas_bajo)
    print("Promedio de sueldos:", promedio_sueldos)
    print("Media geométrica:", media_geom)

def asignar_sueldos_aleatorios():
    global sueldos
    sueldos = [random.randint(300000, 2500000) for _ in range(10)]

def clasificar_sueldos():
    menor_800k = []
    entre_800k_2m = []
    mayor_a_2m = []

    for i in range(len(trabajadores)):
        nombre = trabajadores[i]
        sueldo = sueldos[i]

        if sueldo < 800000:
            menor_800k.append((nombre, sueldo))
        elif sueldo <= 2000000:
            entre_800k_2m.append((nombre, sueldo))
        else:
            mayor_a_2m.append((nombre, sueldo))

    print("Sueldos menores a $800.000\nTOTAL:", len(menor_800k))
    for nombre, sueldo in menor_800k:
        print(nombre, "$", sueldo)

    print("\nSueldos entre $800.000 y $2.000.000\nTOTAL:", len(entre_800k_2m))
    for nombre, sueldo in entre_800k_2m:
        print(nombre, "$", sueldo)

    print("\nSueldos superiores a $2.000.000\nTOTAL:", len(mayor_a_2m))
    for nombre, sueldo in mayor_a_2m:
        print(nombre, "$", sueldo)

    print("\nTOTAL SUELDOS: $", sum(sueldos))

def ver_estadisticas():
    sueldo_mas_alto = max(sueldos)
    sueldo_mas_bajo = min(sueldos)
    promedio_sueldos = sum(sueldos) / len(sueldos)

    from math import prod
    media_geom = prod(sueldos) ** (1 / len(sueldos))

    print("Sueldo más alto:", sueldo_mas_alto)
    print("Sueldo más bajo:", sueldo_mas_bajo)
    print("Promedio de sueldos:", promedio_sueldos)
    print("Media geométrica:", media_geom)

def reporte_sueldos():
    with open('data.csv', 'w') as file:
        file.write("Nombre empleado, Sueldo Base, Descuento Salud, Descuento AFP, Sueldo Líquido\n")
        for i in range(len(trabajadores)):
            nombre = trabajadores[i]
            sueldo = sueldos[i]
            desc_salud = sueldo * 0.07
            desc_afp = sueldo * 0.12
            sueldo_liquido = sueldo - desc_salud - desc_afp
            file.write(f"{nombre}, {sueldo}, {desc_salud}, {desc_afp}, {sueldo_liquido}\n")
    print("Reporte de sueldos generado correctamente en 'data.csv'.")

while True:
    print("\n===== Menú =====")
    print("1. Asignar sueldos aleatorios")
    print("2. Clasificar sueldos")
    print("3. Ver estadísticas")
    print("4. Reporte de sueldos")
    print("5. Salir del programa")
    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        asignar_sueldos_aleatorios()
    elif opcion == '2':
        clasificar_sueldos()
    elif opcion == '3':
        ver_estadisticas()
    elif opcion == '4':
        reporte_sueldos()
    elif opcion == '5':
        print("Finalizando el programa..\nDesarrollado por Gonzalo Palma\nRUT 19.669.511-7")
        break
    else:
        print("Opción no válida. Por favor, seleccione nuevamente.")
