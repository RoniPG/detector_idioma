import tkinter as tk
from main import detectar_idioma


def detectar():
    """
    Dectar el idioma del texto ingresado en la interfaz gráfica.
    """
    texto = entrada.get("1.0", tk.END).strip()
    if not texto:
        resultado.set("No se ingresó texto")
    else:
        resultado.set(f"Idioma: {detectar_idioma(texto)}")


root = tk.Tk()
root.title("Detector de Idioma")

tk.Label(root, text="Introduce un texto:").pack(pady=5)

entrada = tk.Text(root, height=5, width=40)
entrada.pack(pady=5)

tk.Button(root, text="Detectar idioma", command=detectar).pack(pady=5)

resultado = tk.StringVar()
tk.Label(root, textvariable=resultado).pack(pady=5)

root.mainloop()
