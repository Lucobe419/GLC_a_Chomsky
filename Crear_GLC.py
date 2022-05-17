from os import system
from Escribir_GLC import *

# Funcion que permite al usuario crear un GLC
def crear_glc(variables, reglas, mayusculas, epsilon):
    glc_completa = False

    # Si la GLC tiene variables inaccesibles, que se sigan agregando reglas
    while glc_completa is False:
        variable = 'A'

        # Revisar que todavia se quieran agregar reglas
        while variable.lower() != 'terminar' and variable != '':
            checar_variable = False

            # Revisar que el valor escrito sea una variable o diga 'terminar'
            while checar_variable is False:
                system('cls')
                checar_variable = True

                escribir_glc(variables, reglas)

                variable = input("Escribe una variable. Si ya terminaste, escribe 'terminar':\n").upper()

                if variable not in mayusculas and variable.lower() != 'terminar' and variable != '':
                    checar_variable = False

            # Si se escribio una variable, escribir una regla
            regla = ''
            while variable in mayusculas and regla == '':
                if variable not in variables:
                    variables.append(variable)
                    reglas.append([])

                regla = input(f"Escribe una regla para la variable {variable}. Si quieres {epsilon}, escribe 'epsilon':\n")

                # Revisar que no se escriba epsilon 2 veces en una misma variable
                if regla.lower() == 'epsilon':
                    if epsilon not in reglas[variables.index(variable)]:
                        reglas[variables.index(variable)].append(epsilon)
                else:
                    if regla not in reglas[variables.index(variable)]:
                        reglas[variables.index(variable)].append(regla)

        # Revisar que todas las variables puedan ser accesadas
        contador_variables = 0
        for var in variables:
            variable_util = False

            # Si solo hay una variable, entonces es buena
            if len(variables) == 1:
                variable_util = True

            # Si hay mas de una variable, revisarlas
            else:
                # Revisar que la primer variable pueda llamar otras variables
                if var == variables[0]:
                    for rule in reglas[0]:
                        for char in rule:
                            if char in variables and char != var:
                                variable_util = True
                                break

                # Revisa que las variables puedan ser accedidas
                else:
                    for rules in reglas:
                        if reglas.index(rules) != variables.index(var):
                            for single_rule in rules:
                                if var in single_rule:
                                    variable_util = True
                                    break

            # Si todas las variables pueden ser accedidas, la GLC esta completa
            if variable_util is True:
                contador_variables += 1

            if contador_variables == len(variables):
                glc_completa = True
