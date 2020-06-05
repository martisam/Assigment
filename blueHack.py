#Classa libraries for the bluetooth application

#first class library
import time

#3rd party module
from bluetooth.ble import BeaconService

#Creating an Instance object
service = BeaconService() 

#Advertising the  UUID and different ports for spoofing
service.start_advertising("11111111-2222-3333-4444-555555555555", 1, 1, 1, 200)

time.sleep_stop_advertise(15)
service.sleep_stop_advertise()

print("Done.")