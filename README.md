# Gestor de Países 🌎

Proyecto integrador hecho por **Anglat Juan** y **Lemus Nahuel**.

Este programa permite **gestionar información de países** mediante una interfaz gráfica o desde la consola.  
Los datos se guardan en un archivo CSV llamado `paises.csv`.

---

## 🧩 Funcionalidades

- **Añadir país:** permite registrar nuevos países con nombre, población, superficie y continente.  
- **Mostrar países:** lista todos los países almacenados.  
- **Filtrar:** busca países por nombre, continente, población o superficie.  
- **Ordenar:** ordena los países por diferentes criterios (alfabético, población, superficie, continente).  
- **Estadísticas:** muestra información general, como:
  - País con mayor y menor población  
  - Promedio de población y superficie  
  - Cantidad de países por continente  

---

## 🖥️ Modo de uso

Al iniciar el programa, se te preguntará si querés usar la **interfaz gráfica (Tkinter)** o el **modo consola**:


### Modo gráfico (`s`)
Abre una ventana con botones para acceder a todas las funciones.

### Modo consola (`n`)
Muestra un menú de texto con las mismas opciones.

---

## ⚙️ Requisitos

- **Python 3.10 o superior** (por el uso de `match` y anotaciones modernas).
- Librerías estándar:
  - `csv`
  - `os`
  - `tkinter`
  - `time`

No requiere instalación adicional. 

---

## 📁 Archivos generados

- **paises.csv:** se crea automáticamente al ejecutar el programa si no existe.  
  Contiene las columnas:

nombre, poblacion, superficie, continente

---

## 🧠 Detalles técnicos

- La interfaz gráfica usa **Tkinter** y **ttk.Combobox**.  
- Los datos se guardan de forma persistente en CSV.  
- Los nombres de continente válidos son:

América del Norte, Europa, Asia, África, Oceanía, Antártida, América del Sur, Centroamérica

- Se pueden ingresar sin tildes y en minúsculas.

---

## 👥 Autores

- **Juan Anglat**
- **Nahuel Lemus**

---

## 🏷️ Licencia

Este proyecto se distribuye con fines educativos.
