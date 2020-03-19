#Hunter Borwick
#3/18/2020
#Orbital Elements from Position and Velocity Vectors

import math

#Cross Product for two vectors a x b
def cross(a, b):
    c = [a[1]*b[2] - a[2]*b[1],
         a[2]*b[0] - a[0]*b[2],
         a[0]*b[1] - a[1]*b[0]]

    return c

#Dot Product for two vectors a . b 
def dot(a, b):
    return sum(x*y for x,y in zip(a,b))

#Magnitude of given vector a
def mag(a):
    magnitude = math.sqrt(sum(v**2 for v in a))
    
    return magnitude

#Multiplying a vector (b) by coefficient (a)
def coeff(a, b):
    newVector = [0,0,0]
    newVector[0] = a * b[0]
    newVector[1] = a * b[1]
    newVector[2] = a * b[2]

    return newVector 

#Subtracting two vectors (a - b)
def subtract_vectors(a, b):
    newVector = [0,0,0]
    newVector[0] = a[0] - b[0]
    newVector[1] = a[1] - b[1]
    newVector[2] = a[2] - b[2]

    return newVector

if __name__ == "__main__":
    #Universal Gravitation Constant For Earth
    mu = 3.986E5

    #Given state vectors 
    r = [6500, -7500, -2500]
    v = [4, 3, -3]

    #Magnitudes of state vectors
    r_mag = mag(r)
    v_mag = mag(v)

    #Radial Component of velocity
    v_r = (dot(r,v)) / r_mag
    
    #Specific Angular Momentum Vector & Magnitude
    h = cross(r, v)
    h_mag = mag(h)

    #Inclination (degrees)
    i = math.acos(h[2] / h_mag) * (180 / math.pi)

    #Node Line and Node Magnitude
    k_hat = [0, 0, 1]
    node = cross(k_hat, h)
    node_mag = mag(node)

    #Right Ascension of the Ascending Node
    omega = math.acos(node[0] / node_mag) * (180 / math.pi)
    if node[1] < 0:
        omega = 360 - omega

    #Eccentricity Vector and Magnitude
    #Equation:  e = (1/mu)(V x h - mu * (r / r_mag))
    x = cross(v,h)
    c = mu * (1/r_mag)
    newr = coeff(c, r)
    e = subtract_vectors(x, newr)
    inv = 1 / mu

    e = coeff(inv, e)
    e_mag = mag(e)
    
    #Argument of Perigee
    node_unit = coeff(1/node_mag, node)
    eccentricity_unit = coeff(1/e_mag, e)
    w = math.acos(dot(node_unit, eccentricity_unit)) * (180 / math.pi)
    if e[2] < 0:
        w = 360 - w
    
    #True Anomaly
    eccentricity_unit = coeff(1/e_mag, e)
    position_unit = coeff(1/r_mag, r)
    theta = math.acos(dot(eccentricity_unit, position_unit)) * (180 / math.pi)
    if v_r < 0:
        theta = 360 - theta

    #Printing of all orbit element values
    print("############################################################")
    print("Eccentricity:", e_mag)
    print("Specific Angular Momentum:", h_mag)
    print("Inclination:", i)
    print("Right Ascension of the Ascending Node:", omega)
    print("Argument of Perigee:", w)
    print("True Anomaly:", theta)
    print("############################################################")




    