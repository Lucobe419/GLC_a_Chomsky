from Escribir_GLC import *
from Funciones import *
from os import system


# Insertar la nueva variable inicial
def nueva_variable_inicial(variables, reglas, mayusculas, paso):
    reglas.insert(0, [variables[0]])

    if 'S' not in variables:
        variables.insert(0, 'S')
    else:
        variables.insert(0, asignar_variable(mayusculas, variables))

    with open('glc_a_chomsky.txt', 'a', encoding='utf-8') as file:
        file.write(f'\nPaso {paso}: Nueva variable inicial {variables[0]}\n')
    print(f'Paso {paso}: Nueva variable inicial {variables[0]}')
    escribir_glc(variables, reglas)
    glc_to_text(variables, reglas)

    paso += 1

    input("\nPresione Enter para continuar")
    system('cls')

    return paso


def eliminar_epsilon(variables, reglas, paso, epsilon):
    hay_epsilon = True  # Si hay un epsilon, sigue buscando otro
    var = 'sin epsilon'  # Por si no hay epsilon

    while hay_epsilon is True:
        hay_epsilon = False
        solo_epsilon = False

        for i in range(1, len(variables)):
            if epsilon in reglas[i]:
                var = variables[i]  # Identificar la variable con epsilon
                hay_epsilon = True
                index_var = i  # El indice de la variable para borrar su epsilon y posiblemente la variable
                if len(reglas[i]) == 1:
                    solo_epsilon = True
                break

        if hay_epsilon is True:
            with open('glc_a_chomsky.txt', 'a', encoding='utf-8') as file:
                file.write(f'\nPaso {paso}: Eliminar {epsilon} de la variable {var}\n')
            print(f'Paso {paso}: Eliminar {epsilon} de la variable {var}')

            paso += 1

            if solo_epsilon is True:
                eliminar_variable(var, reglas, epsilon)
                variables.pop(index_var)
                reglas.pop(index_var)

            else:
                variantes_de_epsilon(var, variables, reglas, epsilon)
                reglas[index_var].remove(epsilon)

            quitar_reglas_repetidas(reglas)
            escribir_glc(variables, reglas)
            glc_to_text(variables, reglas)
            input("\nPresione Enter para continuar")
            system('cls')

        elif var == 'sin epsilon':
            with open('glc_a_chomsky.txt', 'a', encoding='utf-8') as file:
                file.write(f'\nPaso {paso}:\nNo hay {epsilon}, por lo que no se hace nada\n')
            print(f'Paso {paso}:\nNo hay {epsilon}, por lo que no se hace nada')
            escribir_glc(variables, reglas)
            glc_to_text(variables, reglas)

            paso += 1

            input("\nPresione Enter para continuar")
            system('cls')

    return paso


def eliminar_reglas_unitarias(variables, reglas, paso, epsilon):
    hay_unitaria = True  # Si hay reglas unitarias, sigue buscando otras
    variable_a_cambiar = 'sin unitaria'  # Por si no hay reglas unitarias

    stop = False  # Para dejar de buscar mismas variables

    while hay_unitaria is True:
        hay_unitaria = False
        misma_variable = False  # Por si la regla esta en la misma variable (S -> S)

        if stop is False:
            for i in range(len(variables)):
                for rule in reglas[i]:
                    if rule in variables and rule == variables[i]:
                        variable_a_cambiar = rule  # La variable a cambiar
                        hay_unitaria = True
                        index_reglas = i  # Para obtener las reglas
                        misma_variable = True
                        break

            if misma_variable is False:
                stop = True

        if stop is True:
            for i in range(len(variables)):
                for rule in reglas[i]:
                    if rule in variables:
                        variable_a_cambiar = rule  # La variable a cambiar
                        hay_unitaria = True
                        index_reglas = i  # Para obtener las reglas
                        break

        if hay_unitaria is True:
            with open('glc_a_chomsky.txt', 'a', encoding='utf-8') as file:
                file.write(f'\nPaso {paso}: Eliminar la regla unitaria {variable_a_cambiar} de la variable {variables[index_reglas]}\n')
            print(f'Paso {paso}: Eliminar la regla unitaria {variable_a_cambiar} de la variable {variables[index_reglas]}')

            paso += 1

            if variable_a_cambiar != variables[index_reglas]:
                for rule in reglas[variables.index(variable_a_cambiar)]:
                    reglas[index_reglas].append(rule)

            reglas[index_reglas].remove(variable_a_cambiar)

            if len(reglas[index_reglas]) == 0:
                eliminar_variable(variables[index_reglas], reglas, epsilon)
                variables.pop(index_reglas)
                reglas.pop(index_reglas)

            quitar_reglas_repetidas(reglas)
            escribir_glc(variables, reglas)
            glc_to_text(variables, reglas)
            input("\nPresione Enter para continuar")
            system('cls')

        elif hay_unitaria == 'sin unitaria':
            with open('glc_a_chomsky.txt', 'a', encoding='utf-8') as file:
                file.write(f'\nPaso {paso}:\nNo hay reglas unitarias, por lo que no se hace nada\n')
            print(f'Paso {paso}:\nNo hay reglas unitarias, por lo que no se hace nada')
            escribir_glc(variables, reglas)
            glc_to_text(variables, reglas)

            paso += 1

            input('\nPresione Enter para continuar')
            system('cls')

    return paso


