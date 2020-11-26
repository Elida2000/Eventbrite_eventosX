from event_logic import EventLogic
from categoriaEventos_logic import CategoriaEventLogic
from tipoEventos_logic import TipoEventLogic
from prettytable import PrettyTable
import datetime

while True:
    print("Bienvenido al menu de eventos\n")
    opcion = int(input("Inserte '0' para salir, '1' para ingresar un nuevo evento, '2' para actualizar un evento, '3' para remover un evento, '4' para ver todos los eventos o '5' para ver un evento por ID: "))
    print("------------------------------------------------------------------------------------------------------------------")
    if opcion == 0:
        break

    elif opcion == 1:
        print("Puede comenzar a ingresar datos:\n")
        idUsuarios = int(input("idUsuario: "))
        nombre = input("Nombre: ")
        print("Lista de categorías disponibles para eventos: ")
        catEventObj = CategoriaEventLogic()
        for element in catEventObj.getCat():
            print(str(element["idCategorias-eventos"])+"-"+element["nombreCat"])
        categoria = (input("Seleccione la categoria a la que pertenece su evento según el número correspondiente: "))
        fecha1 = input("fecha (YYYY-MM-DD): ")
        fecha = datetime.datetime.strptime(fecha1, "%Y-%m-%d")
        hora1 = input("Hora (HH:MM): ")
        hora = datetime.datetime.strptime(hora1, "%H:%M")
        descripcion = input("Descripcion: ")
        valorEntrada = float(input("Valor entrada: "))
        capacidad = int(input("Capacidad: "))
        disponibilidad = int(input("Disponibilidad: "))
        ciudad = input("Ciudad: ")
        pais = input("Pais: ")
        direccion = input("Direccion: ")
        print("Lista de tipos de evento disponibles: ")
        tipoEventObj = TipoEventLogic()
        for element in tipoEventObj.getTipo():
            print(str(element["idtipo-eventos"])+"-"+element["nombreTipo"])
        tipo = (input("Seleccione el tipo de evento según el número correspondiente: "))

        logic = EventLogic()
        rows = logic.insertEvent(idUsuarios, nombre, categoria, fecha, hora, descripcion, valorEntrada, capacidad, disponibilidad, ciudad, pais, direccion, tipo)

    elif opcion == 2:
        eventosLogic = EventLogic()
        idEventos = int(input("idEventos: "))
        oldEvent = eventosLogic.getEventById(idEventos)

        print(f"old nombre: {oldEvent['nombre']}")
        nombre = input("Nuevo nombre: ")

        print(f"old categoria: {oldEvent['categoria']}")
        print("Lista de categorías disponibles para eventos: ")
        catEventObj = CategoriaEventLogic()
        for element in catEventObj.getCat():
            print(str(element["idCategorias-eventos"])+"-"+element["nombreCat"])
        categoria = (int(input("Seleccione la nueva categoria a la que pertenece su evento según el número correspondiente: ")))

        print(f"old fecha: {oldEvent['fecha']}")
        fecha1 = input("Nueva fecha (YYYY-MM-DD): ")
        fecha = datetime.datetime.strptime(fecha1, "%Y-%m-%d")

        print(f"old hora: {oldEvent['hora']}")
        hora1 = input("Nueva hora (HH:MM): ")
        hora = datetime.datetime.strptime(hora1, "%H:%M")

        print(f"old descripcion: {oldEvent['descripcion']}")
        descripcion = input("Nueva descripcion: ")

        print(f"old valorEntrada: {oldEvent['valorEntrada']}")
        valorEntrada = float(input("Nuevo valor de entrada: "))

        print(f"old capacidad: {oldEvent['capacidad']}")
        capacidad = int(input("Nueva capacidad: "))

        print(f"old disponibilidad: {oldEvent['disponibilidad']}")
        disponibilidad = int(input("Nueva disponibilidad: "))

        print(f"old ciudad: {oldEvent['ciudad']}")
        ciudad = input("Nueva ciudad: ")

        print(f"old pais: {oldEvent['pais']}")
        pais = input("Nuevo pais: ")

        print(f"old direccion: {oldEvent['direccion']}")
        direccion = input("Nueva direccion: ")

        print(f"old tipo: {oldEvent['tipo']}")
        print("Lista de tipos de evento disponibles: ")
        tipoEventObj = TipoEventLogic()
        for element in tipoEventObj.getTipo():
            print(str(element["idtipo-eventos"])+"-"+element["nombreTipo"])
        tipo = (int(input("Seleccione el nuevo tipo de evento según el número correspondiente: ")))

        rows = eventosLogic.updateEvent(idEventos, nombre, categoria, fecha, hora, descripcion, valorEntrada, capacidad, disponibilidad, ciudad, pais, direccion, tipo)

    elif opcion == 3:
        logic = EventLogic()
        idEventos = int(input("idEventos: "))
        rows = logic.deleteEvent(idEventos)

    elif opcion == 4:
        eventListObj = EventLogic()
        events = eventListObj.getAllEvents()

        table = PrettyTable()
        table.field_names = ["idEventos", "idUsuarios", "nombre", "categoria", "fecha", "hora", "descripcion", "valorEntrada", "capacidad", "disponibilidad", "ciudad", "pais", "direccion", "tipo"]

        for event in events:
            table.add_row(
                [event.idEventos, event.idUsuarios, event.nombre, event.categoria, event.fecha, event.hora, event.descripcion, event.valorEntrada, event.capacidad, event.disponibilidad, event.ciudad, event.pais, event.direccion, event.tipo]
            )
        print(table)


    elif opcion == 5:
        events = EventLogic()
        idEventos = int(input("idEventos: "))
        event = events.getEventById(idEventos)

        table = PrettyTable()
        table.field_names = ["idEventos", "idUsuarios", "nombre", "categoria", "fecha", "hora", "descripcion", "valorEntrada", "capacidad", "disponibilidad", "ciudad", "pais", "direccion", "tipo"]
        table.add_row(
            [event["idEventos"], event["idUsuarios"], event["nombre"], event["categoria"], event["fecha"], event["hora"], event["descripcion"], event["valorEntrada"], event["capacidad"], event["disponibilidad"], event["ciudad"], event["pais"], event["direccion"], event["tipo"]]
        )
        print(table)

        
