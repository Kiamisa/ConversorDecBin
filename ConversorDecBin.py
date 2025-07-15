from tkinter import *

class App:
    def __init__(self, master=None):
        #Config iniciais
        self.fontePadrao = ("Arial", "10")
        #Frame 1
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()
        #Frame 2
        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()
        #Frame 3
        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()
        #Frame 4
        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()
        #Titulo
        self.titulo = Label(self.primeiroContainer, text="Digite o valor para ser convertido")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()
        #Legenda do input
        self.valorLabel = Label(self.segundoContainer,text="Valor", font=self.fontePadrao)
        self.valorLabel.pack(side=LEFT)
        #Input do Valor
        self.valor = Entry(self.segundoContainer)
        self.valor["width"] = 30
        self.valor["font"] = self.fontePadrao
        self.valorLabel.pack(side=LEFT)
        
        #Valor convertido


    def decPARAbin(self, pres):
        num = self.valor.get()
        num = str(num)  # Converte o número para string
        
        # Separa parte inteira e fracionária
        parte_int = int(num[:num.index(".")])  
        parte_frac = float(num[num.index("."):])

        output = ""  # Output do resultado

        # Converte parte inteira para binário
        while parte_int != 0:
            output = str(parte_int % 2) + output
            parte_int //= 2

        if parte_frac == 0:  # Se não houver parte fracionária
            self.mensagem["text"] = output

        output += "."  # Adiciona ponto para a parte fracionária

        # Converte parte fracionária para binário
        while parte_frac != 0 and pres != 0:
            parte_frac *= 2
            parte_frac_string = str(parte_frac)
            output += parte_frac_string[:parte_frac_string.index(".")]
            parte_frac = float(parte_frac_string[parte_frac_string.index("."):])
            pres -= 1
        self.mensagem["text"] = output

        #return output  # Retorna o binário
root = Tk()
App(root)
root.mainloop()
