from itertools import product, compress
import re


# Para cuando se necesite una nueva variable
def asignar_variable(mayusculas, variables):
    for letra in mayusculas:
        if letra not in variables:
            var = letra
            break
    return var


# Eliminar una variable que ya no se necesita en cada regla
def eliminar_variable(var, reglas, epsilon):
    for i in range(len(reglas)):
        index = 1
        for rule in reglas[i]:
            if var in rule:
                if len(rule) == rule.count(var):
                    reglas[i][index] = rule.replace(var, epsilon)
                else:
                    reglas[i][index] = rule.replace(var, '')


# Generar las variables para la regla eliminada de epsilon
def variantes_de_epsilon(var, variables, reglas, epsilon):
    rules_index = 0  # Para identificar donde agregar las nuevas reglas

    for rules in reglas:
        for single_rule in rules:
            if var in single_rule:
                if len(single_rule) > 1:
                    cantidad_variables = single_rule.count(var)  # Veces que aparece la variable a quitar en la regla
                    var_indexes = [i.start() for i in re.finditer(var, single_rule)]  # Los indices donde aparece la variable
                    opciones = list(product([0, 1], repeat=cantidad_variables))  # Producto cartesiano

                    for option in opciones:
                        if option != opciones[0]:
                            ones = [1] * len(single_rule)  # Arreglo de 1's, sirve para borrar las variables

                            for j in range(cantidad_variables):
                                if option[j] == 1:
                                    ones[var_indexes[j]] = 0

                                    resultado = list(compress(single_rule, ones))
                                    resultado = ''.join(resultado)

                                    if resultado != '':
                                        reglas[rules_index].append(resultado)

                                    elif resultado == '' and var != variables[rules_index]:
                                        reglas.append(epsilon)

                elif var != variables[rules_index]:
                    rules.append(epsilon)

        rules_index += 1


def quitar_reglas_repetidas(reglas):
    for i in range(len(reglas)):
        nuevas_reglas = []
        for rule in reglas[i]:
            if rule not in nuevas_reglas:
                nuevas_reglas.append(rule)
        reglas[i] = nuevas_reglas
