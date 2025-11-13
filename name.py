from funciones import suma
from calculos import triangulo
from calculos import cuadrado
from calculos import circulo

print(13,11,2025)

while True :
    print("Menu ")
    print("1.suma")
    print("2.area de triangulo")
    print("3.area de cuadrado")
    print("4.area del circulo")
    print("5.salir")

    opcion = input("Eliga una opcion : ")

    if opcion == "1" :
        a = float(input("ingrese el primer numero:")) 
        b = float (input("ingrese el  segundo numero:"))
        resultado = suma(a,b)
        print("la suma es :", resultado)
       
    elif opcion == "2" :
         base = float(input("ingrese la base del triangulo :"))
         altura = float(input("ingrese la altura del triangulo:"))
         resultado1 = triangulo(base, altura)
         print("El área del triángulo es:", resultado1)

    elif opcion == "3" :
        lado = float(input("ingrese el lado el cuadrado:"))
        resultado2 = cuadrado(lado * lado)
        print("el area del cuadrado es :", resultado2)

    elif opcion == "4" :
       radio = float(input("Ingrese el radio: "))
       resultado3 = circulo(radio)
       print("El área del círculo es:", resultado3)



