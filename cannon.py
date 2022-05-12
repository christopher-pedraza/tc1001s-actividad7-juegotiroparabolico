"""
Actividad 7: Juego del Tiro Parabólico

Equipo 9:
Christopher Gabriel Pedraza Pohlenz A01177767
Kevin Susej Garza Aragón A00833985
Eugenia Ruiz Velasco Olvera A01177887
"""

# Se importan las librerías de random, turtle y freegames
from random import randrange
from turtle import *
from freegames import vector

# Inicializar los vectores de posición y velocidad
ball = vector(-200, -200)
speed = vector(0, 0)
targets = []


# Función que se llama al dar un click
# Recibe: Coordenadas del click
def tap(x, y):
    # Comprueba que la pelota esté dentro de los límites de la pantalla
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 200) / 25
        speed.y = (y + 200) / 25


# Función que comprueba si el elemento se encuentra dentro de la pantalla
def inside(xy):
    return -200 < xy.x < 200 and -200 < xy.y < 200


# Función que dibuja a la pelota y a los objetivos
def draw():
    # Elimina los dibujos en la pantalla
    clear()

    # Ciclo que genera todos los objetivos registrados 
    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')

    # Si la pelota está dentro de la pantalla, la crea
    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')

    update()


# Función que mueve a la pelota y a los objetivos
def move():
    # Genera el objetivo en una posición aleatoria de y
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    # Mover todos los objetivos hacia la izquierda
    for target in targets:
        target.x -= 0.5

    # Reduce velocidad vertical para que haya caída
    if inside(ball):
        speed.y -= 0.35
        ball.move(speed)

    # Copiar la lista de objetivos
    dupe = targets.copy()
    # Limpiar la lista original de objetivos
    targets.clear()

    # Ciclo que recorre todos los objetivos
    for target in dupe:
        # Si la diferencia de posición es mayor a la tolerancia, la vuelve a guardar en la lista
        if abs(target - ball) > 13:
            targets.append(target)
    
    # Vuelve a dibujar el proyectil y los objetivos
    draw()

    # Recorrer todas las coordenadas de los objetivos
    for target in targets:
        # Checa si los objetivos están fuera de la pantalla
        if not inside(target):
            # Elimina al objetivo de la lista
            targets.pop(0)

    # Llama a la función move, cada 5 milisegundos
    ontimer(move, 5)


# Establecer el ancho, largo, y posición inicial en x y y
setup(420, 420, 370, 0)
# Esconder el cursor, la tortuga
hideturtle()
# Deja de dibujar
up()
# Elimina la animación de la tortuga
tracer(False)
# Al haber un click en la pantalla, se llama a esta función, pasando las coordenadas del click
onscreenclick(tap)
# Llama a la función move
move()
# Comienza el ciclo de eventos
done()
