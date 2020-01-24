try :
    import RPi.GPIO as GPIO
except RuntimeError:
    print("SUDO requiered")
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3,GPIO.IN)
cont=0
print("LECTURA DE PULSADOR RASPBERRY")
time.sleep(2)
while True:
    if GPIO.input(3)==GPIO.LOW:
        time.sleep(0.30)
        while GPIO.input(3)==GPIO.LOW:
            time.sleep(0.0001)
        cont=cont+1
        print("PULSO DETECTADO N°"+str(cont))

GPIO.cleanup()
        
