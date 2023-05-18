#Proyecto Final Introduccion a la Programacion
#Grupo 7

#Integrantes:
#-Alejandro Saenz Ponce
#-Diego Solis Mendez
#-Cinthia Selva Duarte

#Menu

paciente=[]
medicos=[]
cancel_o_repro=[]

def autenticarusuario():
    
    opc_menu=0
    print()
    while opc_menu!=7 and opc_menu<7:
        print("Menú")
        print("1 = Módulo de Registro de Médico")
        print("2 = Módulo de Registro de Paciente")
        print("3 = Módulo de Registro de Cita")
        print("4 = Módulo de Cancelación y/o Reprogramación de Cita")
        print("5 = Módulo de Pago y Facturacion")
        print("6 = Módulo de Reportes")
        print("7 = Salir")
        opc_menu=int(input("Seleccione una opción..."))
        print()
        if opc_menu==1:
            modulo1()
            print()
        elif opc_menu==2:
            modulo2()
            print()
        elif opc_menu==3:
            modulo3()
            print()
        elif opc_menu==4:
            modulo4()
            print()
        elif opc_menu==5:
            modulo5()
            print()
        elif opc_menu==6:
            modulo6()
            print()
        else:

            print("Cerrando Módulos")
            print("¡Usted ha salido del programa!")

#1

def modulo1():
    print("Bienvenid@ al Módulo de Registro de Médico")
    
    cantidad=int(input("Ingrese la cantidad de médicos que desea registrar: "))

    for i in range(cantidad):
        nombre=input("Ingrese el nombre del médico: ")
        especialidad=input("Ingrese la especialidad del médico: ")
        correo=input("Ingrese el correo electrónico del médico: ")
        telefono=input("Ingrese el número de teléfono del médico: ")
        horario=input("Ingrese el horario de disponibilidad del médico (solo un dia, minusculas): ")

        medicos.append({"Nombre": nombre, "Especialidad": especialidad, "Correo": correo, "Teléfono": telefono, "Horario": horario})

    print("La información de los médicos registrados es la siguiente:")
    for medico in medicos:
        print("Nombre:", medico["Nombre"])
        print("Especialidad:", medico["Especialidad"])
        print("Correo:", medico["Correo"])
        print("Teléfono:", medico["Teléfono"])
        print("Horario:", medico["Horario"])
        print()
        
    print("Regresando al menú principal...")

#2

def modulo2():
    print("Bienvenid@ al Módulo de Registro de Paciente (solo se permite registrar un paciente por sesion)")

    nombre=input("Ingrese el nombre del paciente: ")
    paciente.append(nombre)

    edad=int(input("Ingrese la edad del paciente: "))
    paciente.append(edad)

    sexo=input("Ingrese el sexo del paciente: ")
    paciente.append(sexo)

    correo=input("Ingrese el correo del paciente: ")
    paciente.append(correo)

    direccion=input("Ingrese la dirección del paciente: ")
    paciente.append(direccion)

    telefono=input("Ingrese el número de teléfono del paciente: ")
    paciente.append(telefono)

    medico=input("Ingrese el nombre del médico que lo atenderá: ")
    paciente.append(medico)

    dia=input("Ingrese el dia de la cita: ")
    paciente.append(dia)

    print("La información del paciente es la siguiente:")
    print("Nombre: ", paciente[0])
    print("Edad: ", paciente[1])
    print("Sexo: ", paciente[2])
    print("Correo electrónico: ", paciente[3])
    print("Dirección: ", paciente[4])
    print("Número de teléfono: ", paciente[5])
    print("Médico que lo atenderá: ", paciente[6])
    print("Día de la cita: ", paciente[7])
    print()
    
    print("Regresando al menú principal...")
    
#3

def modulo3():
    print("Bienvenid@ al Módulo de Registro de Cita")
    
    dia=input("Ingrese el día para la cita (minusculas): ")
    especialidad=input("Ingrese la especialidad del médico: ")
    
    medicos_especialidad=[]
    for medico in medicos:
        if medico["Especialidad"]==especialidad:
            medicos_especialidad.append(medico)
    
    medicos_disponibles=[]
    for medico in medicos_especialidad:
        if medico["Horario"]==dia:
            medicos_disponibles.append(medico)

    if len(medicos_disponibles)==0:
        print("Lo sentimos, no hay médicos disponibles en el día solicitado.")
    else:
        print("Los siguientes médicos están disponibles en el día solicitado:")
        for i in range(len(medicos_disponibles)):
            print(f"{i}. ({medico['Nombre']}) ({medico['Horario']})")
        seleccion=int(input("Ingrese el número del médico que desea seleccionar: "))
        
        print("La cita se ha registrado correctamente:")
        print("Paciente:", paciente[0])
        print("Médico:", medico["Nombre"])
        print("Día:", medico["Horario"])

    print()
    print("Regresando al menú principal...")

#4

