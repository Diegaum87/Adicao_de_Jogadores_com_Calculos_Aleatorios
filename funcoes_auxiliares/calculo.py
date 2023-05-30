from .geradores_aleatorios import gerador_de_numero


def soma_com_valor_aleatorio(a):
    valor_aleatorio = gerador_de_numero()
    return a + int(valor_aleatorio[-1])

if __name__ == "__main__":
    print(f"[calculo.py] -> {__name__}")