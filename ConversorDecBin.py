from customtkinter import *

class App:
    def __init__(self, master):
        set_appearance_mode("Dark")
        set_default_color_theme("blue")

        self.resultFont = ("Consolas", 14, "bold")

        # Container principal
        self.container = CTkFrame(master, corner_radius=15)
        self.container.pack(fill="both", expand=True, padx=20, pady=20)

        # Título
        self.title = CTkLabel(self.container, text="Conversor Decimal → Binário", font=("Segoe UI", 18, "bold"))
        self.title.pack(pady=15)

        # Entrada: Valor
        self.valor = CTkEntry(self.container, placeholder_text="Digite o número decimal...", font=("Consolas", 12))
        self.valor.pack(pady=10)

        # Entrada: Precisão
        self.precisao = CTkEntry(self.container, placeholder_text="Precisão (ex: 5)", font=("Consolas", 12))
        self.precisao.pack(pady=10)

        # Botão de conversão
        self.botao = CTkButton(self.container, text="Converter", command=self.decPARAbin)
        self.botao.pack(pady=15)

        # Resultado
        self.resultado = CTkLabel(self.container, text="Aguardando conversão...", font=self.resultFont, wraplength=380)
        self.resultado.pack(pady=20)

    def decPARAbin(self):
        try:
            num = float(self.valor.get())
            pres = int(self.precisao.get())
            if pres < 0:
                raise ValueError("Precisão negativa")

            parte_int = int(abs(num))
            parte_frac = abs(num) - parte_int

            # Parte inteira
            bin_int = "0" if parte_int == 0 else ""
            while parte_int > 0:
                bin_int = str(parte_int % 2) + bin_int
                parte_int //= 2

            # Parte fracionária
            bin_frac = ""
            while pres > 0 and parte_frac > 0:
                parte_frac *= 2
                bit = int(parte_frac)
                bin_frac += str(bit)
                parte_frac -= bit
                pres -= 1

            # Montar resultado final
            resultado = f"{'-' if num < 0 else ''}{bin_int}"
            if bin_frac:
                resultado += f".{bin_frac}"

            self.resultado.configure(text=resultado, text_color="#2ecc71")

        except Exception as e:
            self.resultado.configure(text="⚠️ Entrada inválida. Use número real e precisão inteira ≥ 0.", text_color="#e74c3c")


# Inicializar Janela
root = CTk()
root.title("Conversor Decimal → Binário")
root.geometry("420x400")
App(root)
root.mainloop()
