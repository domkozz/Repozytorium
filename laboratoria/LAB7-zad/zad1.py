import operator
menu = {​​​​
"Pizza Margarita" : 18.50,
"Pizza Peperoni" : 20.50,
"Pizza Wegetarjańska" : 45.50,
"Pizza Wiejska" : 24.50,
"Pizza Z Szynką" : 20.50,
"Pizza Cztery Sery" : 16.50,
"PIzza Diablo" : 34.50,
"Pizza Feliciana" : 19.50,
"Pizza Z Szynką I Grzybami" : 25.50,
"Pizza Z Owocami Morza" : 30.50,
}​​​​
sorted_menu= sorted(menu.items(), key=operator.itemgetter(1))
print("Menu")
for danie, cena in menu.items():
print(danie, cena)
print(sorted_menu)
del sorted_menu[0]
del sorted_menu[-1]
print(sorted_menu)
a = (input("Podaj nazwę nowej pizzy: "))
b = (input("Podaj cenę nowej pizzy: "))
menu[a] = b
print("Nowe Menu")
for danie, cena in menu.items():
print(danie, cena)
