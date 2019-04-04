import math

# Figura 9.1:
# Abstração: lado * base / 2
# 5 * 6 / 2 = 30
# def areaIsosceles(): return 5 * 6

# Generalização:
def areaIsosceles(lado, base):
    area = lado * base / 2
    return area

# Instanciação
print("Instanciação de areaIsosceles com lado 5 e base 6: {}".format(areaIsosceles(5, 6)))
print("Instanciação de areaIsosceles com lado 2 e base 7: {}".format(areaIsosceles(2, 7)))

# Figura 9.2:
# Base = raio * 2
# Abstração: (lado * base / 2) + (pi * raio**2 / 2)
# (5 * 6 / 2) + (pi * 3**2 / 2) = 44.13716694115407
# def areaSorvetin(): return (5 * 6) + (pi * 3**2 / 2)

# Generalização:
def areaSemiCirculo(raio):
    area = math.pi * raio ** 2 / 2

    return area

def areaSorvetin(lado, raio):
    base = raio * 2
    areaBoleta = areaSemiCirculo(raio)
    areaTriangulo = areaIsosceles(lado, base)

    area = areaTriangulo + areaBoleta

    return area

# Instanciação
print("Instanciação de areaSorvetin com lado 5 e raio 5: {:g}".format(areaSorvetin(5, 6)))
print("Instanciação de areaSorvetin com lado 2 e raio 7: {:g}".format(areaSorvetin(2, 7)))

# Figura 9.3:
# Abstração: (ladoTriangulo * base / 2) + (base * ladoRetangulo)
# (5 * 6 / 2) + (5 * 6)
# def areaCasinha(): return (5 * 6 / 2) + (5 * 6)

# Generalização:
def areaRetangulo(base, lado):
    area = base * lado

    return area

def areaCasinha(base, ladoRetangulo, ladoTriangulo):
    areaRet = areaRetangulo(base, ladoRetangulo)
    areaTriangulo = areaIsosceles(base, ladoTriangulo)

    area = areaRet + areaTriangulo

    return area

# Instanciação
print("Instanciação de areaCasinha com lado 5 e raio 5: {:g}".format(areaCasinha(6, 5, 5)))
print("Instanciação de areaCasinha com lado 2 e raio 7: {:g}".format(areaCasinha(3, 2, 3)))

# Figura 9.4:
# Abstração: (baseRet * ladoRetangulo) - (baseTriangulo * ladoTriangulo / 2)
# 8 * 5 - (6 * 5 / 2)
# def areaNegocio(): return (8 * 5) - (6 * 5 / 2)

# Generalização:
def areaRetangulo(base, lado):
    area = base * lado

    return area

def areaNegocio(baseRet, ladoRetangulo, baseTriangulo, ladoTriangulo):
    areaRet = areaRetangulo(baseRet, ladoRetangulo)
    areaTriangulo = areaIsosceles(baseTriangulo, ladoTriangulo)

    area = areaRet - areaTriangulo

    return area

# Instanciação
print("Instanciação de areaNegocio com lado 5 e raio 5: {:g}".format(areaNegocio(8, 5, 6, 5)))
print("Instanciação de areaNegocio com lado 2 e raio 7: {:g}".format(areaNegocio(3, 2, 3, 3)))
