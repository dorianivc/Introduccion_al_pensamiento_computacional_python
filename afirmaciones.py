def primera_letra(lista_de_palabras):
    """Se recibe una lista de palabras
    Aplicamos asserts para hacer afirmacion de entradas de variables

    """
    primeras_letras=[]
    for palabra in lista_de_palabras:
        assert type(palabra)== str, f'{palabra} no es un str'
        assert len(palabra) > 0, 'No se permiten str vacios'

        primeras_letras.append(palabra[0])

    return primeras_letras

#La lista comentada es para probar el assert(Afirmacion)
#lista=['Dorian','Vallecillo','1', '','Ricardo', '-', '  ']
lista=['Diagrama','Origen','Rigor', 'Insert','Antagonismo', 'Nanomecanica']
print(primera_letra(lista))