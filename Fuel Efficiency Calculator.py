# PCAP test
def liters_100km_to_miles_gallon(liters):
    # l/km
    liters /= 100
    # km/l
    liters **= -1
    # km/g
    liters *= 3.785411784
    # mpg
    liters /= 1.609344
    return liters


def miles_gallon_to_liters_100km(miles):
    # g/m
    miles **= -1
    # g/100miles
    miles *= 100
    # l/100miles
    miles /= 1.609344
    # l/100km
    miles *= 3.785411784
    return miles


print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))
