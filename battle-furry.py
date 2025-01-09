import random

# Definição dos heróis com equilíbrio inicial e pontos fortes
herois = [
    {"nome": "Puppie", "forca": 3000, "defesa": 3000, "velocidade": 4000},
    {"nome": "Twinkee", "forca": 4000, "defesa": 3000, "velocidade": 3000},
    {"nome": "Allepy", "forca": 3000, "defesa": 4000, "velocidade": 3000},
    {"nome": "Whispy", "forca": 3500, "defesa": 3500, "velocidade": 3000},
    {"nome": "Mimzy", "forca": 3000, "defesa": 3500, "velocidade": 3500},
    {"nome": "Blinky", "forca": 3200, "defesa": 3200, "velocidade": 3600},
]

# Definição dos totens com os seus valores
totens = {
    "Luvas do Titã": 1000,
    "Cristal de Fúria": 1000,
    "Porção de Força": 500,
    "Pedra do Poder": 500,
    "Machado Berserker": 1000,
    "Lâmina da Destruição": 1000,
    "Anel do Golpe Devastador": 1000,
    "Totem do Guerreiro Ancestral": 1500,
    "Aura de Armadura": 500,
    "Escudo Divino": 1000,
    "Cota de Malha Mística": 500,
    "Barreira Elemental": 1000,
    "Elmo do Guardião": 500,
    "Amuleto da Proteção Absoluta": 1000,
    "Essência do Rochedo": 1000,
    "Runas do Guardião": 1500,
    "Elixir da Velocidade": 500,
    "Botas Aladas": 1000,
    "Manto do Vento": 500,
    "Adaga da Agilidade": 1000,
    "Braceletes da Celeridade": 1000,
    "Capa das Sombras Rápidas": 1000,
    "Cristal do Teleporte Rápido": 1000,
    "Talismã do Corredor Fantasma": 1500
}

# Função para calcular o poder total
def calcular_poder(heroi, totem):
    poder_base = heroi['forca'] + heroi['defesa'] + heroi['velocidade']
    poder_total = poder_base + totens[totem]
    return poder_total

# Função para determinar o nível do herói com base no poder
def determinar_nivel(poder):
    if poder < 1000:
        nivel = "Ferro"
    elif poder <= 2000:
        nivel = "Bronze"
    elif poder <= 5000:
        nivel = "Prata"
    elif poder <= 7000:
        nivel = "Ouro"
    elif poder <= 8000:
        nivel = "Platina"
    elif poder <= 9000:
        nivel = "Ascendente"
    elif poder <= 10000:
        nivel = "Imortal"
    else:
        nivel = "Radiante"
    return nivel

# Função de batalha
def batalha(heroi1, totem1, heroi2, totem2):
    poder1 = calcular_poder(heroi1, totem1)
    poder2 = calcular_poder(heroi2, totem2)
    nivel1 = determinar_nivel(poder1)
    nivel2 = determinar_nivel(poder2)
    if poder1 > poder2:
        vencedor = heroi1["nome"]
        perdedor = heroi2["nome"]
        poder_vencedor = poder1
    else:
        vencedor = heroi2["nome"]
        perdedor = heroi1["nome"]
        poder_vencedor = poder2
    print(f"{vencedor} abate {perdedor}. Power atual: {poder_vencedor} - Nível: {determinar_nivel(poder_vencedor)}")
    return vencedor

# Partida inicial
while True:
    entrada1 = input("Digite o nome do herói e o totem (ex: Puppie com Luvas do Titã): ")
    if entrada1.lower() == 'sair':
        break
    entrada2 = input("Digite o nome do outro herói e o totem (ex: Allepy com Cristal de Fúria): ")

    heroi1_nome, totem1 = entrada1.split(' com ')
    heroi2_nome, totem2 = entrada2.split(' com ')

    heroi1 = next(heroi for heroi in herois if heroi["nome"] == heroi1_nome)
    heroi2 = next(heroi for heroi in herois if heroi["nome"] == heroi2_nome)

    vencedor = batalha(heroi1, totem1, heroi2, totem2)
    herois = [heroi for heroi in herois if heroi["nome"] != heroi1_nome and heroi["nome"] != heroi2_nome] + [next(heroi for heroi in herois if heroi["nome"] == vencedor)]

# Nova rodada
for heroi in herois:
    print("Nova rodada de batalha")
    entrada1 = input(f"Escolha o herói {heroi['nome']} e o totem: ")
    entrada2 = input(f"Escolha o outro herói e o totem: ")
    
    heroi1_nome, totem1 = entrada1.split(' com ')
    heroi2_nome, totem2 = entrada2.split(' com ')

    heroi1 = next(heroi for heroi in herois if heroi["nome"] == heroi1_nome)
    heroi2 = next(heroi for heroi in herois if heroi["nome"] == heroi2_nome)
    
    vencedor = batalha(heroi1, totem1, heroi2, totem2)
    herois = [heroi for heroi in herois if heroi["nome"] != heroi1_nome and heroi["nome"] != heroi2_nome] + [next(heroi for heroi in herois if heroi["nome"] == vencedor)]

print(f"O vencedor final é: {herois[0]['nome']} com power final: {calcular_poder(herois[0], totem1)} - Nível: {determinar_nivel(calcular_poder(herois[0], totem1))}")
