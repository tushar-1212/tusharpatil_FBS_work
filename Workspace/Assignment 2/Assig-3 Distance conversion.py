#Convert distance given in feet and inches into meter and centimeter.
distance_feet = int(input("Enter the distance in feet: "))
distance_inches = int(input("Enter the distance in inches: "))
total_inches = (distance_feet * 12) + distance_inches   
total_meters = total_inches * 0.0254
total_centimeters = total_inches * 2.54
print("Distance in meters:", total_meters)
print("Distance in centimeters:", total_centimeters)


