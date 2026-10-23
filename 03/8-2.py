import statistics
import tkinter as tk
from tkinter import messagebox


class VentanaNotas(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Notas del estudiante")
        self.resizable(False, False)

        self.entradas = []
        contenedor = tk.Frame(self, padx=20, pady=15)
        contenedor.pack(fill="both", expand=True)

        tk.Label(contenedor, text="Ingrese las cinco notas:").grid(
            row=0, column=0, columnspan=2, pady=(0, 10), sticky="w"
        )

        for i in range(5):
            tk.Label(contenedor, text=f"Nota {i + 1}:").grid(
                row=i + 1, column=0, sticky="w", pady=3
            )
            entrada = tk.Entry(contenedor, width=15, justify="right")
            entrada.grid(row=i + 1, column=1, padx=(10, 0), pady=3)
            self.entradas.append(entrada)

        tk.Button(
            contenedor, text="Calcular", command=self.calcular
        ).grid(row=6, column=0, columnspan=2, pady=12, sticky="ew")

        resultados = tk.Frame(contenedor)
        resultados.grid(row=7, column=0, columnspan=2, sticky="ew")

        self.etiquetas = {}
        nombres = [
            ("promedio", "Promedio:"),
            ("desviacion", "Desviación estándar:"),
            ("mayor", "Mayor nota:"),
            ("menor", "Menor nota:"),
        ]
        for fila, (clave, texto) in enumerate(nombres):
            tk.Label(resultados, text=texto).grid(
                row=fila, column=0, sticky="w", pady=2
            )
            valor = tk.Label(resultados, text="-", width=12, anchor="e")
            valor.grid(row=fila, column=1, sticky="e", padx=(15, 0))
            self.etiquetas[clave] = valor

        self.entradas[0].focus_set()

    def calcular(self):
        notas = []
        for i, entrada in enumerate(self.entradas, start=1):
            texto = entrada.get().strip().replace(",", ".")
            try:
                nota = float(texto)
            except ValueError:
                messagebox.showerror(
                    "Error", f"La nota {i} no es un número válido."
                )
                entrada.focus_set()
                entrada.select_range(0, tk.END)
                return
            if not 0 <= nota <= 5:
                messagebox.showerror(
                    "Error", f"La nota {i} debe estar entre 0 y 5."
                )
                entrada.focus_set()
                entrada.select_range(0, tk.END)
                return
            notas.append(nota)

        self.etiquetas["promedio"].config(text=f"{statistics.mean(notas):.2f}")
        self.etiquetas["desviacion"].config(
            text=f"{statistics.pstdev(notas):.2f}"
        )
        self.etiquetas["mayor"].config(text=f"{max(notas):.2f}")
        self.etiquetas["menor"].config(text=f"{min(notas):.2f}")


if __name__ == "__main__":
    VentanaNotas().mainloop()
