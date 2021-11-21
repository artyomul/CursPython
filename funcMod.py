#suma tuturor nr de la 0 la n
def get_suma(n):
    if not n:
        return 0
    return n + get_suma(n - 1)

#suma nr pare
def get_par(n):
    if not n:
        return 0
    if n % 2:
        return get_par(n - 1)
    else:
        return n + get_par(n - 1)

#impare
def get_impar(n):
    if not n:
        return 0
    if not n % 2:
        return get_impar(n - 1)
    else:
        return n + get_impar(n - 1)