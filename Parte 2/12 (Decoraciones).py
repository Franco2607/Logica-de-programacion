# Sirve para añadirle una funcionabilidad extra a otra funcion de manera elegante

def decorador(function):
    def print_function():
        print(f"La función '{function.__name__}' ha sido llamada.")
        return function
    return print_function


@decorador
def Funcion_ejm():
    pass


@decorador
def Funcion_ejm2():
    pass


@decorador
def Funcion_ejm3():
    pass


Funcion_ejm()
Funcion_ejm2()
Funcion_ejm3()


# Extra



def Llamar_contador(function):
    def Fun_contador():
        Fun_contador.call_count += 1
        print(
            f"La función '{function.__name__} se ha llamado {Fun_contador.call_count}' veces.")
        return function

    Fun_contador.call_count = 0
    return Fun_contador


@Llamar_contador
def Funcion_ejm4():
    pass


@Llamar_contador 
def Funcion_ejm5():
    pass


Funcion_ejm4()
Funcion_ejm4()
Funcion_ejm4()
Funcion_ejm4()
Funcion_ejm5()
Funcion_ejm4()
Funcion_ejm5()