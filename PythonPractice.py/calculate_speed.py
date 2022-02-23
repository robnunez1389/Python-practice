distance_kilo = 150
time_in_hours = 2
distance_mile = distance_kilo*1.6
distance_meters = distance_kilo*1000
time_in_seconds = time_in_hours*3600
speed_in_kph = distance_kilo / time_in_hours
speed_in_mph = distance_mile / time_in_hours
speed_in_mps = distance_meters / time_in_seconds

print("The speed in kilometers per hour is:", speed_in_kph)
print("The speed in miles per hour is:", speed_in_mph)
print("The speed in meters per second is:", speed_in_mps)
