# Input
num = float(input("Determine o valor em decimal:"))

def decPARAbin(num, pres):
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
        return output

    output += "."  # Adiciona ponto para a parte fracionária

    # Converte parte fracionária para binário
    while parte_frac != 0 and pres != 0:
        parte_frac *= 2
        parte_frac_string = str(parte_frac)
        output += parte_frac_string[:parte_frac_string.index(".")]
        parte_frac = float(parte_frac_string[parte_frac_string.index("."):])
        pres -= 1

    return output  # Retorna o binário

print("Valor em decimal", "%.3f" % num, "é", decPARAbin(num, 10))
