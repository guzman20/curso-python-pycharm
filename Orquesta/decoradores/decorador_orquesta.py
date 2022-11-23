from Utils.Log_orquesta import log


def log_orquesta(funcion_a_decorar_b):
    def funcion_decorador_c(*args):
        log.debug(f"Antes ejecucion metodo{funcion_a_decorar_b.__name__}")
        funcion_a_decorar_b(*args)
        log.debug(f"Despues ejecucion metodo{funcion_a_decorar_b.__name__}")

    return funcion_decorador_c
