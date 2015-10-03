#!/usr/bin/python
import requests
from sys import argv
def get_distance(origin,destination):
    gmap='http://maps.googleapis.com/maps/api/distancematrix/json'
    payload={"origins":origin,"destinations":destination,"sensor":'false' }
    try:
        a=requests.get(gmap,params=payload)
        data = a.json()
        print data
        origin = str(data['origin_addresses'][0])
        destination= str(data['destination_addresses'][0])
        distance = data['rows'][0]['elements'][0]['distance']['text']
        return distance,origin,destination
    except Exception,e:
        print "The %s or %destination does not exists :(" %(origin,destination)
        exit()

if __name__=="__main__":
    if len(argv)<3:
        print "sorry Check the format"
    else:
        origin=argv[1]
        destination=argv[2]
        print origin,destination
        distance,origin,destination=get_distance(origin,destination)
        print "%s ---> %s    :   %s" %(origin,destination,distance)
