import RPi.GPIO as GPIO
import time
lista1=[3,5,11,13]
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
#CONFIGURAR UN CONJUNTO DE CANALES COMO SALIDA
GPIO.setup(lista1,GPIO.OUT)
#ENERGIZAR UN CONJUNTO DE CANALES
GPIO.output(lista1,GPIO.HIGH)
time.sleep(2)
GPIO.output(lista1,GPIO.LOW)
