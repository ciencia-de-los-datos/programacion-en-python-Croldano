"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    import csv
    with open("data.csv",newline='') as f:
            datos = csv.reader(f, delimiter='\t')
            colums = list(datos)
        
            suma=0
            for num in colums:
                suma+=int(num[1])

            return suma

   


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    
    import csv
    datos= open('data.csv')
    leercsv= csv.reader(datos)
    lista01=[] #con esta almaceno los datos de la columna 1 del 
    lista02=[] #aquí vamos a meter todas las letras que necesitamos
    dict={} #con el diccionario almacenaremos tanto letras como las cantidades.
    for columna in leercsv: # por cada columna dentro del doc
        lista01.append(columna[0])  # ingrese los datos de la columna 1 a lista01
    for values in lista01:  # por cada dato en la lista 1
        sublista = values.split()[0]  # esta variable almacena la letra que necesitamos
        lista02.append(sublista)  #  los ingresa a la lista
    for letras in lista02:
        dict.setdefault(letras, 0)
        dict[letras] = dict[letras]+1
   
    return sorted(dict.items())
#print(pregunta_02())
 


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
  
    #Lo primero es abrir el archivo
    with open("data.csv", "r") as file:
      datac= file.readlines()
    
    #Ahora para cada f que tenga \n en datac debo reemplazarla por un ""
    #Luego hago split en cada \t en el datac

    datac= [a.replace("\n","") for a in datac]  
    datac=[a.split("\t") for a in datac]

    #para cada a en la columna 0 y cada a en la columna 1 que encuentre en el datac
    columnas= [[a[0],int(a[1])] for a in datac ]

    #set convierte en diccionario y quita duplicado
    id=sorted(set([a[0] for a in datac]))

    contador=0 #usaré contador en dos partes para que este vuelva a cero en vez de acumular el valor de la columna1
    tuplac=[] #creo una lista vacía

    for b in id:
      for a in columnas:
        if a[0]== b:
          contador+= a[1]
        
      tuplac.append((b,contador)) 
      contador=0 
    return tuplac  


  
def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
        #como en los puntos anteriores, abro el archivo
    with open("data.csv","r") as file:
        datad= file.readlines() #leo los datos 
        datad= [f.replace("\n","") for f in datad] #reemplazo para cada f en el datad el \n por ""
        datad= [f.split("\t") for f in datad] #hago split para cada f en datad que contenga \t
    
    lista_fechas=[f[2].split("-") for f in datad ] #para cada f en la columna dos de datad hacer split y usar ""
    lista_meses=[f[1] for f in lista_fechas]
    meses=sorted(set([f for f in lista_meses]))
    tuplad=[(x, lista_meses.count(x)) for x in meses]

    return tuplad
   


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
#como en los puntos anteriores, abro el archivo
    with open("data.csv","r") as file:
        datae=file.readlines()

 #Estos pasos son sacados de los otros puntos, entonces es fácil, repetitivo

 #para cada f encontrado en datae, reemplace \n por "" (nada)   
    datae=[f.replace("\n","")for f in datae]
 #para cada f que encuentre en datae, haga un split en el tabulador que encuentre   
    datae=[f.split("\t") for f in datae]    
    
    id_list=sorted(set([f[0] for f in datae]))
    lista_datae=[(f[0],int(f[1])) for f in datae]
 
  #creo dos listas vacías  
    tuplae=[]
    valores=[]
    

    for b in id_list:
        for a in lista_datae:
            if a[0]== b:
                valores.append(a[1]) #si encuentra que a=b agrega uno en la lista

        tuplae.append((b, max(valores),min(valores)))
        valores.clear() #remueve todos los elementos de la lista

    return tuplae
    


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
   
    with open("data.csv","r") as file:
        dataf=file.readlines()
    dataf=[f.replace("\n","") for f in dataf]
    dataf=[f.split("\t") for f in dataf]
    dataf=[f[4].split(",") for f in dataf]
    
    #puedo reciclar pasos de los puntos anteriores hasta la línea 229 del código

    #Hago una lista clave valor
    Key_value_list= [(b[:3],int(b[4:]))for a in dataf for b in a]

   #la lista va a retornar ordenada gracias a sorted y por medio de set retirará los elementos repetidos. 
    keys_dict=sorted(set(elemento[0] for elemento in Key_value_list ))
    
    valores=[]
    tuplaf=[]
    
    for key in keys_dict:
        for elemento in Key_value_list:
            if elemento[0]== key:
                valores.append(elemento[1]) #lo que hace append es sumarme un elemento a la columna 1
        tuplaf.append((key, min(valores),max(valores)))
        valores.clear()

    return tuplaf


    


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    with open("data.csv","r") as file:
        datag=file.readlines()
    datag=[f.replace("\n","") for f in datag]
    datag=[f.split("\t") for f in datag]
    

    #Debo crear una lista con elementos de la columna 1 y la columna 2
    data_list=[(int(a[1]),a[0]) for a in datag]

    #Debo extraer el conjunto de numeros unicos ordenados en la columna 2 de los datos y eliminar duplicados, para eso es set
    numeros=sorted(set(a[0] for a in data_list))
    
    #Creo dos listas vacías
    tuplag=[]
    letters=[]
    
    #para cada numero extraigo la lista letras que aparecen en la lista de datag
    for b in numeros:
        for a in data_list:
            if a[0]-b == 0:
                letters.append(a[1])    

        tuplag.append((b,letters))
        letters=[]
      
    
    return tuplag    


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    with open("data.csv","r") as file:
        datai=file.readlines()
    datai=[f.replace("\n","") for f in datai]
    datai=[f.split("\t") for f in datai]
    
    #creo una lista que contenga elementos de la columna 2 y la columna 1 respectivamente
    data_list=[(int(a[1]),a[0]) for a in datai]

    #obtengo el conjunto de numeros sin repeticiones (para eso es set) y ordenados (sorted)
    # en la columna #2 de mi data_list
    numeros=sorted(set(a[0] for a in data_list))

    tuplai=[]
    letters=[]
    
    for b in numeros:
        for a in data_list:
            if a[0]-b == 0:
                letters.append(a[1])    

        tuplai.append((b,sorted(set(letters))))
        letters=[]
      
    
    return tuplai
    


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    with open("data.csv","r") as file:
        datah=file.readlines()

    datah=[f.replace("\n","") for f in datah]
    datah=[f.split("\t") for f in datah]
    datah=[f[4].split(",") for f in datah]
    
    #saco cada clave usando string, a su vez, me toca recorrer cada fila y sus elementos
    key_list= [(b[:3])for a in datah for b in a]
    
    #mediante el uso de set, elimino repetidos en key_list
    key_dict=sorted(set( elem for elem in key_list ))
    
    #Creo una tupla y cuento las veces que encuentro cada key
    tuplah=[(a,key_list.count(a))for a in key_dict]
    dict=dict(tuplah)
           
    return dict
    
  


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    return


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    return


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    return
