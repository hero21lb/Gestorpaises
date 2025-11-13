#Integrador hecho por Anglat Juan y Lemus Nahuel

import csv
import os
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import time

CSV_FILE = "paises.csv"

#funciones de manejo de paises

continentes_validos = ["america del norte", "europa", "asia", "africa", "oceania", "antartida", "america del sur", "centroamerica"]

def anadir_pais(nombre: str, poblacion: int, superficie: int, continente: str) -> None:
    with open(CSV_FILE, mode='a', newline='') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow([nombre, poblacion, superficie, continente])
def cargar_paises() -> list[dict]:
    paises = []
    if os.path.exists(CSV_FILE):
        with open(CSV_FILE, mode='r') as archivo:
            lector = csv.reader(archivo)
            next(lector, None)  # Saltar la cabecera
            for fila in lector:
                pais = {
                    "nombre": fila[0],
                    "poblacion": int(fila[1]),
                    "superficie": int(fila[2]),
                    "continente": fila[3]
                }
                paises.append(pais)
    return paises
def filtrar_paises_por_continente(paises: list[dict], continente: str) -> list[dict]:
    return [pais for pais in paises if pais["continente"].lower() == continente.lower()]
def filtrar_paises_por_poblacion(paises: list[dict], min_poblacion: int, max_poblacion: int) -> list[dict]:
    return [pais for pais in paises if min_poblacion <= pais["poblacion"] <= max_poblacion]
def filtrar_paises_por_superficie(paises: list[dict], min_superficie: int, max_superficie: int) -> list[dict]:
    return [pais for pais in paises if min_superficie <= pais["superficie"] <= max_superficie]
def filtrar_paises_por_nombre(paises: list[dict], nombre: str) -> list[dict]:
    return [pais for pais in paises if nombre.lower() in pais["nombre"].lower()]
def ordenar_paises(paises: list[dict], clave: str, ascendente: bool = True) -> list[dict]:
    return sorted(paises, key=lambda x: x[clave], reverse=not ascendente)
def estadisticas_paises(paises: list[dict]) -> dict:
    from statistics import mean
    poblaciones = [pais["poblacion"] for pais in paises]
    superficies = [pais["superficie"] for pais in paises]
    pais_mayor_poblacion = max(paises, key=lambda x: x["poblacion"])
    pais_menor_poblacion = min(paises, key=lambda x: x["poblacion"])
    cantidad_por_continente = {}
    for pais in paises:
        continente = pais["continente"]
        if continente not in cantidad_por_continente:
            cantidad_por_continente[continente] = 0
        cantidad_por_continente[continente] += 1
    return {
        "pais_mayor_poblacion": pais_mayor_poblacion,
        "pais_menor_poblacion": pais_menor_poblacion,
        "promedio_poblacion": mean(poblaciones) if poblaciones else 0,
        "promedio_superficie": mean(superficies) if superficies else 0,
        "cantidad_por_continente": cantidad_por_continente        
    }
if not os.path.exists(CSV_FILE): #si no existe el archivo csv, lo crea con la cabecera
    with open(CSV_FILE, mode='w', newline='') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(["nombre", "poblacion", "superficie", "continente"])

#funciones de la interfaz grafica

def ventana_anadir_pais():
    ventana2 = tk.Toplevel()
    ventana2.title("Añadir País")
    ventana2.geometry("720x480")
    tk.Label(ventana2, text="Añadir Nuevo País", font=("Minecraft", 24)).pack(pady=20)
    entrada_nombre = tk.Entry(ventana2, font=("Minecraft", 16))
    entrada_nombre.pack(pady=10)
    entrada_poblacion = tk.Entry(ventana2, font=("Minecraft", 16))
    entrada_poblacion.pack(pady=10)
    entrada_superficie = tk.Entry(ventana2, font=("Minecraft", 16))
    entrada_superficie.pack(pady=10)
    entrada_continente = tk.Entry(ventana2, font=("Minecraft", 16))
    entrada_continente.pack(pady=10)
    tk.Button(ventana2, text="Guardar País", font=("Minecraft", 16), width=20, height=2, command=lambda: anadir_pais_gui(entrada_nombre.get(), entrada_poblacion.get(), entrada_superficie.get(), entrada_continente.get(), ventana2)).pack(pady=10)

