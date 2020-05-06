# How fast does a 12 foot car need to be going to fit in a 10 foot garage?
# https://www.wolframalpha.com/input/?i=length%20contraction

import math

#x = int(math.sqrt(9))
#print(x)

# known variables
l = (10 / 3.281) # length of garage converted to meters
s = (12 / 3.281) # length of car / stationary length converted to meters
c = (2.997925 * 10**8) # speed of light constant

# formula = l=sl*(sqrt(1-(v**2)/(2.998*(10**8))))

# formula changed to solve for v
# use wolframalpha hints to step through this solution
v = (math.sqrt((c**2)-((l**2)*(c**2)/(s**2))))

print(int(v),' meters per second or ',int(v)*2.23694,' miles per hour')













#v = symbols('v') # solve for velocity
# known variables
#l = (10 / 3.281) # length of garage converted to meters
#s = (12 / 3.281) # length of car / stationary length converted to meters
# c**2 = speed of light squared (2.998 * 10**8)

# formula = l=sl*(sqrt(1-(v**2)/(2.998*(10**8))))
#(10 = 12*(sqrt(1-(v**2)/(2.998*(10**8)))))

#formula = l = s * (sqrt(1 - (v**2) / (2.998 * (10**8))))
#sol = solve(formula)
#print(sol)