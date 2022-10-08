import random
contador1 = ""
contador2 = ""
contador3 = ""
contador4 = ""
contador5 = ""
contador6 = ""
x = int(input("Digite cuantas veces lanzara el dado: "))

for i in range(1,x+1):
    b = random.randint(1,6)
    print("Resultados")
    if b ==1:
        contador1=(contador1+ "*")
    if b ==2:
        contador2=(contador2+ "*")
    if b ==3:
        contador3=(contador3+ "*")
    if b ==4:
        contador4=(contador4+ "*")
    if b ==5:
        contador5=(contador5+ "*")
    if b ==6:
        contador6=(contador6+ "*")
print("El numero de veces que cayo el 1 : " + str(contador1))
print("El numero de veces que cayo el 2 : " + str(contador2))
print("El numero de veces que cayo el 3 : " + str(contador3))
print("El numero de veces que cayo el 4 : " + str(contador4))
print("El numero de veces que cayo el 5 : " + str(contador5))
print("El numero de veces que cayo el 6 : " + str(contador6))