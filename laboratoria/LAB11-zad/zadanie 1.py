a = 3
b= 5
c = 2.5

PowSufit = (a*b)
print("Powierzchnia sufitu o wymiarach 5mx3m = ",PowSufit,"m^2")
PowSciany1=(a*c)
print("Powierzchnia sufitu o wymiarach 3mx2.5m = ",PowSciany1,"m^2")
PowSciany2 = (b*c)
print("Powierzchnia sufitu o wymiarach 3mx2.5m = ",PowSciany2,"m^2")
Okno = (1.4*1.1)
print("Powierzchnia okna o wymiarach 1.4mx1.1 = ")
Drzwi = (2*0.8)
print("Powierzchnia drzwi o wymiarach 2m x 0.8m =",Drzwi,"m^2")
PowCeli1 = (2 * PowSciany1 + 2 * PowSciany2 + 2 * PowSufit)
print("Całkowita powierzchnia celi bez drzwi i okien = ",PowCeli1,"m^2")
PowCeli2 = (2 * PowSciany1 + 2 * PowSciany2 + 2 * PowSufit - Drzwi -Okno)
print("Całkowita powierzchnia celi = ", PowCeli2,"m^2")
RozPowCel = (PowCeli1 - PowCeli2)
print("Różnica powierzchni celi = ",RozPowCel,"m^2")




