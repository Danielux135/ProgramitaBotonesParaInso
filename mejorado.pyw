import tkinter as tk
import json
from tkinter.font import Font

def update_json():
    # Obtener los valores de las celdas
    package_name = PackageNameValue.get()
    direct_connection = DirectConnectionValue.get()
    server_address = ServerAddressValue.get()
    proxy_redirection = ProxyRedirectionValue.get()
    proxy_address = ProxyAddressValue.get()
    proxy_port = ProxyPortValue.get()
    trace_active = TraceValue.get()
    dump_active = ActiveValue.get()
    dump_path = PathValue.get()

    # Actualizar el archivo JSON con los nuevos valores
    data["Connection"]["PackageName"] = package_name
    data["Connection"]["DirectConnection"] = direct_connection
    data["Connection"]["ServerAddress"] = server_address
    data["Connection"]["ProxyRedirection"] = proxy_redirection
    data["Connection"]["ProxyAddress"] = proxy_address
    data["Connection"]["ProxyPort"] = proxy_port
    data["Trace"] = trace_active
    data["Dump"]["Active"] = dump_active
    data["Dump"]["Path"] = dump_path

    # Guardar los cambios en el archivo JSON
    with open("config.json", "w") as json_file:
        json.dump(data, json_file, indent=4)


    #Función para los colores
def set_theme(X, Y, A):
        window.config(background=X)
        section1_frame.config(bg=X)
        section2_frame.config(bg=X)
        section3_frame.config(bg=X)
        label_section1.config(bg=X, fg=Y, font=bold_font)
        label_section2.config(bg=X, fg=Y, font=bold_font)
        label_section3.config(bg=X, fg=Y, font=bold_font)
        button_save_changes.config(bg="springgreen2", fg=Y)
        checkbutton1.config(bg=X, fg=Y, selectcolor=X)
        checkbutton2.config(bg=X, fg=Y, selectcolor=X)
        checkbutton3.config(bg=X, fg=Y, selectcolor=X)
        checkbutton4.config(bg=X, fg=Y, selectcolor=X)
        entry1_label.config(bg=X, fg=Y)
        entry2_label.config(bg=X, fg=Y)
        entry3_label.config(bg=X, fg=Y)
        entry4_label.config(bg=X, fg=Y)
        entry5_label.config(bg=X, fg=Y)
        entry1.config(bg=X, fg=Y)
        entry2.config(bg=X, fg=Y)
        entry3.config(bg=X, fg=Y)
        entry4.config(bg=X, fg=Y)
        entry5.config(bg=X, fg=Y)
        button_toggle_theme.config(bg="gray", fg="white")
        
def toggle_theme():
    global IsDarkTheme
    if IsDarkTheme:
        set_theme(light_theme_bg, light_theme_fg, universal_theme)
    else:
        set_theme(dark_theme_bg, dark_theme_fg,universal_theme)
    IsDarkTheme = not IsDarkTheme
        
# Crear la ventana principal
window = tk.Tk()    

# Configurar la ventana
window.title("Programa con botones seleccionables y campos de texto")
window.geometry("190x606")
window.resizable(False,False)
window.grid_columnconfigure(0, weight=1)  # Ajustar el ancho de la columna principal

# Variables para almacenar las opciones seleccionadas
DirectConnectionValue = tk.BooleanVar()
ProxyRedirectionValue = tk.BooleanVar()
TraceValue = tk.BooleanVar()
ActiveValue = tk.BooleanVar()
ThemeValue = tk.BooleanVar()
IsDarkTheme = True

# Variables para almacenar los valores de los campos de texto
PackageNameValue = tk.StringVar()
ServerAddressValue = tk.StringVar()
ProxyAddressValue = tk.StringVar()
ProxyPortValue = tk.StringVar()
PathValue = tk.StringVar()

# Leer los datos del archivo JSON
with open("config.json") as json_file:
    data = json.load(json_file)        

# Establecer los valores booleanos en la primera sección
DirectConnectionValue.set(data["Connection"]["DirectConnection"])
ProxyRedirectionValue.set(data["Connection"]["ProxyRedirection"])
TraceValue.set(data["Trace"])
ActiveValue.set(data["Dump"]["Active"])
ThemeValue.set(IsDarkTheme) 

