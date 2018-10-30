import sys
from time import sleep
import Adafruit_DHT as dht
import requests
def DHT22_data():
	# Reading from DHT22 and storing the temperature and humidity
	humi, temp = dht.read_retry(dht.DHT22, 23) 
	return humi, temp
while True:
	try:
		humi, temp = DHT22_data()
		# If Reading is valid
		if isinstance(humi, float) and isinstance(temp, float):
			# Formatting to two decimal places
			humi = '%.2f' % humi 					   
			temp = '%.2f' % temp
			
      data_from_pi = {'humi': humi, 'temp': temp}
      response = requests.post('http://127.0.0.1:5000/pi', json=data_from_pi)
      if response.ok:
        print(response.json()) #--> {'humi': humi, 'temp': temp}
		  else:
			  print 'Error'
		# DHT22 requires 2 seconds to give a reading, so make sure to add delay of above 2 seconds.
		sleep(20)
	except:
		break
