# -*- coding: utf-8 -*-
# !/usr/bin/pytho


while True:
    try:
        print('\n')
        contenedor = float(input('-Bin size: '))
        if contenedor <= 0:
            print(u'\n # Error: ¡¡¡ It must be major than zero !!!  #\n')
        else:
            break
    except:
        print(u'\n #  Error: ¡¡¡ It must be a number !!!  #\n')


##--------------------------------------------------------------------------------------
# Introducimos la lista de elemntos con sus tamaños
##--------------------------------------------------------------------------------------

elementos = input( "List of elements sizes:" )
lista_elementos = input( "List of element's names: " )


##---------------------------------------------------------------------------------------
# Comprobamos que ninguna elemento sea demasiado grande
##---------------------------------------------------------------------------------------

eleccion = ''
lista_elementos_borrar = []

for i in range(len(lista_elementos)):
    if sizes[i] > contenedor:
        elemento_grande = lista_elementos[sizes.index(sizes[i])]

        # mensaje de error-------------------------------------------------------------
        frase1 = '## El elemento "' + \
        elemento_grande + '" es demasiado grande.'
        frase2 = '## Ocupa ' + str(sizes[i]) + '(MB);' + 'es mayor de ' + str(contenedor) + '(MB).'

        if len(frase1) > len(frase2):
            frase2 += (len(frase1) - len(frase2)) * ' ' + '##'
            frase1 += '##'
        elif len(frase1) < len(frase2):
            frase1 += (len(frase2) - len(frase1)) * ' ' + '##'
            frase2 += '##'
        else:
            frase1 += ' ##'
            frase2 += ' ##'

        print('\n')
        print(max(len(frase1), len(frase2)) * '#')
        print(frase1)
        print(frase2)
        print(max(len(frase1), len(frase2)) * '#' + '\n')
        # --------------------------------------------------------------mensaje de error

        if eleccion != 'i':

            while True:
                eleccion = input(' Introduzca:\n -Para continuar e ignorarla "c":\n '
                '-Para ignorar todas "i":\n -Para salir "s":\n')
                if eleccion == 's':
                    fo.close()
                    osremove(donde_abrir)
                    print('\n')
                    print('  #########################################')
                    print('  ###             Saliendo              ###')
                    print('  #########################################\n')
                    sleep(1.5)
                    sysexit()
                elif (eleccion == 'c') or (eleccion == 'i'):
                    lista_elementos_borrar += [elemento_grande]
                    break
                else:
                    print(' *** siga las indicaciones ***\n')
        else:
            lista_elementos_borrar += [elemento_grande]

if len(lista_elementos_borrar) == 1:
    fo.write('  ' + str(lista_elementos_borrar) + ' es demasiado grande.\n\n\n')
elif len(lista_elementos_borrar) > 1:
    fo.write('  ' + str(lista_elementos_borrar) + ' son demasiado grandes.\n\n\n')

# eliminamos de los tamaños y de la lista de elementos que sobrepasan el espaico asignado

for i in lista_elementos_borrar:
    sizes.remove(sizes[lista_elementos.index(i)])
    lista_elementos.remove(i)


input('  ...presiona ENTER para continuar:\n')

print('\n Calculando...\n')
print(' Espere por favor.\n Esto puede tardar un rato...\n\n')

try:
    while ne.evaluate('sum(subsizes)') > contenedor:

        n_grupo += 1

        total = len(sublista_elementos)  # número total de elementos

    #----------------------------------------------------------------------------------------
    # Realizamos todas las combinaciones posibles
    #----------------------------------------------------------------------------------------

        suma = 0

        for i in range(len(subsizes)):
            suma += sorted(subsizes)[i]
            if suma > contenedor:
                nmax = i  # los máximos elementos que cabrían (uno menos que el de la condición)
                break

        start_time = time()  # ttttttttttttt  medimos el tiempo de ejecucion tttttttttttttt

        for i in range(1, 2 ** total):
            vector_bin_ = vector_binario(i, len(subsizes))
            A_ = np.zeros(len(subsizes))

            for j in range(len(vector_bin_)):
                if ne.evaluate('sum(vector_bin_)') > nmax:
                    break
                A_[j] = vector_bin_[j] * subsizes[j]  # todas las combinaciones posibles

            #sustituyo el valor por el actual si se acerca más al valor del contenedor sin pasarse
            try:
                resto_ = contenedor - ne.evaluate('sum(A_)')
                if i == 1:
                    A = A_  # será el primero
                    vector_bin = vector_bin_
                    resto = contenedor - ne.evaluate('sum(A)')  # nuevo resto
                elif (resto_ < resto) and (resto_ >= 0):
                    A = A_  # sustituyo el actual por el anterior
                    vector_bin = vector_bin_
                    resto = contenedor - ne.evaluate('sum(A)')  # nuevo resto
            except:
                print('error')
