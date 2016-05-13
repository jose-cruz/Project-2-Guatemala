#Jose Alejandro Cruz, 09368
#Miguel Zea,
#El lobo, la oveja y la lechuga"
#Debemos llevar a la lechuga, la oveja y el lobo al otro lado del rio,
#pero hay un problema. Si dejamos al lobo y a la oveja solos, sin alguien
#que los cuide, de un lado del rio, el lobo se comera a la oveja. Asi
#como si dejamos a la oveja y a la lechuga, sin alguien que los cuide,
#de un lado del rio, la oveja se comera la lechuga.

#Definimos las variables que nos ayudaran a controlar el programa.
lado1 = ['lechuga', 'oveja', 'lobo']#Esta lista es el lado 1 del rio, aqui empiezan definidos el lobo, la oveja y la lechuga
lado2 = []#Esta lista es el lado 2 del rio, en el momento que todos llegan a este lado, el juego termina. 
barco = 'lado 1' #Este es el barco, gracias a esta variable evitamos que el juego se termine cuando estan del mismo lado la oveja y la lechuga o el lobo.
seguir_jugando = ''#Esta variable determina si seguimos jugando, cambiara cuando termine el juego.
print 'INSTRUCCIONES:'#Imprimimos las instrucciones del juego.
print 'Debemos llevar a la lechuga, la oveja y el lobo al otro lado del rio,'
print 'pero hay un problema. Si dejamos al lobo y a la oveja solos, sin alguien'
print 'que los cuide, de un lado del rio, el lobo se comera a la oveja. Asi'
print 'como si dejamos a la oveja y a la lechuga, sin alguien que los cuide,'
print 'de un lado del rio, la oveja se comera la lechuga.'
#Con esta definicion evaluamos si nuestro ingreso es valido (se encuentra dentro de alguna de las 2 listas)
def pick():
    d1 = raw_input('''Escoger que desea mover al otro lado
del rio: "lechuga", "oveja", "lobo" o "ninguno": ''')
    prueba1 = d1 in lado1
    prueba2 = d1 in lado2
    if prueba1 == True:
        return d1
    elif prueba2 == True:
        return d1
    elif d1 == 'ninguno':
        return d1
    else:
        print 'ERROR: Seleccion no valida, por favor intente de nuevo'
        juego()
#Al comprobar que la seleccion existe, debemos comprobar que esta este del mismo lado que el barco. Y devuelve el valor que tiene dentro de la lista en la que esta.
def decision(x):
    ind = ''
    prueba1 = x in lado1
    prueba2 = x in lado2
    if prueba1 == True:
        if barco == 'lado 1':
            ind = lado1.index(x)
        elif barco =='lado 2':
            print 'ERROR: Su seleccion esta del otro lado del barco, por favor intente de nuevo'
            juego()
    elif prueba2 == True:
        if barco == 'lado 2':
            ind = lado2.index(x)
        elif barco == 'lado 1':
            print 'ERROR: Su seleccion esta del otro lado del barco, por favor intente de nuevo'
            juego()
    elif x == 'ninguno':#La unica excepcion, es la opcion de "ninguno", con esta devuelve un valor str "mover"
        ind = 'mover'
    return ind
#Al comprobar todas las condiciones anteriores, debemos mover nuestra eleccion al otro lado, asi mismo, debemos mover el barco al otro lado tambien. 
def mover(x, y, z):
    prueba1 = y in lado1
    prueba2 = y in lado2
    if x == 'mover': #Con este if, evaluamos si nuestra eleccion fue "ninguna", y de esta forma solo movemos al barco al otro lado.
        if z == 'lado 1':
            z = 'lado 2'
        elif z == 'lado 2':
            z = 'lado 1'
    if prueba1 == True:
        cambio = lado1.pop(x)
        lado2.append(cambio)
        z = 'lado 2'
    if prueba2 == True:
        cambio = lado2.pop(x)
        lado1.append(cambio)
        z = 'lado 1'
    return z
