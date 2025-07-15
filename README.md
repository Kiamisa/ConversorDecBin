# 🔢 Conversor Decimal para Binário com Precisão (Tkinter)

Este projeto é uma interface gráfica simples desenvolvida em Python com a biblioteca `Tkinter` que permite ao usuário converter números decimais (com parte inteira e fracionária) para binário. A precisão da parte fracionária é configurável.

## 🚀 Funcionalidades

- Conversão de números decimais com ponto (ex: `10.625`) para binário.
- Controle do número de casas binárias fracionárias através do campo de **precisão**.
- Interface gráfica simples e responsiva com `Tkinter`.

---

## 💻 Como usar

### 1. Clone o repositório (ou copie o código):
```bash
git clone https://github.com/seu-usuario/conversor-binario-tkinter.git
cd conversor-binario-tkinter
````

### 2. Execute o script Python:

```bash
python conversor.py
```

> **Requisitos:** Python 3.x instalado

---

## 🧠 Exemplos de uso

| Valor Decimal | Precisão | Resultado em Binário |
| ------------- | -------- | -------------------- |
| `10.625`      | `3`      | `1010.101`           |
| `5.2`         | `5`      | `101.00110`          |
| `0.1`         | `8`      | `0.00011001`         |

---

## 📦 Estrutura

* `conversor.py` → Script principal com interface Tkinter
* `README.md` → Este arquivo

---

## ⚙️ Lógica da Conversão

* A parte **inteira** do número é convertida usando divisões sucessivas por 2.
* A parte **fracionária** é convertida multiplicando-se por 2 e extraindo os bits à esquerda do ponto.
* A conversão da parte fracionária para binário para quando:

  * O número termina (`parte_fracionária == 0`), ou
  * O número de casas decimais binárias atinge o valor da **precisão** informada.

---

## 🤝 Contribuição

Contribuições são bem-vindas! Se tiver ideias de melhorias (como suporte a números negativos, limpar campos, copiar resultado etc), abra uma issue ou envie um pull request.
