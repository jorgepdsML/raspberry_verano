#---importar los modulos necesarios
import time
import RPi.GPIO as GPIO
#---------------------------------
var=input("INGRESAR TIEMPO DE ENCENDIDO")
var=int(var)

var2=input("INGRESAR TIEMPO DE APAGADO")
var2=int(var2)
#INDENDICACIÓN
if var>var2:
    print("var>var2")
    print("variable var es igual a: ",var)
else :
    print("var<=var2")
    print("variable var2 es igual a:",var2)

#desactivar los setwarnings
GPIO.setwarnings(False)
#configurar el setmode y el setup
GPIO.setmode(GPIO.BOARD)#Númeración BOARD
GPIO.setup(8,GPIO.OUT)#8 COMO SALIDA
while True:
    GPIO.output(8,GPIO.HIGH)
    time.sleep(var)
    GPIO.output(8,GPIO.LOW)
    time.sleep(var2)
    