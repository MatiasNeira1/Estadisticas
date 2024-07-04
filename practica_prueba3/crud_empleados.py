import os
import json
import globales



def crear_empleado():
    os.system("cls")
    print("===CREAR USUARIO===")
    empleados=globales.leer_archivo_json('empleado.json')

    id_empleado=input("Ingrese ID de empleado que desea agregar: ")
    nombre=input("Ingrese nombre de empleado que desea agregar: ")
    apellido=input("Ingrese apellido de empleado que desea agregar: ")
    try:
        sueldo=input("Ingrese sueldo de empleado que desea agregar: ")
    except:
        sueldo=0
    id_cargo=input("Ingrese ID del cargo de empleado a agregar: ")


    empleado_nuevo={
        "id_empleado": id_empleado,
        "nombre": nombre,
        "apellido": apellido,
        "sueldo": sueldo,
        "id_cargo": id_cargo
    }

    empleados.append(empleado_nuevo)
    globales.guardar_archivo_json('empleado.json', empleados)



def actualizar_empleado():
    os.system("cls")
    print("===ACTUALIZAR DATOS===")
    empleados=globales.leer_archivo_json('empleado.json')


    id_empleado=input("Ingrese ID de empleado que desea actualizar: ")
    nombre=input("Ingrese nombre de empleado que desea actualizar: ")
    apellido=input("Ingrese apellido de empleado que desea actualizar: ")
    try:
        sueldo=input("Ingrese sueldo de empleado que desea actualizar: ")
    except:
        sueldo=0
    id_cargo=input("Ingrese ID del cargo de empleado a actualizar: ")



    for empleado in empleados:
        if empleado['id_empleado']==id_empleado:
            empleado['nombre']=nombre
            empleado['apellido']=apellido
            empleado['sueldo']=sueldo
            empleado['id_cargo']=id_cargo
            break
    globales.guardar_archivo_json('empleado.json', empleados)



def listar_empleados():
    os.system("cls")
    print("===LISTA DE DATOS===")
    empleados=globales.leer_archivo_json('empleado.json')

    for empleado in empleados:
        print(empleado)




def borrar_empleado():
    os.system("cls")
    print("===ELIMINAR DATOS===")
    empleados=globales.leer_archivo_json('empleados.json')


    id_empleado=input("Ingrese ID de empleado que desea eliminar: ")

    empleados_que_quedan=[]

    for empleado in empleados:
        if empleado['id_empleado']!=id_empleado:
            empleados_que_quedan.append(empleado)
    globales.guardar_archivo_json('empleado.json', empleados_que_quedan)





def menu_general():
    while True:
        os.system("cls")
        print("== EMPLEADOS ==")
        print("1. Crear         - Create")
        print("2. Actualizar    - Update")
        print("3. Listar        - Read")
        print("4. Borrar        - Delete")
        print("5. Salir")

        opcion=globales.seleccionar_opcion(5)

        if opcion==1:
            crear_empleado()
        elif opcion==2:
            actualizar_empleado()
        elif opcion==3:
            listar_empleados()
        elif opcion==4:
            borrar_empleado()
        elif opcion==5:
            print("Ha salido del menu")
            return
        
        input("Presione ENTER para continuar")
        

    
menu_general()