def reducir_reglas_grandes(variables, reglas, mayusculas, paso):
    hay_regla_grande = True  # Si hay reglas grandes, sigue buscando otras
    regla_a_cambiar = 'sin regla grande'  # Por si no hay reglas grandes

    while hay_regla_grande is True:
        hay_regla_grande = False

        for rules in reglas:
            for single_rule in rules:
                if len(single_rule) >= 3:
                    new_var = asignar_variable(mayusculas, variables)
                    regla_a_cambiar = single_rule[:2]
                    hay_regla_grande = True
                    break

        if hay_regla_grande is True:
            with open('glc_a_chomsky.txt', 'a', encoding='utf-8') as file:
                file.write(f"\nPaso {paso}: Cambiar '{regla_a_cambiar}' por {new_var} en todas las reglas grandes\n")
            print(f"Paso {paso}: Cambiar '{regla_a_cambiar}' por {new_var} en todas las reglas grandes")

            paso += 1

            variables.append(new_var)
            reglas.append([regla_a_cambiar])

            for i in range(len(reglas)):
                index = 0
                for rule in reglas[i]:
                    if len(rule) >= 3 and regla_a_cambiar in rule:
                        reglas[i][index] = rule.replace(regla_a_cambiar, new_var)
                    index += 1

            escribir_glc(variables, reglas)
            glc_to_text(variables, reglas)
            input('\nPresione Enter para continuar')
            system('cls')

        elif regla_a_cambiar == 'sin regla grande':
            with open('glc_a_chomsky.txt', 'a', encoding='utf-8') as file:
                file.write(f'\nPaso {paso}:\nNo hay reglas para reducir, por lo que no se hace nada\n')
            print(f'Paso {paso}:\nNo hay reglas para reducir, por lo que no se hace nada')
            escribir_glc(variables, reglas)
            glc_to_text(variables, reglas)

            paso += 1

            input('\nPresione Enter para continuar')
            system('cls')

    return paso


# Para cambiar variable y terminal a dos variables
def variable_y_terminal(variables, reglas, mayusculas, paso):
    hay_doble = True  # Para saber si hay variable y terminal
    terminal = 'no hay'  # Por si no hay variable y terminal

    while hay_doble is True:
        hay_doble = False

        for i in range(len(reglas)):
            for rule in reglas[i]:
                if len(rule) == 2:
                    if rule[0] not in variables:
                        terminal = rule[0]
                        new_var = asignar_variable(mayusculas, variables)
                        hay_doble = True
                        break

                    elif rule[1] not in variables:
                        terminal = rule[1]
                        new_var = asignar_variable(mayusculas, variables)
                        hay_doble = True
                        break

        if hay_doble is True:
            with open('glc_a_chomsky.txt', 'a', encoding='utf-8') as file:
                file.write(f"\nPaso {paso}: Cambiar la terminal '{terminal}' por {new_var} donde tambien haya una variable\n")
            print(f"Paso {paso}: Cambiar la terminal '{terminal}' por {new_var} donde tambien haya una variable")

            paso += 1

            variables.append(new_var)
            reglas.append(terminal)

            for i in range(len(reglas)):
                index = 0
                for rule in reglas[i]:
                    if len(rule) == 2:
                        reglas[i][index] = rule.replace(terminal, new_var)
                    index += 1

            escribir_glc(variables, reglas)
            glc_to_text(variables, reglas)
            input('\nPresione Enter para continuar')
            system('cls')

        elif terminal == 'no hay':
            with open('glc_a_chomsky.txt', 'a', encoding='utf-8') as file:
                file.write(f'\nPaso {paso}:\nNo hay reglas con variable y terminal, por lo que no se hace nada\n')
            print(f'Paso {paso}:\nNo hay reglas con variable y terminal, por lo que no se hace nada')
            escribir_glc(variables, reglas)
            glc_to_text(variables, reglas)

            paso += 1

            input('\nPresione Enter para continuar')
            system('cls')

    return paso