def modulo4():
    print("Bienvenid@ al Módulo de Cancelación y/o Reprogramación de Cita")

    reprogramar=input("¿Desea reprogramar su cita? (s/n): ")
    if reprogramar=="s":
        dia_nuevo=input("Ingrese el nuevo día en que desea programar su cita: ")
        medicos_disponibles=[]
        for medico in medicos:
            if medico["Horario"]==dia_nuevo:
                medicos_disponibles.append(medico)

        if medicos_disponibles:
            print("Los siguientes médicos están disponibles en el nuevo día solicitado:")
            for medico in medicos_disponibles:
                print("-",medico["Nombre"])

            medico_nuevo = input("Ingrese el nombre del médico que desea seleccionar: ")
            for medico in medicos_disponibles:
                if medico["Nombre"]==medico_nuevo:
                    paciente.pop(7)
                    paciente.pop(6)
                    paciente.append(medico_nuevo)                  
                    paciente.append(dia_nuevo)
                    print("La cita ha sido reprogramada correctamente:")
                    print("Paciente:", paciente[0])
                    print("Médico:", paciente[6])
                    print("Día:", paciente[7])
                    cancel_o_repro.append(1)
                    break
            else:
                print("El médico ingresado no se encuentra disponible en el nuevo día.")
        else:
            print("No hay médicos disponibles en el nuevo día ingresado.")
    else:
        paciente.pop(7)
        cancel_o_repro.append(1)
        print("La cita ha sido cancelada correctamente.")
        
    print()
    print("Regresando al menú principal...")
    
#5

def modulo5():
    print("Bienvenid@ al Módulo de Pago y Facturacion")

    tratamientos={"Limpieza": 50000, "Extracción": 80000, "Empaste": 120000, "Ortodoncia": 500000}

    print("Tratamientos dentales disponibles")
    print("20% de descuento en todos los tratamientos por tiempo limitado):")
    for tratamiento, precio in tratamientos.items():
        print(f"-{tratamiento}: ₡{precio}")

    tratamiento_elegido=input("Elija un tratamiento dental: (primer letra mayuscula)")

    if tratamiento_elegido not in tratamientos:
        print("Tratamiento no válido.")
    else:
        subtotal=tratamientos[tratamiento_elegido]*0.8
        iva=tratamientos[tratamiento_elegido]*0.12
        precio_final=subtotal+iva
        
        print("Contamos con las siguientes formas de pago:")
        print("-Efectivo")
        print("-Sinpe Movil")
        print("-Tarjeta de debito")
        print("-Tarjeta de credito")
        formadepago=input("Digite su forma de pago: ")

        precio_og=tratamientos[tratamiento_elegido]

        print(f"El subtotal del tratamiento es: ₡{subtotal}, y su forma de pago es:", formadepago)

        input("Presione enter para ver su factura")
        print()

        print("********************************************")
        print("*            FACTURA DE SERVICIO           *")
        print("********************************************")
        print("Clinica de atencion: Consultorio Dental Dientitos")
        print("Especialidad: Odontologia")
        print(f"Moneda: Colon")
        print(f"Nombre del paciente:",paciente[0])
        print(f"Servicio: Tratamiento dental")
        print(f"Cantidad: 1")
        print(f"Precio: ₡{precio_og}")
        print("Detalle: ")
        print("Tratamiento: ",tratamiento_elegido)
        print(f"Subtotal: ₡{subtotal}")
        print(f"Descuento: 20%")
        print(f"IVA: ₡{iva}")
        print(f"Total General: ₡{precio_final}")
        
        print()
        input("Presione enter para terminar de revisar la factura")

    print()
    print("Regresando al menú principal...")

#6

def modulo6():
    print("Bienvenid@ al Módulo de Reportes")
    print("Citas Programadas")
    print("-Dia de cita:",paciente[7])
    print()
    print("Cancelaciones y/o reprogramaciones")
    for i in range(len(cancel_o_repro)):
        mod4=len(cancel_o_repro)
        print("-",mod4)
        print()
    print("Medicos:")
    for medico in medicos:
        print("-Nombre", medico["Nombre"])
        print("-Horario", medico["Horario"])
        print()
    print()
    print("Tratamientos Orales:")
    print("-Ortodoncia")
    print("-Blanqueamiento")
    print("-Cirugias")
    print("-Coronas")
    print("-Implantes")
    
    print()
    print("Regresando al menú principal...")


#Pantalla de bloqueo

print("Bienvenid@ al Consultorio Dental Dientitos")

intentos=0

while intentos<3:
    us=input("¡Ingrese su usuario por favor! (nota: usar solo minúsuculas): ")
    clave=input("¡Ingrese su contraseña por favor! ")
    if us=="admin" and clave=="1234":
        autenticarusuario()
        break
    else:
        intentos+=1
        print("¡Usuario y/o contraseña incorrecta!")
        print("Intente de nuevo")
        
if intentos==3:
    print("¡Su usuario ha sido bloqueado, por favor contacte a soporte técnico!")
