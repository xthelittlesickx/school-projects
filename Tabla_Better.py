#project state transition table
import tkinter as tk
from tkinter import messagebox
import draw_automata

tabla_transiciones_global = {}
estados_aceptacion_global = set()
simbolos_transiciones = []
tabla_transiciones_entries = {}

def agregar_fila():
    row = len(tabla_transiciones_entries)
    tabla_transiciones_entries[row] = []
    for i, col in enumerate(['S'] + simbolos_transiciones + ['t']):
        e = tk.Entry(tabla_frame, width=10)
        e.grid(row=row + 1, column=i)  # +1 porque la primera fila tiene los encabezados
        tabla_transiciones_entries[row].append(e)

def guardar_tabla():
    global tabla_transiciones_global, estados_aceptacion_global
    tabla_transiciones = {}
    estados_aceptacion = set()

    for row_entries in tabla_transiciones_entries.values():
        if len(row_entries) != len(simbolos_transiciones) + 2:  # +2 para estado y aceptación
            continue  # Ignorar filas incompletas

        estado = row_entries[0].get()
        transiciones = {simbolo: entry.get() for simbolo, entry in zip(simbolos_transiciones, row_entries[1:-1])}
        es_aceptacion = row_entries[-1].get().lower() == 's'

        if estado:
            tabla_transiciones[estado] = transiciones
            if es_aceptacion:
                estados_aceptacion.add(estado)

    tabla_transiciones_global = tabla_transiciones
    estados_aceptacion_global = estados_aceptacion
    messagebox.showinfo("Tabla Guardada", "La tabla de transiciones ha sido guardada correctamente.")

def evaluar_cadena():
    cadena = entrada_cadena.get()
    es_valida = evaluar_afd(tabla_transiciones_global, estados_aceptacion_global, cadena)
    resultado.set("VALIDA" if es_valida else "NO VALIDA")

def evaluar_afd(tabla, estados_aceptacion, cadena):
    estado_actual = '0'  # Asumir '0' como estado inicial
    for simbolo in cadena:
        estado_actual = tabla.get(estado_actual, {}).get(simbolo)
        if estado_actual is None:
            return False
    return estado_actual in estados_aceptacion

def definir_simbolos():
    global simbolos_transiciones, tabla_transiciones_entries
    if simbolos_transiciones and tabla_transiciones_entries:
        respuesta = messagebox.askyesno(
            "Redefinir Símbolos",
            "Al cambiar los símbolos se perderán los datos de la tabla actual. ¿Quieres continuar?"
        )
        if not respuesta:
            return

    simbolos = entrada_simbolos.get().split()
    simbolos_transiciones = simbolos
    tabla_transiciones_entries.clear()  # Limpiar en lugar de crear una nueva referencia
    actualizar_encabezados()

def actualizar_encabezados():
    for widget in tabla_frame.winfo_children():
        widget.destroy()
    for i, text in enumerate(['Estado (S)'] + simbolos_transiciones + ['Aceptación (t=S/N)']):
        tk.Label(tabla_frame, text=text).grid(row=0, column=i)
    agregar_fila()

def dibujar_automata():
    if not tabla_transiciones_global or not estados_aceptacion_global:
        messagebox.showwarning("Advertencia", "Primero debes guardar la tabla de transiciones.")
        return
    draw_automata.draw_automata(estados_aceptacion_global, tabla_transiciones_global)

# Interfaz gráfica
root = tk.Tk()

etiqueta_simbolos = tk.Label(root, text="Introduce los símbolos de transición separados por espacios:")
etiqueta_simbolos.pack()

entrada_simbolos = tk.Entry(root)
entrada_simbolos.pack()

btn_definir_simbolos = tk.Button(root, text="Definir Símbolos y Actualizar Tabla", command=definir_simbolos)
btn_definir_simbolos.pack()

btn_dibujar_automata = tk.Button(root, text="Dibujar Autómata", command=dibujar_automata)
btn_dibujar_automata.pack(pady=5)

tabla_frame = tk.LabelFrame(root, text="Tabla de Transiciones")
tabla_frame.pack(padx=10, pady=10)

btn_agregar_fila = tk.Button(root, text="Agregar Fila", command=agregar_fila)
btn_agregar_fila.pack(pady=5)

btn_guardar_tabla = tk.Button(root, text="Guardar Tabla", command=guardar_tabla)
btn_guardar_tabla.pack(pady=5)

etiqueta_cadena = tk.Label(root, text="Cadena a evaluar:")
etiqueta_cadena.pack()

entrada_cadena = tk.Entry(root)
entrada_cadena.pack()

resultado = tk.StringVar()
etiqueta_resultado = tk.Label(root, textvariable=resultado)
etiqueta_resultado.pack()

boton_evaluar = tk.Button(root, text="Evaluar", command=evaluar_cadena)
boton_evaluar.pack(pady=10)

root.mainloop()
