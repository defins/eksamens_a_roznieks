from math import pi

def circlearea (r):
    return pi*r**2
print ("Ievadi rinka radiusu:")
r = int(input())
print(circlearea(r))