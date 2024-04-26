import Adafruit_DHT

#Definido o Sensor

sensor = Adafruit_DHT.DHT22

#Definindo o pino GPIO

pin = 4

while True:

    umidade, temperatura = Adafruit_DHT.read_reatry(sensor, pin) 

    if umidade is not None and temperatura is not None:
        print("Tempetura: {0:0.1f} °C".format(temperatura))
        print("Umidade: {0:0.1f} %".format(umidade))

    else:
        print("Falha ao ler o sensor DHT!")
    

time.sleep(1)