#renombrar GPIO con RPi.GPIO
import RPi.GPIO as GPIO
import time 
#ENUMERACIóN BOARD
#set warning false
GPIO.setwarnings(False)
#OBJETO.METODO(OBJETO.ATRIBUTO)
GPIO.setmode(GPIO.BOARD)
#configurar el pin NUMERO 8 COMO SALIDA
GPIO.setup(8,GPIO.OUT)
print("CONFIGURANDO A LA RASPBERRY")
time.sleep(3)
print("ENCENDER DIODO LED")
GPIO.output(8,GPIO.HIGH)
time.sleep(6)
GPIO.output(8,GPIO.LOW)
