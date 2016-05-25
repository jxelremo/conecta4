from utils import *

# state -> ['__cmp__', '__doc__', '__init__', '__module__', '__repr__', 'board', 'moves', 'to_move', 'utility']
# max (1..7, 1..6) (columna, fila)


def memoize(f):
    memo = {}

    def helper(state):
        key = tuple(state.board.items())
        if key not in memo:
            memo[key] = f(state)
        return memo[key]

    return helper


def legal_moves(state):
    "Legal moves are any square not yet taken."
    return [(x, y) for (x, y) in state.moves
            if y == 1 or (x, y - 1) in state.board]


def k_in_row(state, player, (delta_x, delta_y)):
    board = state.board
    # Con los pesos favorecemos jugar abajo y en el centro del tablero
    weights_c = [4, 8, 16, 32, 16, 8, 4]
    weights_f = [32, 16, 8, 4, 2, 1]
    htotal = 0
    h1 = 0
    h2 = 0
    for move in legal_moves(state):
        pos = (move[0] + delta_x, move[1] + delta_y)
        good = 0
        # Mientras sea una posicion legal calculamos su valor para un maximo de 3 desplazamientos
        while (pos in state.moves or board.get(pos) == player) and good < 3:
            # Si la posicion nos pertenece
            if board.get(pos) == player:
                # Si la ficha anterior es nuestra
                if board.get(pos[0] - delta_x, pos[1] - delta_y) == player:
                    h1 += weights_c[pos[0] - 1] * weights_f[pos[1] - 1] * 2
                # Si la ficha anterior es un hueco
                else:
                    h1 += weights_c[pos[0] - 1] * weights_f[pos[1] - 1]
            # Si la posicion es un hueco
            elif pos in state.moves:
                # Si la ficha anterior es nuestra
                if board.get(pos[0] - delta_x, pos[1] - delta_y) == player:
                    h1 += weights_c[pos[0] - 1] * weights_f[pos[1] - 1]
                # Si la ficha anterior es un hueco
                else:
                    h1 += weights_c[pos[0] - 1] * weights_f[pos[1] - 1] / 2
            # Actualizamos las posiciones
            pos = (pos[0] + delta_x, pos[1] + delta_y)
            good += 1
        # Si es un potencial 4 en raya sumamos su valor heuristico
        if good == 3:
            htotal += h1
        # Reiniciamos a la posicion original
        pos = (move[0] + delta_x, move[1] + delta_y)
        good = 0
        h1 = 0
        # Mientras sea una posicion legal calculamos su valor para un maximo de 3 desplazamientos
        while (pos in state.moves or board.get(pos) == player) and good < 3:
            # Si la posicion nos pertenece
            if board.get(pos) == player:
                # Si la ficha anterior es nuestra
                if board.get(pos[0] + delta_x, pos[1] + delta_y) == player:
                    h2 += weights_c[pos[0] - 1] * weights_f[pos[1] - 1] * 2
                # Si la ficha anterior es un hueco
                else:
                    h2 += weights_c[pos[0] - 1] * weights_f[pos[1] - 1]
            # Si la posicion es un hueco
            elif pos in state.moves:
                # Si la ficha anterior es nuestra
                if board.get(pos[0] + delta_x, pos[1] + delta_y) == player:
                    h2 += (weights_c[pos[0] - 1] * weights_f[pos[1] - 1])
                # Si la ficha anterior es un hueco
                else:
                    h2 += (weights_c[pos[0] - 1] * weights_f[pos[1] - 1]) / 2
            # Actualizamos las posiciones
            pos = (pos[0] - delta_x, pos[1] - delta_y)
            good += 1
        # Si es un potencial 4 en raya sumamos su valor heuristico
        if good == 3:
            htotal += h2
        h2 = 0
    return htotal


# Calcula segun el jugador usando k_in_row
def compute_utility(state, player):
        pk = 0
        pk += k_in_row(state, player, (0, 1))
        pk += k_in_row(state, player, (1, 0))
        pk += k_in_row(state, player, (1, -1))
        pk += k_in_row(state, player, (-1, 1))
        if player == 'X':
            contrincante = 'O'
        else:
            contrincante = 'X'
        pk -= k_in_row(state, contrincante, (0, 1))
        pk -= k_in_row(state, contrincante, (1, 0))
        pk -= k_in_row(state, contrincante, (1, -1))
        pk -= k_in_row(state, contrincante, (-1, 1))

        return pk


@memoize
# FACIL: Retorna siempre 0
def h_0(state):
    if state.utility != 0:
        return state.utility * infinity
    else:
        return 0


@memoize
# MEDIO: Retorna valor aleatorio entre -100 y 100
def h_1(state):
    if state.utility != 0:
        return state.utility * infinity
    else:
        return random.randint(-100, 100)


@memoize
# DIFICIL: Cada posicion tiene un peso y buscamos potenciales 4 en raya
def h_2(state):
    if state.utility != 0:
        return state.utility * infinity
    else:
        # Calcula el valor heuristico para el jugador
        h = compute_utility(state, 'X')
        return h