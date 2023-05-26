import tkinter as tk
import os
from tkinter import messagebox
import json

root = tk.Tk()

def abrir_ventana():
    ruta = "login-module.py"
    os.system(f"python {ruta}")

def verificar_credenciales():
    usuario = eusu.get()
    contrasena = epas.get()

    with open('credenciales.json', 'r') as archivo:
        data = json.load(archivo)
        usuarios = data["usuarios"]

        if len(usuarios) == 0:
            messagebox.showerror("Error", "No hay usuarios registrados")
            return

        for usuario_data in usuarios:
            nombre = usuario_data["nombre"]
            clave = usuario_data["contrasena"]
            if usuario == nombre and contrasena == clave:
                abrir_ventana()
                return

    messagebox.showerror("Error", "Credenciales incorrectas")

def agregar_usuario():
    usuario = eusu.get()
    contrasena = epas.get()

    with open('credenciales.json', 'r') as archivo:
        data = json.load(archivo)
        usuarios = data["usuarios"]

        for usuario_data in usuarios:
            nombre = usuario_data["nombre"]
            if usuario == nombre:
                messagebox.showerror("Error", "El usuario ya existe")
                return

    with open('credenciales.json', 'w') as archivo:
        nuevo_usuario = {"nombre": usuario, "contrasena": contrasena}
        usuarios.append(nuevo_usuario)
        data["usuarios"] = usuarios
        json.dump(data, archivo, indent=4)

    messagebox.showinfo("Éxito", "Usuario agregado correctamente")

lusu = tk.Label(root, text="Username: ")
lusu.pack()
user = tk.StringVar()
eusu = tk.Entry(root, width=30, textvariable=user)
eusu.pack()

lpas = tk.Label(root, text="Password: ")
lpas.pack(anchor=tk.CENTER)
pas = tk.StringVar()
epas = tk.Entry(root, width=30, show="*", textvariable=pas)
epas.pack()

bl = tk.Button(root, text="Login", command=verificar_credenciales)
bl.pack(side=tk.LEFT)

bu = tk.Button(root, text="Add User", command=agregar_usuario)
bu.pack(side=tk.RIGHT)

root.mainloop()