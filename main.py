#Librerias
import math

""" Taller 2.3 Distancia mas corta #
    Yenifer Barco Castrillón
    Mayo 15-2021 """

# Definición de Funciones (Dividir)
#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# =====================================================================
def calcular_distancia_c1_a1(xc1,yc1,xa1,ya1):
    """
    Parameters
    --------------
    xc1,yc1,xa1,ya1:float
      valores de coordenadas de celular 1 y antena 1
    Return
    --------------
    d1:float
      valor de la distancia entre celular 1 a la antena 1
    """
    d1= math.sqrt((xc1-xa1)**2+(yc1-ya1)**2)

    return d1
#-------------------------------------------
def calcular_distancia_a1_ch(xa1,ya1,xch,ych):
    """
    Parameters
    --------------
    xa1,ya1,xch,ych:float
      valores de coordenadas de antena 1 y central holi
    Return
    --------------
    d2:float
      valor de la distancia entre la antena 1 y central Holi
    """
    d2=math.sqrt((xa1-xch)**2-(ya1-ych)**2)

    return d2
#-------------------------------------------
def calcular_distancia_ch_a2(xch,ych,xa2,ya2):
    """
    Parameters
    --------------
    xch,ych,xa2,ya2:float
      valores de coordenadas de central Holi y antena 2
    Return
    --------------
    d3:float
      valor de la distancia entre la central Holi y antena 2
    """
    d3=math.sqrt((xch-xa2)**2-(ych-ya2)**2)

    return d3
#-------------------------------------------
def calcular_distancia_a2_c2(xa2,ya2,xc2,yc2):
    """
    Parameters
    --------------
    xa2,ya2,xc2,yc2:float
      valores de coordenadas de antena 2 y celular 2
    Return
    --------------
    d4:float
      valor de la distancia entre la antena a celular 2
    """
    d4= math.sqrt((xa2-xc2)**2+(ya2-yc2)**2)

    return d4
#-------------------------------------------
def obtener_distancia_total (d1,d2,d3,d4):
    """
    Parameters
    --------------
    d1,d2,d3,d4:float
      valores de las distancias
    Return
    --------------
    dt:float
      valor total de las distancias
    """

    dt=d1+d2+d3+d4

    return dt

#======================================================================
#          E S P A C I O    P R E _ _ C O N F I G U R A D O
# =====================================================================

#======================================================================
#   Algoritmo principal Punto de entrada a la aplicación (Conquistar)
# =====================================================================
#lectura coordenadas celular 1
xc1=float(input("Celular 1: Coordenada en x= "))
yc1=float(input("Celular 1: Coordenada en y= "))

#lectura coordenadas antena 1
xa1=float(input("\nAntena 1: Coordenada en x= "))
ya1=float(input("Antena 1: Coordenada en y= "))

#lectura coordenadas central holi 
xch=float(input("\nCentral Holi: Coordenada en x= "))
ych=float(input("Central Holi: Coordenada en y= "))

#lectura coordenadas antena 2
xa2=float(input("\nAntena 2: Coordenada en x= "))
ya2=float(input("Antena 2: Coordenada en y= "))

#lectura coordenadas celular 2
xc2=float(input("\nCelular 2: Coordenada en x= "))
yc2=float(input("Celular 2: Coordenada en y= "))

d1=calcular_distancia_c1_a1(xc1,yc1,xa1,ya1)
d2=calcular_distancia_a1_ch(xa1,ya1,xch,ych)
d3=calcular_distancia_ch_a2(xch,ych,xa2,ya2)
d4=calcular_distancia_a2_c2(xa2,ya2,xc2,yc2)

distancia_total=obtener_distancia_total (d1,d2,d3,d4)
print("\n***************************\nLa distancia total es: ",distancia_total)


