valor1 = int(input())
var = input()
valor2 = int(input())


op = None


if var == "/":
    op = valor1//valor2
    
    
elif var == "+":
    op = valor1 + valor2
    
elif var == "*":
   op = valor1 * valor2
    
elif var == "**":
    op = valor1 ** valor2
    
elif var == "-":
    op = valor1 - valor2
    
elif var == "rad" and valor2 !=0:
    op = int(valor1**(1/valor2))

if op is None:
    print("Luffy, você SUUUUPER não sabe usar isso, chama o Sanji!")
else:
    print(f"O resultado é {op}.")
    