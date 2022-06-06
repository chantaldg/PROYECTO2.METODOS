#CHANTAL DE GRACIA, DANIELA MOSCOSO
from sympy import *
i = 0
x = symbols('x') #La funcion establece un símbolo que se le asigna a una variable.
print('INSERTAR FUNCION: ')
y = sympify(input()) #La funcion sympify convierte strings a expresiones SYMPY
c = float(input('Valor inicial: '))
print("FUNCION : {} ".format(y))

y_derivada = Derivative(y, x) #
	
print(f"DERIVADA : {y_derivada.doit()} ")

#CICLO DE REPETICION PARA LAS ITERACIONES
while(abs(y.evalf(subs={x:c}))>0.0000000001):
  i = i + 1 #CONTADOR ITERACIONES
  a = y.evalf(subs={x:c}) #EVALUACION DE DE LA FUNCION CON EL VALOR INICIAL SUBSTITUIDO
  b = y_derivada.doit().evalf(subs={x:c}) #EVALUACION DE LA FUNCION DERIVADA CON EL VALOR INICIAL SUBSTITUIDO
  #print(a)
  #print(b)
  c = c - a/b #CALCULO DE LA FORMULA
  print("Iteracion #" + str(i) + ": ")
  print('{:.5f}'.format(c))