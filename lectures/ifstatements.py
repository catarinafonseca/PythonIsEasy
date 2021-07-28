# Basic structure of an if statement
""" 
if condition:
    Action
"""

click = False

Like = 0

click = True

if click == True:
    Like += 1
    click = False

# print(Like)

Temperature = 30
Thermo = 15

# print(Thermo)

if Temperature <= 15:
    Thermo += 5

# print(Thermo)

if Temperature >= 20:
    Thermo -= 3

# print(Thermo)


time = "Morning"
sleepy = False
pajamas = "Off"

if time == "Night" or sleepy == True:
    pajamas = "on"

elif time == "Morning":
    pajamas = "on"

else:
    pajamas = "off"

print(pajamas)
