listaIDs = [
  {
    "codigoId": "00000",
    "dueDate": "9-08-2023",
    "estado": "Finalizado",
    "cartasFaltantes": True,
    "cartasFirmadas": True,
    "cantidadCambioDueDate": 1,
  },
  {
    "codigoId": "00001",
    "dueDate": "12-09-2023",
    "estado": "En Progreso",
    "cartasFaltantes": True,
    "cartasFirmadas": False,
    "cantidadCambioDueDate": 0,
  },
  {
    "codigoId": "00002",
    "dueDate": "9-05-2023",
    "estado": "Finalizado",
    "cartasFaltantes": False,
    "cartasFirmadas": False,
    "cantidadCambioDueDate": 2,
  },
  {
    "codigoId": "00003",
    "dueDate": "9-11-2023",
    "estado": "En Progreso",
    "cartasFaltantes": False,
    "cartasFirmadas": True,
    "cantidadCambioDueDate": 3,
  }
]

# Ejercicio 1

def filtrarElementosSegun(criterio,valor, lista):
    elementosFiltrados = filter(lambda elemento: elemento.get(criterio) == valor, lista)
    return list(elementosFiltrados)


def obtengoFinalizadas(lista):
    listaFinalizada = filtrarElementosSegun("estado","Finalizado",lista)
    print(f"Cantidad de IDs finalizados es de {len(listaFinalizada)}\n")
    return listaFinalizada

def cantidadPorCriteriosA(lista,criterios):
    print("Aplicando los siguientes criterios encontramos las siguientes cantidades:\n")
    for criterio in criterios:
        listaFiltrada= filtrarElementosSegun(criterio,True, lista)
        print(f"Cantidad de IDs que cumple el criterio {criterio} es de {len(listaFiltrada)}\n")
    
def mostrarTiposFinalizadas(lista):
    listaFiltrada = obtengoFinalizadas(lista)
    cantidadPorCriteriosA(listaFiltrada,["cartasFaltantes","cartasFirmadas"]) 
    print("Terminamos con los tipos de IDs en estado finalizadas\n\n")

def totalCambiosDueDatesSegun(lista,criterio,valor):  
    listaFiltrada = filtrarElementosSegun(criterio,valor,lista)
    print(f"Con el filtro '{criterio}: {valor}': \n")
    totalCambiosDueDates(listaFiltrada)

def totalCambiosDueDates(lista): 
    totalCambios = sum(elemento.get("cantidadCambioDueDate", 0) for elemento in lista)
    print(f"Cantidad de cambios Due Date es de {totalCambios}\n")

def mostrarTotalesDueDates(lista):
    totalCambiosDueDates(lista)
    totalCambiosDueDatesSegun(lista,"estado","En Progreso") #Como no hubo casos de varios filtros a la vez, asumimos que se esperaría uno solo en particular

def ejecutarEjercicio1(lista):
    mostrarTiposFinalizadas(lista)
    mostrarTotalesDueDates(lista)
    print("Finalizamos ejercio 1 \n\n\n")

try:
    ejecutarEjercicio1(listaIDs)
except:
    print("Ejercicio 1 no salio correctamente")


#Ejercicio 2

def filtrarIDsFinalizadas(lista):
    idsFinalizados = []
    lista[:] = [elemento for elemento in lista if (idsFinalizados.append(elemento) if elemento["estado"] == "Finalizado" else True)]
    return lista,idsFinalizados

def ejecutarEjercicio2(lista):
    print("Iniciamos ejercicio 2\n")
    listaFiltrada,idsFinalizados = filtrarIDsFinalizadas(lista)
    print(f"La lista original es: {listaFiltrada}\n")
    print(f"La lista de IDs finalizados es: {idsFinalizados}\n")
    print("Finalizamos ejercicio 2\n\n\n")

try:
    ejecutarEjercicio2(listaIDs)
except:
    print("Ejercicio 2 no salio correctamente")


