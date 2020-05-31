print("siemanko anko")

import sys

print("costam")
print(sys.avgr)

import bluetooth as BT
from bluetooth import *


print("Starting Discovery")
devices = discover_devices()
print("Discovery Finished")

for device in devices:
    if device == sys.argv :
        print("Device is discoverable")
        break
    else:
        exit()

services = find_service(sys.argv)

if len(services) > 0:
    for service in services:
        print(service)
else:
    print("services list is empty")

