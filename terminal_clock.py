# PARA O PROGRAMA RODAR EM SEU TERMINAL É SO NECESSARIO ESCREVER 'python3 terminal_clock.py' E SEU PROGRAMA FUNCIONARÁ PERFEITAMENTE 

import time
import os
from datetime import datetime

# Números 7x7 com blocos █
# ESTE CÓDIGO É DE SnowDev01
NUMEROS_BASE = {
    "0": [
        "███████",
        "█     █",
        "█     █",
        "█     █",
        "█     █",
        "█     █",
        "███████"
    ],
    "1": [
        "   █   ",
        "   █   ",
        "   █   ",
        "   █   ",
        "   █   ",
        "   █   ",
        "   █   "
    ],
    "2": [
        "███████",
        "      █",
        "      █",
        "███████",
        "█      ",
        "█      ",
        "███████"
    ],
    "3": [
        "███████",
        "      █",
        "      █",
        "███████",
        "      █",
        "      █",
        "███████"
    ],
    "4": [
        "█     █",
        "█     █",
        "█     █",
        "███████",
        "      █",
        "      █",
        "      █"
    ],
    "5": [
        "███████",
        "█      ",
        "█      ",
        "███████",
        "      █",
        "      █",
        "███████"
    ],
    "6": [
        "███████",
        "█      ",
        "█      ",
        "███████",
        "█     █",
        "█     █",
        "███████"
    ],
    "7": [
        "███████",
        "      █",
        "      █",
        "      █",
        "      █",
        "      █",
        "      █"
    ],
    "8": [
        "███████",
        "█     █",
        "█     █",
        "███████",
        "█     █",
        "█     █",
        "███████"
    ],
    "9": [
        "███████",
        "█     █",
        "█     █",
        "███████",
        "      █",
        "      █",
        "███████"
    ],
    ":": [
        "       ",
        "   █   ",
        "       ",
        "       ",
        "   █   ",
        "       ",
        "       "
    ]
}

# ESTE CÓDIGO É DE SnowDev01
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def scale_block(block, scale_w, scale_h):
    """Escala horizontal e verticalmente um bloco"""
    scaled = []
    for line in block:
        new_line = "".join(char * scale_w for char in line)
        for _ in range(scale_h):
            scaled.append(new_line)
    return scaled

def mostrar_hora_centralizada(hora_str):
    """Mostra a hora escalada e centralizada horizontal e verticalmente"""
    term_size = os.get_terminal_size()
    term_width, term_height = term_size.columns, term_size.lines

    # Escala baseada na largura
    total_chars = len(hora_str) * 7 + (len(hora_str)-1)*2
    scale_w = max(1, term_width // total_chars)
    scale_h = scale_w  # altura proporcional

    # Cria linhas escaladas
    linhas = [""] * (7 * scale_h)
    for char in hora_str:
        bloco = scale_block(NUMEROS_BASE[char], scale_w, scale_h)
        for i in range(len(linhas)):
            linhas[i] += bloco[i] + "  "  # espaço entre números

    # Centraliza verticalmente
    empty_lines = max(0, (term_height - len(linhas)) // 2)
    print("\n" * empty_lines, end="")

    # Imprime cada linha centralizada horizontalmente
    for linha in linhas:
        print(linha.center(term_width))

# ESTE CÓDIGO É DE SnowDev01
try:
    while True:
        clear()
        agora = datetime.now().strftime("%H:%M:%S")
        mostrar_hora_centralizada(agora)
        time.sleep(1)
except KeyboardInterrupt:
    print("⏰ Relógio encerrado!")

# ESTE CÓDIGO É DE SnowDev01
