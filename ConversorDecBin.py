import math
import decimal

num=float(input("Determine o valor em decimal:"))
num_digitado=float(num)
round(num, 3)

def decPARAbin(num, base, pres):
  num=str(num)
  parte_int=int(num[:num.index(".")])
  parte_frac=float (num[num.index("."):])

  output = ""

  while parte_int!=0:
        output=str(parte_int%base)+output
        parte_int//=base
  if parte_frac==0:
    return output

  output+="."

  while parte_frac !=0 and pres != 0:
       parte_frac*=base
       parte_frac_string=str(parte_frac)
       output+=parte_frac_string[:parte_frac_string.index(".")]
       parte_frac=float(parte_frac_string[parte_frac_string.index("."):])
       pres-=1
  return output

print ("Valor em decimal", "%.3f" %num , "é" , decPARAbin(num, 2, 10) )