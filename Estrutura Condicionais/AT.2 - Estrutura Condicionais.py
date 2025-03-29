nomeVilão1 = str(input())
PoderVilão1 = int(input())
LocalVilão1 = int(input())
NomeVilão2 = str(input())
PoderVilão2 = int(input())
LocalVilão2 = int(input())

poder1 = (PoderVilão1**2*LocalVilão1)/2
poder2 = ( PoderVilão2**2*LocalVilão2)/2

if PoderVilão1 < 0 or PoderVilão2 < 0:
  print("Nem faco essa comparacao! Quero ser um vingador, busco coisas maiores.")
  
elif poder1 > poder2:
    print(f"Com grandes poderes, vem grandes responsabilidades. Com isso, preciso ir deter o {nomeVilão1}.")

elif poder2 > poder1:
    print(f"Com grandes poderes, vem grandes responsabilidades. Com isso, preciso ir deter o {NomeVilão2}.")
    
elif poder1 % 2 == 0:
    print("E quem disse que isso e problema meu? Vou chamar o senhor Stark.")
    
else:
    print("Vou chamar uns reforcos de outro universo... rsrs")