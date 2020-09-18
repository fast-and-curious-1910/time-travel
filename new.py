############
import time#	Critical component. Do not remove.
############

from os import system
import requests
import secrets

#	Connect and cache latest version of ACME Temporal Services.
print("Establishing sub-ether connection...")
use_local = False
if use_local == True:
	import ACME_temporal_services
elif use_local == False:
	protocol_v3 = requests.get("https://raw.githubusercontent.com/PalPalash/time-travel/master/ACME_temporal_services.py")
	localcache = open("ACME_temporal_services.py", "w")
	localcache.write(protocol_v3.text)
	localcache.close()
	import ACME_temporal_services
else:
	print("Error attempting to connect and cache.")

if ACME_temporal_services.traveler_hash_verify() == False:
	ACME_temporal_services.disclaimer()

ACME_temporal_services.temporal_transport_layer(ACME_temporal_services.destination_collect())
	