def anadir_pais_gui(nombre: str, poblacion: str, superficie: str, continente: str, ventana2) -> None:
    if nombre.strip() == "" or poblacion.strip() == "" or superficie.strip() == "" or continente.strip() == "":
        tk.messagebox.showerror("Error", "Todos los campos son obligatorios.")
        return
    if not poblacion.isdigit() or not superficie.isdigit():
        tk.messagebox.showerror("Error", "Población y Superficie deben ser números enteros.")
        return
    poblacion = int(poblacion)
    superficie = int(superficie)
    if poblacion <= 0 or superficie <= 0:
        tk.messagebox.showerror("Error", "Población y Superficie deben ser números positivos.")
        return
    anadir_pais(nombre, poblacion, superficie, continente)
    tk.messagebox.showinfo("Éxito", f"País {nombre} añadido correctamente.")
    ventana2.destroy()

def ventana_mostrar_paises():
    ventana3 = tk.Toplevel()
    ventana3.title("Mostrar Países")
    ventana3.geometry("720x480")
    tk.Label(ventana3, text="Lista de Países", font=("Minecraft", 24)).pack(pady=20)
    paises = cargar_paises()
    texto_paises = tk.Text(ventana3, font=("Minecraft", 10))
    texto_paises.pack(pady=10)
    for pais in paises:
        texto_paises.insert(tk.END, f"{pais['nombre']} | Población: {pais['poblacion']} | Superficie: {pais['superficie']} km² | Continente: {pais['continente']}\n")

def ventana_filtrar_paises():
    ventana4 = tk.Toplevel()
    ventana4.title("Filtrar Países")
    ventana4.geometry("720x480")
    tk.Label(ventana4, text="Filtrar Países", font=("Minecraft", 24)).pack(pady=20)

    frame_opciones = tk.Frame(ventana4)
    frame_opciones.pack(pady=10)
    frame_botones = tk.Frame(ventana4)
    frame_botones.pack(pady=10)

    tk.Label(frame_opciones, text="Nombre:       ", font=("Minecraft", 10)).pack(side="left", padx=5)
    tk.Label(frame_opciones, text="Continente:                         ", font=("Minecraft", 10)).pack(side="left", padx=5)
    tk.Label(frame_opciones, text="Población Min: ", font=("Minecraft", 10)).pack(side="left", padx=5)
    tk.Label(frame_opciones, text="Población Max: ", font=("Minecraft", 10)).pack(side="left", padx=5)
    tk.Label(frame_opciones, text="Superficie Min: ", font=("Minecraft", 10)).pack(side="left", padx=5)
    tk.Label(frame_opciones, text="Superficie Max:  ", font=("Minecraft", 10)).pack(side="left", padx=5)

    entrada_buscador = tk.Entry(frame_botones, font=("Minecraft", 16), width=10)
    entrada_buscador.pack(side="left", padx=5)
    continentes = ttk.Combobox(frame_botones, values=["America del Norte", "Europa", "Asia", "Africa", "Oceania", "Antartida", "America del Sur", "Centroamerica"], font=("Minecraft", 16)) 
    continentes.pack(side="left", padx=5)
    entrada_min_poblacion = tk.Entry(frame_botones, font=("Minecraft", 16), width=10)
    entrada_min_poblacion.pack(side="left", padx=5)
    entrada_max_poblacion = tk.Entry(frame_botones, font=("Minecraft", 16), width=10)
    entrada_max_poblacion.pack(side="left", padx=5)
    entrada_min_superficie = tk.Entry(frame_botones, font=("Minecraft", 16), width=10)
    entrada_min_superficie.pack(side="left", padx=5)
    entrada_max_superficie = tk.Entry(frame_botones, font=("Minecraft", 16), width=10)
    entrada_max_superficie.pack(side="left", padx=5)
    texto_resultados = tk.Text(ventana4, font=("Minecraft", 10))
    texto_resultados.pack(pady=10)

    tk.Button(ventana4, text="Filtrar", font=("Minecraft", 16), width=20, height=2, command=lambda: filtrar_paises_gui(entrada_buscador.get(), continentes.get(), entrada_min_poblacion.get(), entrada_max_poblacion.get(), entrada_min_superficie.get(), entrada_max_superficie.get(), texto_resultados)).pack(pady=10)

