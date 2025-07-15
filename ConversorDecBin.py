from tkinter import *

class App:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "10")

        # Frame 1
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 20
        self.primeiroContainer.pack()

        # Frame 2
        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()

        # Frame 3
        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()

        # Frame 4
        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()

        # Título
        self.titulo = Label(self.primeiroContainer, text="Digite o valor para ser convertido")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        # Valor
        self.valorLabel = Label(self.segundoContainer, text="Valor", font=self.fontePadrao)
        self.valorLabel.pack(side=LEFT)
        self.valor = Entry(self.segundoContainer, width=15, font=self.fontePadrao)
        self.valor.pack(side=LEFT)

        # Precisão
        self.precisaoLabel = Label(self.terceiroContainer, text="Precisão", font=self.fontePadrao)
        self.precisaoLabel.pack(side=LEFT)
        self.precisao = Entry(self.terceiroContainer, width=15, font=self.fontePadrao)
        self.precisao.pack(side=LEFT)

        # Botão Converter
        self.conversor = Button(self.quartoContainer, text="Converter", font=("Calibri", "8"),
                                width=12, command=self.decPARAbin)
        self.conversor.pack()

        # Mensagem Resultado
        self.mensagem = Label(self.quartoContainer, text="", font=self.fontePadrao)
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
                self.mensagem["text"] = output
                return

            output += "."
            while parte_frac != 0 and pres > 0:
                parte_frac *= 2
                bit = int(parte_frac)
                output += str(bit)
                parte_frac -= bit
                pres -= 1

            self.mensagem["text"] = output

        except ValueError:
            self.mensagem["text"] = "Entrada inválida. Use números reais e precisão inteira."

root = Tk()
root.title("Conversor Decimal → Binário")
App(root)
root.mainloop()
