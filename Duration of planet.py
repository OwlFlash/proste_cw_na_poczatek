import math
odległość_Ziemii = 150 *pow(10,9)
okres_Ziemii = pow(1314000,2) #w kwadracie
print ("Podaj nazwę planety")
planeta = input()
print("Podaj odległość (W METRACH) planety od Słońca"),format(planeta)
odległość =int( input())
d = float (odległość/odległość_Ziemii)
okres =( math.sqrt( (pow(d, 3))*okres_Ziemii ))/3600
print("Okres planety :{} o odległości od Słońca równej : {} metrów wynosi : {} dni".format(planeta,odległość,okres))

