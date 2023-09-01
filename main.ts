let distancia = 0
input.onButtonPressed(Button.A, function () {
    Tinybit.car_sport(100, 100)
    distancia = Tinybit.Ultrasonic_CarV2()
    if (distancia < 10) {
        basic.pause(1000)
        Tinybit.Music_Car(Tinybit.enMusic.dadadum)
    }
})
