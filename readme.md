En el fichero heuristica.py se encuentran implementadas las diferentes heurísticas, una para cada dificultad.
Tambien se encuentra la implementación de memoize usada por cada heurística.
El fichero run.py se implemento de modo que pregunta que jugador empezará (X = maquina, O = humano),
y la dificultad de la máquina.
En games.py se añadió una clase para darle color al tablero.

heuristica.py
Para el nivel fácil tenemos h0, la cual siempre devuelve 0.
Para el medio tenemos h1, que retorna un valor aletaorio entre 100 y -100
Para el difícil tenemos h2, usa el metodo compute_utility (que calcula el valor
de la heuristica), calcula el valor con el método k_in_row, cuenta los potenciales 4 en raya,
es decir, localiza el número de piezas alineadas del jugador (mayor número de piezas
alineadas, mayor valor) y le resta el número de potenciales 4 en raya del contrario.
Además, dependiendo de la posición en la que se localicen las fichas se le asigna un peso,
dando mayor valor a las piezas mas abajo y centradas que al resto.