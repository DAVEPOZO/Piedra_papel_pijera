import tkinter as tk
import random

class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.puntuacion = 0

class aplicacion:
    def __init__(self, root):
        self.root = root
        self.root.title("Piedra, Papel o Tijera")

        # Crear jugadores
        self.jugador = Jugador("Jugador")
        self.computadora = Jugador("Computadora")

        # Etiquetas para mostrar puntuaciones
        self.label_puntuacion_jugador = tk.Label(root, text=f"{self.jugador.nombre}: {self.jugador.puntuacion}", font=("Arial", 14))
        self.label_puntuacion_jugador.pack()

        self.label_puntuacion_computadora = tk.Label(root, text=f"{self.computadora.nombre}: {self.computadora.puntuacion}", font=("Arial", 14))
        self.label_puntuacion_computadora.pack()

        # Etiqueta para mostrar la selección de la computadora
        self.label_computadora = tk.Label(root, text="Computadora eligió: ?", font=("Arial", 14))
        self.label_computadora.pack(pady=10)

        # Etiqueta para mostrar el resultado
        self.label_resultado = tk.Label(root, text="Resultado: ?", font=("Arial", 16), fg="blue")
        self.label_resultado.pack(pady=10)

        # Botones para las opciones del jugador
        self.boton_piedra = tk.Button(root, text="Piedra", font=("Arial", 14), command=lambda: self.jugar("Piedra"))
        self.boton_piedra.pack(side=tk.LEFT, padx=10)

        self.boton_papel = tk.Button(root, text="Papel", font=("Arial", 14), command=lambda: self.jugar("Papel"))
        self.boton_papel.pack(side=tk.LEFT, padx=10)

        self.boton_tijera = tk.Button(root, text="Tijera", font=("Arial", 14), command=lambda: self.jugar("Tijera"))
        self.boton_tijera.pack(side=tk.LEFT, padx=10)

    def jugar(self, eleccion_jugador):
        opciones = ["Piedra", "Papel", "Tijera"]
        eleccion_computadora = random.choice(opciones)

        # Mostrar la elección de la computadora
        self.label_computadora.config(text=f"Computadora eligió: {eleccion_computadora}")

        # Determinar el resultado del juego
        if eleccion_jugador == eleccion_computadora:
            resultado = "Empate"
        elif (eleccion_jugador == "Piedra" and eleccion_computadora == "Tijera") or \
             (eleccion_jugador == "Papel" and eleccion_computadora == "Piedra") or \
             (eleccion_jugador == "Tijera" and eleccion_computadora == "Papel"):
            resultado = "Ganaste"
            self.jugador.puntuacion += 1
        else:
            resultado = "Perdiste"
            self.computadora.puntuacion += 1

        # Actualizar los puntajes
        self.label_puntuacion_jugador.config(text=f"{self.jugador.nombre}: {self.jugador.puntuacion}")
        self.label_puntuacion_computadora.config(text=f"{self.computadora.nombre}: {self.computadora.puntuacion}")

        # Mostrar el resultado
        self.label_resultado.config(text=f"Resultado: {resultado}")

# Crear la ventana principal y ejecutar la aplicación
root = tk.Tk()
app = aplicacion(root)
root.mainloop()