def filtrar_paises_gui(nombre: str, continente: str, min_poblacion: str, max_poblacion: str, min_superficie: str, max_superficie: str, texto_resultados) -> None:
    paises = cargar_paises()
    resultado = paises
    if nombre.strip() != "":
        resultado = filtrar_paises_por_nombre(resultado, nombre)
    if continente.strip() != "":
        resultado = filtrar_paises_por_continente(resultado, continente)
        #si no se detecta uno de los valores de superficie o poblacion, de ser minima dar el valor 0 y de ser máxima dar un valor alto
    if min_poblacion.strip() == "":
        min_poblacion = 0
    else:
        min_poblacion = int(min_poblacion)
    if max_poblacion.strip() == "":
        max_poblacion = 10**10
    else:
        max_poblacion = int(max_poblacion)
    resultado = filtrar_paises_por_poblacion(resultado, min_poblacion, max_poblacion)
    if min_superficie.strip() == "":
        min_superficie = 0
    else:
        min_superficie = int(min_superficie)
    if max_superficie.strip() == "":
        max_superficie = 10**10
    else:
        max_superficie = int(max_superficie)
    resultado = filtrar_paises_por_superficie(resultado, min_superficie, max_superficie)
    texto_resultados.delete(1.0, tk.END)
    for pais in resultado:
        texto_resultados.insert(tk.END, f"{pais['nombre']} | Población: {pais['poblacion']} | Superficie: {pais['superficie']} km² | Continente: {pais['continente']}\n")

def ventana_ordenar_paises():
    ventana5 = tk.Toplevel()
    ventana5.title("Ordenar Países")
    ventana5.geometry("720x480")
    tk.Label(ventana5, text="Ordenar Países", font=("Minecraft", 24)).pack(pady=20)
    frame_botones = tk.Frame(ventana5)
    frame_botones.pack(pady=10)
    tk.Button(frame_botones, text="Alfabético", font=("Minecraft", 16), width=10, height=2, command=lambda: ordenar_paises_gui("nombre", texto_resultados, combo_ascendente.get() == "Ascendente")).pack(side="left", padx=5)
    tk.Button(frame_botones, text="Población", font=("Minecraft", 16), width=10, height=2, command=lambda: ordenar_paises_gui("poblacion", texto_resultados, combo_ascendente.get() == "Ascendente")).pack(side="left", padx=5)
    tk.Button(frame_botones, text="Superficie", font=("Minecraft", 16), width=10, height=2, command=lambda: ordenar_paises_gui("superficie", texto_resultados, combo_ascendente.get() == "Ascendente")).pack(side="left", padx=5)
    tk.Button(frame_botones, text="Continente", font=("Minecraft", 16), width=10, height=2, command=lambda: ordenar_paises_gui("continente", texto_resultados, combo_ascendente.get() == "Ascendente")).pack(side="left", padx=5)
    combo_ascendente = ttk.Combobox(frame_botones, values=["Ascendente", "Descendente"], font=("Minecraft", 16), width=10)
    combo_ascendente.current(0)
    combo_ascendente.pack(side="left", padx=5)
    texto_resultados = tk.Text(ventana5, font=("Minecraft", 10))
    texto_resultados.pack(pady=10)
def ordenar_paises_gui(clave: str, texto_resultados, ascendente) -> None:
    paises = cargar_paises()
    resultado = ordenar_paises(paises, clave, ascendente)
    texto_resultados.delete(1.0, tk.END)
    for pais in resultado:
        texto_resultados.insert(tk.END, f"{pais['nombre']} | Población: {pais['poblacion']} | Superficie: {pais['superficie']} km² | Continente: {pais['continente']}\n")