#Y finalmente, despues de mover, evaluamos si la lechuga y la oveja estan solas de un lado, o bien, si la oveja y el lobo estan solos de un lado.
def prueba(x):
    p = 0
    global lado1
    global lado2
    P1L1 = 'lechuga' in lado1
    P1L2 = 'lechuga' in lado2
    P2L1 = 'oveja' in lado1
    P2L2 = 'oveja' in lado2
    P3L1 = 'lobo' in lado1
    P3L2 = 'lobo' in lado2
    if P1L1 == True:
        if P2L1 == True:
            if not x == 'lado 1':
                p = 1
    if P1L2 == True:
        if P2L2 == True:
            if not x == 'lado 2':
                p = 1
    if P2L1 == True:
        if P3L1 == True:
            if not x == 'lado 1':
                p = 1
    if P2L2 == True:
        if P3L2 == True:
            if not x == 'lado 2':
                p = 1
    return p #Finalmente, retornamos el valor de "p", si este es 0 es porque no hay estan juntos ninguno de las 2 condiciones decritas arriba, si "p" es igual a 1 es porque alguna de las condiciones de arriba si se cumple.
#Con esta definicion ponemos todo junto, ademas imprime un pequeño "rio" de asteriscos que nos ayuda a visualizar el juego. 
def juego():
    global barco
    while len(lado2) < 3:
        op = pick() #ingrsamos en esta variable el retorno de "pick" 
        pos = decision(op) #Aqui ingresamos el retorno de "decision", y usamos de parametro a "op" 
        barco = mover(pos, op, barco) # En esta variable, ingresamos el valor del retorno de "mover" y usamos de parametros a "op", "pos" y al valor anterios de "barco".
        perdio = prueba(barco) #En esta variable ingresamos el valor de retorno de "prueba", con el parametro de "barco"
        if perdio == 1: # Si el valor de "perdio" es igual a 1, el ciclo se termina. 
            break
        if barco == 'lado 1': 
            print '--------LADO 1--------'
            print '**********************'
            print lado1, 'barco'
            print '**********************'
            print '**********************'
            print '**********************'
            print '**********************'
            print '**********************'
            print '**********************'
            print '**********************'
            print lado2
            print '**********************'
            print '--------LADO 2--------'
        elif barco == 'lado 2':
            print '--------LADO 1--------'
            print '**********************'
            print lado1
            print '**********************'
            print '**********************'
            print '**********************'
            print '**********************'
            print '**********************'
            print '**********************'
            print '**********************'
            print lado2, 'barco'
            print '**********************'
            print '--------LADO 2--------'
    return perdio #Retornamos el valor de perdio. 
#En este ciclo, se define hasta que momento seguir jugando, en este caso, hasta que la variable "segui_jugando" sea igual a "no".  Esto se evalua al final de cada juego, independientemente si gano o perdio, 
while seguir_jugando != 'no':
    #Nos aseguramos de que todas las variables importantes esten en orden, y donde deben empezar al principio del juego. 
    lado1 = ['lechuga', 'oveja', 'lobo']
    lado2 = []
    barco = 'lado 1'
    #Imprimimos un plano inicial del "rio", para referencia visual. 
    print '--------LADO 1--------'
    print '**********************'
    print lado1, 'barco'
    print '*********************'
    print '*********************'
    print '**********************'
    print '**********************'
    print '**********************'
    print '**********************'
    print '**********************'
    print lado2
    print '**********************'
    print '--------LADO 2--------'
    game_over = juego() #En esta variable ingresamos el valor de "juego", para evaluar si perdio o gano. 
    if game_over == 0: #Si la variable es 0, este gano y se muestra este mensaje, seguido por el nuevo ingreso de la variable "seguir_jugando". 
        print 'Felicidades!!!! Ha ganado!!'
        seguir_jugando = raw_input('Desea jugar de nuevo? si/no: ')
    else: #Si la variable es 1, este perdio, y se muestra este mensaje, seguido por el nuevo ingreso de la variable "seguir_jugando".
        print 'Ud. a perdido'
        seguir_jugando = raw_input('Desea jugar de nuevo? si/no: ')
print 'Gracias por jugar!' #Y finalmente damos las gracias por jugar.
