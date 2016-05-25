import games
import heuristica

# game = games.TicTacToe(h=3,v=3,k=3)
game = games.ConnectFour()

state = game.initial

# Valores iniciales
player = 'X'
# player1 = 'X'
# player2 = 'O'
dificultad1 = 'heuristica'
dificultad2 = 'none'
jugadas = 0
prof = 1

while dificultad1 == 'heuristica':
    print "Seleccion de dificultad: "
    entrada = raw_input("1: Facil 2: Medio 3: Dificil ")
    if entrada == '1':
        dificultad1 = "h_1", heuristica.h_1
    elif entrada == '2':
        dificultad1 = "h_2", heuristica.h_2
    elif entrada == '3':
        dificultad1 = "h_3", heuristica.h_3
    else:
        print "Entrada no valida"

while dificultad2 == 'none':
    print "Selecciona jugador O:"
    entrada = raw_input("Maquina = m, Jugador = j ")
    if entrada == 'm' or entrada == 'M':
        dificultad2 = 'heuristica'
    elif entrada == 'j' or entrada == 'J':
        dificultad2 = 'human'
    else:
        print "Entrada no valida"

while dificultad2 == 'heuristica':
    print "Seleccion de dificultad: "
    entrada = raw_input("1: Facil 2: Medio 3: Dificil ")
    if entrada == '1':
        dificultad2 = "h_1", heuristica.h_1
    elif entrada == '2':
        dificultad2 = "h_2", heuristica.h_2
    elif entrada == '3':
        dificultad2 = "h_3", heuristica.h_3
    else:
        print "Entrada no valida"

while True:
    # Jugador no humano 'O'
    if dificultad1 != 'human':
        if game.terminal_test(state):
            game.display(state)
            print "Final de la partida"
            break
        print "Jugador a mover:", game.to_move(state)
        game.display(state)
        print "Thinking..."
        move = games.alphabeta_search(state, game, d=prof, cutoff_test=None, eval_fn=dificultad1[1])
        state = game.make_move(move, state)
        player = 'X'
        jugadas += 1
        # Cada 20 jugadas aumentamos la profundidad de busqueda
        #if jugadas % 20 == 0:
            #prof += 2
        print "Profundidad:", prof
        print "Dificultad:", dificultad1[0], "vs", dificultad2[0]
    # Jugador humano 'O'
    else:
        if game.terminal_test(state):
            game.display(state)
            print "Final de la partida"
            break
        print "Jugador a mover:", game.to_move(state)
        game.display(state)
        col_str = raw_input("Movimiento: ")
        coor = int(str(col_str).strip())
        x = coor
        y = -1
        legal_moves = game.legal_moves(state)
        for lm in legal_moves:
            if lm[0] == x:
                y = lm[1]
        state = game.make_move((x, y), state)
        player = 'X'
        jugadas += 1
        # Cada 20 jugadas aumentamos la profundidad de busqueda
        #if jugadas % 20 == 0:
        #    prof += 2
        print "Profundidad:", prof
        print "Dificultad:", dificultad1[0], "vs", dificultad2[0]
    # Jugador no humano 'X'
    if dificultad2 != 'human':
        if game.terminal_test(state):
            game.display(state)
            print "Final de la partida"
            break
        print "Jugador a mover:", game.to_move(state)
        game.display(state)
        print "Thinking..."
        move = games.alphabeta_search(state, game, d=prof, cutoff_test=None, eval_fn=dificultad2[1])
        state = game.make_move(move, state)
        player = 'O'
        jugadas += 1
        # Cada 20 jugadas aumentamos la profundidad de busqueda
        #if jugadas % 20 == 0:
            #prof += 2
        print "Profundidad:", prof
        print "Dificultad:", dificultad1[0], "vs", dificultad2[0]
    # Jugador humano 'X'
    else:
        if game.terminal_test(state):
            game.display(state)
            print "Final de la partida"
            break
        print "Jugador a mover:", game.to_move(state)
        game.display(state)
        col_str = raw_input("Movimiento: ")
        coor = int(str(col_str).strip())
        x = coor
        y = -1
        legal_moves = game.legal_moves(state)
        for lm in legal_moves:
            if lm[0] == x:
                y = lm[1]
        state = game.make_move((x, y), state)
        player = 'O'
        jugadas += 1
    # Cada 20 jugadas aumentamos la profundidad de busqueda
    #if jugadas % 20 == 0:
        #prof += 2
    print "Profundidad:", prof
    print "Dificultad:", dificultad1[0], "vs", dificultad2[0]
    print "-------------------"
