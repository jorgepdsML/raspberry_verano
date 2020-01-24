#ARCHIVO PARA LA DEFINICION DE FUNCIONES
import RPi.GPIO as GPIO
import time
#---funciones------------------
def encender(pin):
    GPIO.output(pin,GPIO.HIGH)
def apagar(pin):
    GPIO.output(pin,GPIO.LOW)
#--------CONFIGURACIÓN DEL GPIO---------
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8,GPIO.OUT)
GPIO.setup(15,GPIO.IN)
while True:
    #LEER EL ESTADO DEL GPIO15
    if GPIO.input(15)==0:
        #SE HA PRESIONADO EL PIN 15
        time.sleep(0.05)
        while GPIO.input(15)==0:
            time.sleep(0.0001)
        print("SE HA PRESIONADO EL PULSADOR")
        
        
    """
    encender(8)
    time.sleep(3)
    apagar(8)
    time.sleep(4)
    """
    


    