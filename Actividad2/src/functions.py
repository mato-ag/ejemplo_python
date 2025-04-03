
def sumar_puntaje(estadisticas):
    total = estadisticas['kills'] * 3 + estadisticas['assists']
    if estadisticas['deaths']:
        total = total - 1
    return total

def calcular_mvp(mvp):
    jugador_max = None
    max_puntaje = -1
    for jugador, datos in mvp[0].items():
        if datos['puntos'] > max_puntaje:
            max_puntaje = datos['puntos']
            jugador_max = jugador
    return jugador_max

def actualizar_datos(mvp, jugador, estadisticas):
    mvp[0][jugador]['kills'] = mvp[0][jugador]['kills'] + estadisticas['kills']
    mvp[0][jugador]['assists'] = mvp[0][jugador]['assists'] + estadisticas['assists']
    if estadisticas['deaths']:
        mvp[0][jugador]['deaths'] += 1
