from sense_hat import SenseHat
import time
from datetime import datetime
sense =SenseHat()

temp = sense.get_temperature()
pre = sense.get_pressure()
hum = sense.get_humidity()

id = 1
now = datetime.now()
time = time.mktime(now.timetuple())*1000 + now.microsecond/1000

print(
   '{{"id":{0:d},"time":{1:0.0f},"temp_in_C":{2:0.2f},"Pressure":{3:0.2f},"Humidity":{4:0.2f}}}'.format(id,time,temp,pre,hum))

