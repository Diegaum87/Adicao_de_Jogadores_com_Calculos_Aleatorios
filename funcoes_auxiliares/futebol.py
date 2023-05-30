from data import jogadores


def add_jogadores(*args):
    # print(f"[add_jogador] -> {args}") 

# adicionar o jogador dentro da lista...
    for jogador in args:
       validador_de_campos_obrigatórios(**jogador)
       jogadores.append(jogador)

    return jogadores

def validador_de_campos_obrigatórios(**kwargs):
    # print(f"[validador_de_campos_obrigatórios] -> {kwargs}") 

    obrigatorios ={"nome", "time", "salario",}
    recebidos = set(kwargs)
    teste = obrigatorios.intersection(recebidos)
    # print(f"[validador_de_campos_obrigatórios] -> {teste}") 
    
    # levantamento de erro!
    if len(obrigatorios) != len(obrigatorios.intersection(recebidos)):
        raise ValueError(
            f"faltam(m) alguma(s) chave(s)! {obrigatorios.difference(recebidos)}"
    
        )

    return True