def ventana_estadisticas_paises():
    ventana6 = tk.Toplevel()
    ventana6.title("Estadísticas Países")
    ventana6.geometry("720x480")
    tk.Label(ventana6, text="Estadísticas de Países", font=("Minecraft", 24)).pack(pady=20)
    paises = cargar_paises()
    stats = estadisticas_paises(paises)
    frame_poblacion_promedio = tk.Frame(ventana6)
    frame_poblacion_promedio.pack(pady=10)
    frame_superficie_promedio = tk.Frame(ventana6)
    frame_superficie_promedio.pack(pady=10)
    frame_mayor_población = tk.Frame(ventana6)
    frame_mayor_población.pack(pady=10)
    frame_menor_población = tk.Frame(ventana6)
    frame_menor_población.pack(pady=10)
    frame_cantidad_continente = tk.Frame(ventana6)
    frame_cantidad_continente.pack(pady=10)
    tk.Label(frame_poblacion_promedio, text=f"Población Promedio: {stats['promedio_poblacion']:.2f}", font=("Minecraft", 16)).pack()
    tk.Label(frame_superficie_promedio, text=f"Superficie Promedio: {stats['promedio_superficie']:.2f} km²", font=("Minecraft", 16)).pack()
    tk.Label(frame_mayor_población, text=f"País con Mayor Población: {stats['pais_mayor_poblacion']['nombre']} ({stats['pais_mayor_poblacion']['poblacion']})", font=("Minecraft", 16)).pack()
    tk.Label(frame_menor_población, text=f"País con Menor Población: {stats['pais_menor_poblacion']['nombre']} ({stats['pais_menor_poblacion']['poblacion']})", font=("Minecraft", 16)).pack()
    tk.Label(frame_cantidad_continente, text="Cantidad de Países por Continente:", font=("Minecraft", 16)).pack()
    for continente, cantidad in stats['cantidad_por_continente'].items():
        tk.Label(frame_cantidad_continente, text=f" - {continente}: {cantidad}", font=("Minecraft", 14)).pack()

opciondeuso = input("Desea usar la interfaz grafica? (s/n): ").lower()
if opciondeuso == 's':
    app = tk.Tk()
    app.title("Gestor de Países")
    app.geometry("720x480")
    tk.Label(app, text="Menu principal", font=("Minecraft", 24)).pack(pady=20)
    tk.Button(app, text="Añadir País ➕", font=("Minecraft", 16), width=20, height=2, command=ventana_anadir_pais).pack(pady=10)
    tk.Button(app, text="Mostrar Países 📋", font=("Minecraft", 16), width=20, height=2, command=ventana_mostrar_paises).pack(pady=10)
    tk.Button(app, text="Filtrar Países 🔍", font=("Minecraft", 16), width=20, height=2, command=ventana_filtrar_paises).pack(pady=10)
    tk.Button(app, text="Ordenar Países ↕️", font=("Minecraft", 16), width=20, height=2, command= ventana_ordenar_paises).pack(pady=10)
    tk.Button(app, text="Estadísticas 📊", font=("Minecraft", 16), width=20, height=2, command=ventana_estadisticas_paises).pack(pady=10)
    tk.Button(app, text="Salir ❌", font=("Minecraft", 16), width=20, height=2, command=app.quit).pack(pady=10)

    app.mainloop()

