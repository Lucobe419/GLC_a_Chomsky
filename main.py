from os import system, startfile
from Escribir_GLC import *
from Crear_GLC import *
from Pasos import *

mayusculas = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
variables = []
reglas = []
paso = 1
epsilon = chr(949)

crear_glc(variables, reglas, mayusculas, epsilon)
system('cls')

with open('glc_a_chomsky.txt', 'w') as file:
    file.write('GLC a utilizar:\n')
escribir_glc(variables, reglas)
glc_to_text(variables, reglas)

input('Esta es la GLC con la que se trabajara. Para ver los pasos, presione Enter\n')
system('cls')

# Paso 1: Asignar nueva variable inicial
paso = nueva_variable_inicial(variables, reglas, mayusculas, paso)

# Paso 2: Eliminar epsilon de las reglas
paso = eliminar_epsilon(variables, reglas, paso, epsilon)

# Paso 3: Eliminar las reglas unitarias
paso = eliminar_reglas_unitarias(variables, reglas, paso, epsilon)

# Paso 4: Reducir reglas grandes (>3)
paso = reducir_reglas_grandes(variables, reglas, mayusculas, paso)

# Paso 5: Variable y terminal
paso = variable_y_terminal(variables, reglas, mayusculas, paso)

# Final
with open('glc_a_chomsky.txt', 'a', encoding='utf-8') as file:
    file.write('\nResultado Final:\n')
print('Resultado Final:')
escribir_glc(variables, reglas)
glc_to_text(variables, reglas)
input("\nPresione Enter para finalizar")

startfile('glc_a_chomsky.txt')
