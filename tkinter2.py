import tkinter as tk
import webview

def main():
    root = tk.Tk()
    root.title("Mi Aplicación Tkinter")

    label = tk.Label(root, text="¡Hola, mundo!")
    label.pack()

    root.mainloop()

    # Código para convertir la aplicación a HTML
    webview.create_window("Mi Aplicación Tkinter", html='<h1>¡Hola, mundo!</h1>', width=800, height=600)
    webview.start()

if __name__ == "__main__":
    main()
