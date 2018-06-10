def sumatoria(n):
    if isinstance(n, int) and (n > 0):
        return suma(n)
    else:
        return "Error"

def suma(n):
    if n == 0:
        return 0
    else:
        return n + suma(n-1)
