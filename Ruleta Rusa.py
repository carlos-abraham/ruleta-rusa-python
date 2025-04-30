import random
import time

ruleta = [0, 0, 0, 0, 0, 1]
turnos = 0


print("El jugador 1 y 2 jugaran con una revolver de 6 compartimientos, el primero que dispare al otro gana, el jugador 1 inicia.")
time.sleep(4)
while True:
    turnos += 1
    disparo = random.choice(ruleta)
    ruleta.remove(disparo)
    print("El turno actual es:", (turnos))
    time.sleep(1.5)
    if disparo == 1:
        if turnos in (1, 3, 5):
            print("*Sonido de disparo*")
            time.sleep(1.2)
            print("Jugador 1 ganador.")
            break
        else:
            print("*Sonido de disparo*")
            time.sleep(1)
            print("Jugador 2 ganador.")
            break
    
    else:
        print("*Click...*")
        time.sleep(1)
        print("La pistola no se a disparado")
        time.sleep(2)

