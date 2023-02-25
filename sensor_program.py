import socket
import serial
import time
from threading import Timer

import RPi.GPIO as GPIO
import dht11
import time

#arduino data
ser = serial.Serial('/dev/ttyACM0')
ser.flushInput()


# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
#GPIO.cleanup()
GPIO.setup(21, GPIO.IN) # Set pin 8 to be an output pin and set initial value to low (off)
# read data using Pin GPIO21 
instance = dht11.DHT11(pin=21)
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("",5000))
s.listen(1000)
print('server is now running.')

def controller():
    while True:
        ser_bytes = ser.readline()
        decoded_bytes = str(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
        ard=decoded_bytes
        result = instance.read()
        if result.is_valid():
            temp=result.temperature
            humidity=result.humidity
            l=ard.split()
            x=int(l[len(l)-1])
            print(x)
            t=0
            n=0
            if(temp>=18.0 and temp<=33.0 and humidity>=50 and humidity<=88  and x<800):
                  m1="The temprature "+str(temp)+" C the humidity "+str(humidity)+"% and the moisture "+str(x)+" is in the range for Bengal Tiger to survive"
                  print(m1)
                  clientsocket.send(bytes(m1, "utf-8"))
            elif((temp<=18.0 or temp>=33.0) or (humidity<=77 or humidity>=88) or(x>=800)):
                m2="Result:The place is not suitable for the Bengal Tiger to live"
                print(m2)
                clientsocket.send(bytes(m2, "utf-8"))
            Timer(1000, controller).start()
        
       
        #print("Temp: %d C" % result.temperature +' '+"Humid: %d %%" % result.humidity)
    #time.sleep(10)
        
        
while True:
    clientsocket, address=s.accept()
    print(f"connection from {address} has been established")
    controller()
    
    
    
    

