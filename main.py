from funcoes_auxiliares.calculo import soma_com_valor_aleatorio
from funcoes_auxiliares.futebol import add_jogadores,validador_de_campos_obrigatórios 


def main():
    print(soma_com_valor_aleatorio(2))

def main_futebol():
    jogadores = [
         {
        "nome": "Robert Lewandowski",
        "time": "Bayern Munich",
        "salario": 750000
    },
    {
        "nome": "Kevin De Bruyne",
        "time": "Manchester City",
        "salario": 800000 
    },
    ]

    jogador =  {
        "nome": "Kylian Mbappé",
        "time": "Paris Saint-Germain",
        "salario": 950000
    }
    print(add_jogadores(*jogadores))
    # validador_de_campos_obrigatórios(**jogador)
    


if __name__ == "__main__":
    # main()
    main_futebol()