# Establecer los valores de los campos de texto
PackageNameValue.set(data["Connection"]["PackageName"])
ServerAddressValue.set(data["Connection"]["ServerAddress"])
ProxyAddressValue.set(data["Connection"]["ProxyAddress"])
ProxyPortValue.set(data["Connection"]["ProxyPort"])
PathValue.set(data["Dump"]["Path"])

# Variables para almacenar los colores del tema
dark_theme_bg = "gray"
dark_theme_fg = "white"
light_theme_bg = "lightskyblue"
light_theme_fg = "black"
universal_theme = "black"
bold_font = Font(family="Arial", size=12, weight="bold")  # Fuente en negrita

# Crear los marcos para las secciones
section1_frame = tk.Frame(window)
section1_frame.grid(row=0, column=0, padx=20, pady=20, sticky="w")

section2_frame = tk.Frame(window)
section2_frame.grid(row=1, column=0, padx=20, pady=20, sticky="w")

section3_frame = tk.Frame(window)
section3_frame.grid(row=2, column=0, padx=20, pady=20, sticky="w")

# Etiquetas para los nombres de las secciones

label_section1 = tk.Label(section1_frame, text="Connection")
label_section1.grid(row=0, column=0, columnspan=2, sticky="w")

label_section2 = tk.Label(section2_frame, text="Trace")
label_section2.grid(row=0, column=0, sticky="w")

label_section3 = tk.Label(section3_frame, text="Dump")
label_section3.grid(row=0, column=0, sticky="w")

# Crear los botones seleccionables en cada sección
checkbutton1 = tk.Checkbutton(section1_frame, text="Direct Connection", variable=DirectConnectionValue)
checkbutton1.grid(row=1, column=0, sticky="w")

checkbutton2 = tk.Checkbutton(section1_frame, text="Proxy Redirection", variable=ProxyRedirectionValue)
checkbutton2.grid(row=2, column=0, sticky="w")

checkbutton3 = tk.Checkbutton(section2_frame, text="Trace", variable=TraceValue)
checkbutton3.grid(row=1, column=0, sticky="w")

checkbutton4 = tk.Checkbutton(section3_frame, text="Active", variable=ActiveValue)
checkbutton4.grid(row=1, column=0, sticky="w")

# Crear campos de texto en la primera sección
entry1_label = tk.Label(section1_frame, text="PackageName")
entry1_label.grid(row=3, column=0, sticky="w")

entry1 = tk.Entry(section1_frame, textvariable=PackageNameValue)
entry1.grid(row=4, column=0, sticky="w")

entry2_label = tk.Label(section1_frame, text="ServerAddress")
entry2_label.grid(row=5, column=0, sticky="w")

entry2 = tk.Entry(section1_frame, textvariable=ServerAddressValue)
entry2.grid(row=6, column=0, sticky="w")

entry3_label = tk.Label(section1_frame, text="ProxyAddress")
entry3_label.grid(row=7, column=0, sticky="w")

entry3 = tk.Entry(section1_frame, textvariable=ProxyAddressValue)
entry3.grid(row=8, column=0, sticky="w")

entry4_label = tk.Label(section1_frame, text="ProxyPort")
entry4_label.grid(row=9, column=0, sticky="w")

entry4 = tk.Entry(section1_frame, textvariable=ProxyPortValue)
entry4.grid(row=10, column=0, sticky="w")

entry5_label = tk.Label(section3_frame, text="Path")
entry5_label.grid(row=2, column=0, sticky="w")

entry5 = tk.Entry(section3_frame, textvariable=PathValue)
entry5.grid(row=3, column=0, sticky="w")

# Crear un botón para guardar los cambios en el archivo JSON
button_save_changes = tk.Button(window, text="Guardar cambios", command=update_json)
button_save_changes.grid(row=3, column=0, pady=20, sticky="we", columnspan=1)  # Centrar el botón
button_save_changes.configure(width=2) 

# Crear el botón para cambiar el tema
button_toggle_theme = tk.Button(window, text="Cambiar tema", command=toggle_theme)
button_toggle_theme.grid(row=4, column=0, pady=20, sticky="we", columnspan=1)  # Centrar el botón

toggle_theme()

# Iniciar el bucle principal de la ventana
window.mainloop()