
def sumar_puntaje(estadisticas):
    total = estadisticas['kills'] * 3 + estadisticas['assists']
    if estadisticas['deaths']:
        total = total - 1
    return total

def calcular_mvp(mvp):
    return max(mvp[0].items(), key=lambda item: item[1]['puntos'])[0]

def actualizar_datos(mvp, jugador, estadisticas):
    mvp[0][jugador]['kills'] += estadisticas['kills']
    mvp[0][jugador]['assists'] += estadisticas['assists']
    if estadisticas['deaths']:
        mvp[0][jugador]['deaths'] += 1