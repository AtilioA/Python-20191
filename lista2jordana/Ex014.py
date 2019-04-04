from Ex004 import distEuclid
import math

# def areaR1(Px, Py, Qx, Qy):

#     return

# def areaR2(Px, Py, Qx, Qy):

#     return

# def areaR3(Px, Py, Qx, Qy):

#     return

def alturaTrianguloIsosceles(lado, base):
    altura = math.sqrt(lado**2 - base**2 / 4)

    return altura

print(alturaTrianguloIsosceles(5, 8))

def areaFigura(Px, Py, Qx, Qy):
    lado = distEuclid(x1, y1, x2, y2)
    base = (distEuclid(x1, y1, x2, y1)) * 2
    hTriangulo = alturaTrianguloIsosceles(lado, base)

    



    R2 = areaR2(Px, Py, Qx, Qy)
    R3 = areaR3(Px, Py, Qx, Qy)
