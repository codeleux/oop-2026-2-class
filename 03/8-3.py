import math
import tkinter as tk
from abc import ABC, abstractmethod
from tkinter import messagebox, ttk


class FiguraGeometrica(ABC):
    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def volumen(self):
        pass

    @abstractmethod
    def superficie(self):
        pass


class Cilindro(FiguraGeometrica):
    def __init__(self, radio, altura):
        super().__init__("Cilindro")
        self.radio = radio
        self.altura = altura

    def volumen(self):
        return math.pi * self.radio ** 2 * self.altura

    def superficie(self):
        return 2 * math.pi * self.radio * (self.radio + self.altura)


class Esfera(FiguraGeometrica):
    def __init__(self, radio):
        super().__init__("Esfera")
        self.radio = radio

    def volumen(self):
        return 4 / 3 * math.pi * self.radio ** 3

    def superficie(self):
        return 4 * math.pi * self.radio ** 2


class Piramide(FiguraGeometrica):
    def __init__(self, base, altura, apotema):
        super().__init__("Pirámide")
        self.base = base
        self.altura = altura
        self.apotema = apotema

    def volumen(self):
        return self.base ** 2 * self.altura / 3

    def superficie(self):
        return self.base ** 2 + 2 * self.base * self.apotema


CAMPOS = {
    "Cilindro": (Cilindro, ("Radio (cm)", "Altura (cm)")),
    "Esfera": (Esfera, ("Radio (cm)",)),
    "Pirámide": (Piramide, ("Lado de la base (cm)", "Altura (cm)", "Apotema (cm)")),
}


class VentanaFiguras(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Volumen y superficie de figuras")
        self.resizable(False, False)

        contenedor = tk.Frame(self, padx=20, pady=15)
        contenedor.pack(fill="both", expand=True)

        tk.Label(contenedor, text="Seleccione la figura:").pack(anchor="w")

        self.tipo = tk.StringVar(value="Cilindro")
        opciones = tk.Frame(contenedor)
        opciones.pack(anchor="w", pady=(5, 10))
        for nombre in CAMPOS:
            ttk.Radiobutton(
                opciones,
                text=nombre,
                value=nombre,
                variable=self.tipo,
                command=self.mostrar_campos,
            ).pack(side="left", padx=(0, 15))

        self.campos = tk.Frame(contenedor)
        self.campos.pack(fill="x")

        ttk.Button(
            contenedor, text="Calcular", command=self.calcular
        ).pack(fill="x", pady=12)

        resultados = tk.Frame(contenedor)
        resultados.pack(fill="x")
        self.valores = {}
        for fila, (clave, texto) in enumerate(
            (("volumen", "Volumen:"), ("superficie", "Superficie:"))
        ):
            tk.Label(resultados, text=texto).grid(
                row=fila, column=0, sticky="w", pady=2
            )
            valor = tk.Label(resultados, text="-", width=18, anchor="e")
            valor.grid(row=fila, column=1, sticky="e", padx=(15, 0))
            self.valores[clave] = valor

        self.entradas = []
        self.mostrar_campos()

    def mostrar_campos(self):
        for widget in self.campos.winfo_children():
            widget.destroy()
        self.entradas = []
        for i, etiqueta in enumerate(CAMPOS[self.tipo.get()][1]):
            tk.Label(self.campos, text=f"{etiqueta}:").grid(
                row=i, column=0, sticky="w", pady=3
            )
            entrada = tk.Entry(self.campos, width=15, justify="right")
            entrada.grid(row=i, column=1, padx=(10, 0), pady=3)
            self.entradas.append(entrada)
        self.entradas[0].focus_set()
        for valor in self.valores.values():
            valor.config(text="-")

    def calcular(self):
        valores = []
        for i, entrada in enumerate(self.entradas, start=1):
            texto = entrada.get().strip().replace(",", ".")
            try:
                valor = float(texto)
            except ValueError:
                messagebox.showerror(
                    "Error", f"El dato {i} no es un número válido."
                )
                entrada.focus_set()
                entrada.select_range(0, tk.END)
                return
            if valor <= 0:
                messagebox.showerror(
                    "Error", f"El dato {i} debe ser mayor que cero."
                )
                entrada.focus_set()
                entrada.select_range(0, tk.END)
                return
            valores.append(valor)

        clase, _ = CAMPOS[self.tipo.get()]
        figura = clase(*valores)

        self.valores["volumen"].config(text=f"{figura.volumen():.2f} cm³")
        self.valores["superficie"].config(text=f"{figura.superficie():.2f} cm²")


if __name__ == "__main__":
    VentanaFiguras().mainloop()