elif opciondeuso == 'n':

    while True:
        paises = cargar_paises() #carga los paises al principio
        time.sleep(2)
        print("╔═════════════════════════════════════╗")
        print("║       Menú de Gestión de Países     ║")
        print("╠═════════════════════════════════════╣")
        print("║ 1. Añadir País ➕                   ║")
        print("║ 2. Mostrar Países 📋                ║")
        print("║ 3. Filtrar Países 🔍                ║")
        print("║ 4. Ordenar Países ↕️                 ║")
        print("║ 5. Estadísticas 📊                  ║")
        print("║ 6. Salir ❌                         ║")
        print("╚═════════════════════════════════════╝")
        opcion = input(" » Seleccione una opción del 1 al 6: \n » ")

        match opcion:
            case "1":
                print("╔═════════════════════════════════════╗")
                print("║          Añadir Nuevo País          ║")
                print("╚═════════════════════════════════════╝")
                nombre = input(" » Ingrese el nombre del país: ")
                if nombre.strip() == "":
                    print(" » El nombre no puede estar vacío.")
                    continue
                elif nombre.isdigit():
                    print(" » El nombre no puede ser un número.")
                    continue
                #comprobar que el nombre no exista en el csv
                elif any(pais["nombre"].lower() == nombre.lower() for pais in paises):
                    print(" » El país ya existe en el registro.")
                    continue
                poblacion = input(" » Ingrese la población del país: ")
                if not poblacion.isdigit():
                    print(" » La población debe ser un número entero.")
                    continue
                poblacion = int(poblacion)
                if poblacion <= 0:
                    print(" » La población debe ser un número positivo.")
                    continue
                superficie = input(" » Ingrese la superficie del país (km²): ")
                if not superficie.isdigit():
                    print(" » La superficie debe ser un número entero.")
                    continue
                superficie = int(superficie)
                if superficie <= 0:
                    print(" » La superficie debe ser un número positivo.")
                    continue
                continente = input(" » Ingrese el continente del país: ")
                if continente.strip() == "":
                    print(" » El continente no puede estar vacío.")
                    continue
                elif continente.isdigit():
                    print(" » El continente no puede ser un número.")
                    continue
                #comprobar que el continente exista (america, europa, asia, africa, oceania, antartida)
                continente = continente.lower().replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")
                if continente.lower() not in continentes_validos:
                    print(" » Continente no válido. Los continentes válidos son: América del Norte, Europa, Asia, África, Oceanía, Antártida, América del Sur, Centroamérica.")
                    continue
                #guardar el continente sin tildes
                anadir_pais(nombre, poblacion, superficie, continente)
                print(f" » País {nombre} añadido correctamente.")
                
            case "2":
                print("╔═════════════════════════════════════╗")
                print("║           Lista de Países           ║")
                print("╚═════════════════════════════════════╝ \n")
                if not paises:
                    print(" » No hay países registrados.")
                else:
                    for pais in paises:
                        print(f" » {pais['nombre']} | Población: {pais['poblacion']} | Superficie: {pais['superficie']} km² | Continente: {pais['continente']}")
            case "3":
                print("╔═════════════════════════════════════╗")
                print("║           Filtrar Países            ║")
                print("╚═════════════════════════════════════╝")
                print(" » 1. Filtrar por Continente")
                print(" » 2. Filtrar por Rango de Población")
                print(" » 3. Filtrar por Rango de Superficie")
                print(" » 4. Filtrar por Nombre")
                subopcion = input(" » Seleccione una opción del 1 al 4: \n » ")
                if subopcion == "1":
                    continente = input(" » Ingrese el continente: ")
                    if continente.strip() == "":
                        print(" » El continente no puede estar vacío.") 
                    elif continente.isdigit():
                        print(" » El continente no puede ser un número.")
                        continue
                    elif continente.lower() not in continentes_validos:
                        print(" » Continente no válido. Los continentes válidos son: América del Norte, Europa, Asia, África, Oceanía, Antártida, América del Sur, Centroamérica.")
                        continue
                    resultado = filtrar_paises_por_continente(paises, continente)
                elif subopcion == "2":
                    min_poblacion = input(" » Ingrese la población mínima: ")
                    if not min_poblacion.isdigit():
                        print(" » La población mínima debe ser un número entero.")
                        continue
                    min_poblacion = int(min_poblacion)
                    if min_poblacion < 0:
                        print(" » La población mínima debe ser un número positivo.")
                        continue
                    max_poblacion = input(" » Ingrese la población máxima: ")
                    if not max_poblacion.isdigit():
                        print(" » La población máxima debe ser un número entero.")
                        continue
                    max_poblacion = int(max_poblacion)
                    if max_poblacion < 0:
                        print(" » La población máxima debe ser un número positivo.")
                        continue
                    elif max_poblacion < min_poblacion:
                        print(" » La población máxima debe ser mayor o igual a la mínima.")
                        continue
                    resultado = filtrar_paises_por_poblacion(paises, min_poblacion, max_poblacion)
                elif subopcion == "3":
                    min_superficie = input(" » Ingrese la superficie mínima (km²): ")
                    if not min_superficie.isdigit():
                        print(" » La superficie mínima debe ser un número entero.")
                        continue
                    min_superficie = int(min_superficie)
                    if min_superficie < 0:
                        print(" » La superficie mínima debe ser un número positivo.")
                        continue
                    max_superficie = input(" » Ingrese la superficie máxima (km²): ")
                    if not max_superficie.isdigit():
                        print(" » La superficie máxima debe ser un número entero.")
                        continue
                    max_superficie = int(max_superficie)
                    if max_superficie < 0:
                        print(" » La superficie máxima debe ser un número positivo.")
                        continue
                    elif max_superficie < min_superficie:
                        print(" » La superficie máxima debe ser mayor o igual a la mínima.")
                        continue
                    resultado = filtrar_paises_por_superficie(paises, min_superficie, max_superficie)
                elif subopcion == "4":
                    nombre = input(" » Ingrese el nombre o parte del nombre del país: ")
                    if nombre.strip() == "":
                        print(" » El nombre no puede estar vacío.")
                        continue
                    elif nombre.isdigit():
                        print(" » El nombre no puede ser un número.")
                        continue
                    resultado = filtrar_paises_por_nombre(paises, nombre)
                else:
                    print(" » Opción no válida.")
                    continue
                if not resultado:
                    print(" » No se encontraron países con los criterios especificados.")
                else:
                    for pais in resultado:
                        print(f" » {pais['nombre']} | Población: {pais['poblacion']} | Superficie: {pais['superficie']} km² | Continente: {pais['continente']}")
                
            case "4":
                print("╔═════════════════════════════════════╗")
                print("║           Ordenar Países            ║")
                print("╚═════════════════════════════════════╝")
                print(" » Claves disponibles: nombre, poblacion, superficie, continente")
                clave = input(" » Ingrese la clave por la cual desea ordenar: ").lower()
                if clave not in ["nombre", "poblacion", "superficie", "continente"]:
                    print(" » Clave no válida.")
                    continue
                orden = input(" » ¿Desea un orden ascendente? (s/n): ").lower()
                ascendente = orden == 's' and orden != 'n'
                if orden not in ['s', 'n']:
                    print(" » Opción no válida. Se establecerá orden ascendente por defecto.")
                resultado = ordenar_paises(paises, clave, ascendente)
                for pais in resultado:
                    print(f" » {pais['nombre']} | Población: {pais['poblacion']} | Superficie: {pais['superficie']} km² | Continente: {pais['continente']}")
                
            case "5":
                print("╔═════════════════════════════════════╗")
                print("║          Estadísticas Países        ║")
                print("╚═════════════════════════════════════╝")
                stats = estadisticas_paises(paises)
                print(f" » País con mayor población: {stats['pais_mayor_poblacion']['nombre']} ({stats['pais_mayor_poblacion']['poblacion']})")
                print(f" » País con menor población: {stats['pais_menor_poblacion']['nombre']} ({stats['pais_menor_poblacion']['poblacion']})")
                print(f" » Población promedio: {stats['promedio_poblacion']:.2f}")
                print(f" » Superficie promedio: {stats['promedio_superficie']:.2f}")
                print(" » Cantidad de países por continente:")
                for continente, cantidad in stats['cantidad_por_continente'].items():
                    print(f"   - {continente}: {cantidad}")
                
            case "6":
                print(" » Saliendo del programa... Adiós!")
                break
            case _:
                print(" » Opción no válida. Por favor, seleccione una opción del 1 al 6.")  