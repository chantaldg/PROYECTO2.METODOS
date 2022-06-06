#CHANTAL DE GRACIA, DANIELA MOSCOSO

from sys import stdin
stdin

def falsi (funcion, x_i,x_f, iteraciones = 20, error_r = 0.001):
    #inicializar las variables
    solucion = None
    contador = 0
    error_calculado= 100
    #Evaluar si la raiz esta dentro del intervalo
    if funcion(x_i) * funcion(x_f) <= 0:
        #si se cumple la condición de arriba, se puede calcular la solucion
        while contador <= iteraciones and error_calculado >= error_r:
            contador +=1
            solucion = x_f - ((funcion(x_f) * (x_f - x_i))/ (funcion(x_f)- funcion (x_i))) #formula REGULA FALSI
            error_calculado = abs((solucion-x_i)/ solucion) * 100
            #redefinir el nuevo intervalo
            if funcion(x_i) * funcion (solucion) >= 0:
                x_i = solucion #Xi toma el valor que adquiere arriba (variable temporal)
            else:
                x_f = solucion  #Xf toma el valor que adquiere arriba (variable temporal)        
        print ('La solución aproximada es: {:.3f}'.format(solucion))
        print('Encontrada en: {:.0f}' .format(contador) + ' iteraciones.')
        print('Tiene un error relativo de: {:.3f}'.format(error_calculado) + '%')
    else:
        print("No existe una solución para este intevalo")
        #Esta condicion se cumple si la multiplicación en el if no se cumple

#Captura de datos
funcion = eval("lambda x: " + input ("Ingrese la función: "))
x_i = int (input("El inicio del intervalo es: "))
x_f= int (input("El final del intervalo es: "))
#Se le agregan los parametros capturados a la funcion
falsi(funcion,x_i,x_f)
