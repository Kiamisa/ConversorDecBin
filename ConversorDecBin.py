from customtkinter import *

class App:
    def __init__(self, master):
        set_appearance_mode("System")  # Pode ser "Dark", "Light" ou "System"
        set_default_color_theme("blue")  # Ou outros temas: "green", "dark-blue"

        self.fontePadrao = ("Arial", 12)

        # Frame 1
        self.primeiroContainer = CTkFrame(master)
        self.primeiroContainer.pack(pady=20)

        # Frame 2
        self.segundoContainer = CTkFrame(master)
        self.segundoContainer.pack(pady=10)

        # Frame 3
        self.terceiroContainer = CTkFrame(master)
        self.terceiroContainer.pack(pady=10)

        # Frame 4
        self.quartoContainer = CTkFrame(master)
        self.quartoContainer.pack(pady=20)

        # Título
        self.titulo = CTkLabel(self.primeiroContainer, text="Digite o valor para ser convertido", font=("Arial", 14, "bold"))
        self.titulo.pack()

        # Valor
        self.valorLabel = CTkLabel(self.segundoContainer, text="Valor:", font=self.fontePadrao)
        self.valorLabel.pack(side=LEFT, padx=(0, 10))
        self.valor = CTkEntry(self.segundoContainer, width=150, font=self.fontePadrao)
        self.valor.pack(side=LEFT)

        # Precisão
        self.precisaoLabel = CTkLabel(self.terceiroContainer, text="Precisão:", font=self.fontePadrao)
        self.precisaoLabel.pack(side=LEFT, padx=(0, 10))
        self.precisao = CTkEntry(self.terceiroContainer, width=150, font=self.fontePadrao)
        self.precisao.pack(side=LEFT)

        # Botão Converter
        self.conversor = CTkButton(self.quartoContainer, text="Converter", width=120, command=self.decPARAbin)
        self.conversor.pack(pady=10)

        # Mensagem Resultado
        self.mensagem = CTkLabel(self.quartoContainer, text="", font=self.fontePadrao, text_color="green")
        self.mensagem.pack()

    def decPARAbin(self):
        try:
            num = float(self.valor.get())
            pres = int(self.precisao.get())

            parte_int = int(num)
            parte_frac = num - parte_int

            output = ""
            if parte_int == 0:
                output = "0"
            else:
                while parte_int != 0:
                    output = str(parte_int % 2) + output
                    parte_int //= 2

            if pres == 0 or parte_frac == 0:
                self.mensagem.configure(text=output)
                return

            output += "."
            while parte_frac != 0 and pres > 0:
                parte_frac *= 2
                bit = int(parte_frac)
                output += str(bit)
                parte_frac -= bit
                pres -= 1

            self.mensagem.configure(text=output)

        except ValueError:
            self.mensagem.configure(text="Entrada inválida. Use números reais e precisão inteira.", text_color="red")


# Inicializar Janela
root = CTk()
root.title("Conversor Decimal → Binário")
root.geometry("300x300")
App(root)
root.mainloop()
