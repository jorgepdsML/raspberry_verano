import time
try :
    import RPi.GPIO as GPIO
except RuntimeError:
    print("ERROR")

GPIO.setmode(GPIO.BOARD)
print ("GPIO.BOARD")
time.sleep(2)
print("INICIANDO")
GPIO.setwarnings(False)

GPIO.setup(11,GPIO.OUT)
GPIO.cleanup()

while True:
    print("ENCENDIDO")
    GPIO.output(11,GPIO.HIGH)
    time.sleep(2)
    print("APAGADO")
    
    GPIO.output(11,GPIO.LOW)
    time.sleep(2)
#ENCENDER DIODO LED PATILLA 11
GPIO.cleanup()
print("STOP")