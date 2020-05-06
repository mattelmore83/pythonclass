# Take user input in feet and output that distance in miles and meters

d = int(input('Distance in feet? '))

miles = (d / 5280)
meters = (d / 3.281)

print('Distance in miles: ',miles,'\nDistance in meters: ',meters,'')