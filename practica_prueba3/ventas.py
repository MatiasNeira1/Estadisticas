import globales
import json
import os
import random
import math


def precargar_ventas():
    ventas=globales.leer_archivo_json('ventas.json')
    empleados=globales.leer_archivo_json('empleado.json')

    id_venta=1

    for i in range(10):
        empleado=random.choice(empleados)

        id_venta+=1
        id_empleado=empleado['id_empleado']
        total_venta=random.randint(30000,70000)
        propina=total_venta*0.1

        nueva_venta_aleatoria={
        "id_venta": id_venta,
        "id_empleado": id_empleado,
        "total_venta": total_venta,
        "propina": propina
    
        }
    
        ventas.append(nueva_venta_aleatoria)
    globales.guardar_archivo_json('ventas.json', ventas)


def crear_venta():
    os.system("cls")
    print("===CREAR VENTA===")
    ventas=globales.leer_archivo_json('ventas.json')

    id_venta=input("Ingrese ID de venta nueva: ")
    id_empleado=input("Ingrese ID de empleado que realza venta: ")
    try:
        total_venta=int(input("Ingrese el total de la venta: "))
    except:
        total_venta=0
    
    propina=total_venta*0.1
   
    


    nueva_venta={
        "id_venta": id_venta,
        "id_empleado": id_empleado,
        "total_venta": total_venta,
        "propina": propina
    
        }
    

    ventas.append(nueva_venta)
    globales.guardar_archivo_json('ventas.json', ventas)


def reporte_sueldos():
   
    empleados=globales.leer_archivo_json('empleado.json')

    for empleado in empleados:
        sueldo_bruto=float(empleado['sueldo'])

        afp=  sueldo_bruto* 0.07
        salud= sueldo_bruto* 0.12

        sueldo_liquido=sueldo_bruto - afp - salud

        print(f"ID_empleado:{empleado['id_empleado']}")
        print(f"Nombre empleado:{empleado['nombre']} {empleado['apellido']}")
        print(f"Sueldo Bruto: ${sueldo_bruto}")
        print(f"Descuento AFP: ${afp}")
        print(f"Descuento salud: ${salud}")
        print(f"Sueldo Liquido:{sueldo_liquido}")
        print("="*45)
        

    
def cinco_ventas_mas_altas():
    ventas=globales.leer_archivo_json('ventas.json')
    empleados=globales.leer_archivo_json('empleado.json')

    ventas_ordenadas=sorted(ventas, key=lambda x: x['total_venta'], reverse=True)
    print("id_venta | nombre | total venta")

    for venta in ventas_ordenadas[:5]:
        nombre_empleado=""
        for empleado in empleados:
            if empleado['id_empleado']== venta['id_empleado']:
                nombre_empleado=f"{empleado['nombre']} {empleado['apellido']} {empleado['id_cargo']}"

                print(f"{venta['id_venta']} {nombre_empleado} {venta['total_venta']}")


def cinco_ventas_mas_bajas():
    ventas=globales.leer_archivo_json('ventas.json')
    empleados=globales.leer_archivo_json('empleado.json')

    ventas_ordenadas=sorted(ventas, key=lambda x: x['total_venta'], reverse=False)
    print("id_venta | nombre | total venta")

    for venta in ventas_ordenadas[:5]:
        nombre_empleado=""
        for empleado in empleados:
            if empleado['id_empleado']== venta['id_empleado']:
                nombre_empleado=f"{empleado['nombre']} {empleado['apellido']} {empleado['id_cargo']}"

                print(f"{venta['id_venta']} {nombre_empleado} {venta['total_venta']}")


def media_geometrica():
    ventas=globales.leer_archivo_json('ventas.json')

    suma_ventas=0
    cantidad_ventas=0

    for venta in ventas:
        suma_ventas+=math.log(venta['total_venta'])

        cantidad_ventas+=1

        media_geometrica=math.exp(suma_ventas / cantidad_ventas)

    print(f"La media geometrica de las ventas es: {int(media_geometrica)}")


# def promedio_ventas():
    

def menu_estadisica():
    while True:
        os.system("cls")
        print("1. Ventas mas altas")
        print("2. Ventas mas bajas")
        print("3. Media geometrica")
        print("4. Promedio de ventas")

        opcion = globales.seleccionar_opcion(4)

        if opcion == 1:
            cinco_ventas_mas_altas()
             
        elif opcion == 2:
            cinco_ventas_mas_bajas()
        elif opcion == 3:
            media_geometrica()
        elif opcion==4:
            input()
            # promedio_ventas()

        input("Presiona ENTER para continuar")
        return







def menu_general():
    while True:
        os.system("cls")
        print("1. Precargar ventas")
        print("2. Crear Venta")
        print("3. Reporte de sueldos")
        print("4. Estadisticas")
        print("5. Salir")

        opcion = globales.seleccionar_opcion(4)

        if opcion == 1:

            precargar_ventas()
        elif opcion == 2:
            crear_venta()
        elif opcion == 3:
            reporte_sueldos()
        elif opcion == 4:
            menu_estadisica()
       
        elif opcion == 5:
            print("5. Salir")
            return

        input("Presiona ENTER para continuar")



menu_general()
