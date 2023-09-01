distancia = 0

def on_button_pressed_a():
    global distancia
    Tinybit.car_sport(100, 100)
    distancia = Tinybit.Ultrasonic_CarV2()
    if distancia < 10:
        basic.pause(1000)
        Tinybit.Music_Car(Tinybit.enMusic.DADADUM)
input.on_button_pressed(Button.A, on_button_pressed_a)
