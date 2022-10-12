import math

def distance(origin, destination):
    lat1, lon1 = origin
    lat2, lon2 = destination
    radius = 6371 # km

    dlat = math.radians(lat2-lat1)
    print("dlat",dlat)
    dlon = math.radians(lon2-lon1)
    print("dlon",dlon)
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = radius * c
    print("a",a)
    print("c",c)
    print("d",d)
    return d

# 38.35252313201552 (km为单位)
print (distance((51.187222,6.79725), (51.2179166, 6.76175)))