# Funcion para escribir el GLC
def escribir_glc(variables, reglas):
    for i in variables:
        print(f'{i} -> ', end='')
        cantidad_reglas = len(reglas[variables.index(i)])
        contador = 1
        for j in reglas[variables.index(i)]:
            if cantidad_reglas == 1 or contador == cantidad_reglas:
                print(j)
            else:
                print(j, end=' | ')
            contador += 1


# Funcion para escribir el GLC a un archivo txt
def glc_to_text(variables, reglas):
    with open('glc_a_chomsky.txt', 'a', encoding='utf-8') as file:
        for i in variables:
            file.write(f'{i} -> ')
            cantidad_reglas = len(reglas[variables.index(i)])
            contador = 1
            for j in reglas[variables.index(i)]:
                if cantidad_reglas == 1 or contador == cantidad_reglas:
                    file.write(f'{j}\n')
                else:
                    file.write(f'{j} | ')
                contador += 1
