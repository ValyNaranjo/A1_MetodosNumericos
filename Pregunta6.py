import math

print("Programa que encuentra el sen(pi/3) y trunca en 50 \n")

#Código en grados, en este caso se utilizará el 60
x_deg = float(input("Ingrese el número que desee resolver en grados "))
print("\n")

#Código para cambiar el valor a radianes
x = math.radians(x_deg)

n = int(input("Ingrese el número en el que desee truncar "))
print("\n")

sen_x = 0.0

print("{:^2}{:^15}{:^1}".format("Término", "Dato", "Sen(x)"))

#Procedimiento de la serie de Taylor
for d in range(n):
     sen_x = sen_x + (-1)**d*x**(2*d+1) / math.factorial((2*d+1))
     print("{:^2}{:^15}{:^1}".format(d+1, d, sen_x))
