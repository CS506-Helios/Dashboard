#!/usr/bin/env python

@Testing

import requests
from decimal import *
import time

# IP address of inverter
host = "144.92.98.92"
# number of seconds between samples

minute = 1

sample_seconds = 60 * minute
    
if sample_seconds != 300:
    print ('Too short') 

def main():
    energy_generated()


# power generated in certain time piriod
def energy_generated():
    url = "http://" + host + "/solar_api/v1/GetInverterRealtimeData.cgi?Scope=System"
    r = requests.get(url, timeout=10)
    json_data = r.json()
    dic = json_data["Body"]["Data"]["PAC"]["Values"]
    # sum up values in two units of inverters and transfer the unit to kWh
    result = sum(dic.values()) / float(60000/minute)
    return result


if __name__ == "__main__":
    main()
