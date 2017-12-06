#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 19:27:47 2017

@author: ying
"""



import requests
import time

# IP address of inverter
host = "144.92.98.92"
# number of seconds between samples
sample_seconds = 60 * 5


def main():
    print("started")
    while True:
        try:
            watts = watts_generated()
            now = time.strftime("%H:%M:%S")
            line = "%s\t%s\n" % (now, watts)
            # print(line)
            write_to_logfile(line)
        except requests.exceptions.ConnectTimeout:
            print("Connect timeout at %s" % time.strftime("%H:%M:%S"))
        if sample_seconds > 0:
            time.sleep(sample_seconds)
        else:
            return


def write_to_logfile(line):
    today = time.strftime("%Y_%m_%d")
    file_name = today + ".csv"
    out_file = open(file_name, "a")
    out_file.write(line)
    out_file.close()


def watts_generated():
    url = "http://" + host + "/solar_api/v1/GetInverterRealtimeData.cgi?Scope=System"
    r = requests.get(url, timeout=10)
    json_data = r.json()
    result = json_data["Body"]["Data"]["PAC"]["Values"]
    return result


if __name__ == "__main__":
    main()
